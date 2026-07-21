"""Text analyzer: analyze pasted text, an uploaded file (document or audio/video via STT),
or a URL (web page / Google Doc). Returns CEFR estimate, a full translation, parts of
speech with translations, tense info, vocabulary and a summary."""
from __future__ import annotations

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.content.tense_guide import tense_info
from app.core.config import get_settings
from app.db.session import get_db
from app.models.user import User
from app.schemas.analyzer import TextAnalyzeRequest, TextAnalyzeResponse
from app.services.extraction_service import (
    ExtractionError, UnsupportedType, extract_text, is_audio, is_video,
)
from app.services.security.upload_guard import scan_upload_or_raise
from app.services.url_ingest import UrlError, fetch as url_fetch, filename_for, normalize_target
from app.services.usage_guard import (
    check_ai_quota, check_transcription_quota, record_ai_usage, record_transcription_usage,
)

settings = get_settings()
router = APIRouter(prefix='/analyze', tags=['text-analyzer'])

MAX_TEXT_CHARS = 20000


def _as_word_objs(items) -> list[dict]:
    out = []
    for it in items or []:
        if isinstance(it, dict):
            word = (it.get('word') or it.get('es') or '').strip()
            if word:
                out.append({'word': word, 'translation': (it.get('translation') or it.get('ru') or '').strip()})
        elif isinstance(it, str) and it.strip():
            out.append({'word': it.strip(), 'translation': ''})
    return out


def _finalize(result: dict, native_language: str, source_text: str = '') -> TextAnalyzeResponse:
    verbs = []
    for v in result.get('verbs') or []:
        if isinstance(v, dict):
            verbs.append({'word': (v.get('word') or '').strip(), 'tense': v.get('tense') or '', 'translation': (v.get('translation') or '').strip()})
        elif isinstance(v, str) and v.strip():
            verbs.append({'word': v.strip(), 'tense': '', 'translation': ''})
    result['verbs'] = verbs
    for key in ('nouns', 'adjectives', 'adverbs'):
        result[key] = _as_word_objs(result.get(key))
    tenses = [t for t in (result.get('tenses') or []) if isinstance(t, str)]
    result['tenses'] = tenses
    result['tense_info'] = tense_info(tenses, native_language)
    result.setdefault('translation', '')
    if source_text:
        result['source_text'] = source_text[:MAX_TEXT_CHARS]
    return TextAnalyzeResponse(**result)


async def _analyze(db: Session, user: User, text: str, native_language: str, source_text: str = '') -> TextAnalyzeResponse:
    check_ai_quota(db, user)
    orch = AgentOrchestrator()
    result = await orch.analyze_text(text=text[:MAX_TEXT_CHARS], native_language=native_language)
    record_ai_usage(db, user, orch.ai.last_usage, agent_name='analyze')
    return _finalize(result, native_language, source_text=source_text)


@router.post('/text', response_model=TextAnalyzeResponse)
async def analyze_text(payload: TextAnalyzeRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return await _analyze(db, current_user, payload.text, payload.native_language)


@router.post('/file', response_model=TextAnalyzeResponse)
async def analyze_file(
    file: UploadFile = File(...),
    native_language: str = Form('ru'),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    filename = file.filename or 'upload'
    data = await file.read()
    scan_upload_or_raise(data, filename)
    max_bytes = settings.max_upload_mb * 1024 * 1024
    if len(data) > max_bytes:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail=f'File exceeds {settings.max_upload_mb} MB')

    # Audio and video both go through speech-to-text (the transcription API accepts common
    # video containers like mp4 and extracts the audio track).
    if is_audio(filename, file.content_type) or is_video(filename, file.content_type):
        check_transcription_quota(db, current_user)
        stt = await AgentOrchestrator().transcribe(data=data, filename=filename, language='es')
        text = (stt.get('text') or '').strip()
        if not text:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Empty transcript')
        record_transcription_usage(db, current_user, float(stt.get('duration_seconds') or 0.0))
    else:
        try:
            text, _meta = extract_text(filename, data, file.content_type)
        except UnsupportedType as exc:
            raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail=str(exc)) from exc
        except ExtractionError as exc:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)) from exc

    return await _analyze(db, current_user, text, native_language, source_text=text)


class AnalyzeUrlRequest(BaseModel):
    url: str = Field(min_length=3, max_length=2000)
    native_language: str = 'ru'


@router.post('/url', response_model=TextAnalyzeResponse)
async def analyze_url(payload: AnalyzeUrlRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    try:
        fetch_url, kind, _label = normalize_target(payload.url)
        data, ctype, _final = await url_fetch(fetch_url, settings.max_upload_mb * 1024 * 1024)
    except UrlError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f'Could not fetch URL: {exc}') from exc
    try:
        text, _meta = extract_text(filename_for(kind, ctype), data, ctype)
    except (UnsupportedType, ExtractionError) as exc:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='No readable text found at that URL.') from exc
    return await _analyze(db, current_user, text, payload.native_language, source_text=text)
