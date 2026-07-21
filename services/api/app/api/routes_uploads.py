"""Upload Studio: turn pasted text, a document, OR an audio file into a lesson.

Audio path: file -> STT transcript -> the same lesson builder (analyze + flashcards
+ exercises). This closes the "bring any material, get a lesson" loop for audio.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.core.config import get_settings
from app.db.session import get_db
from app.services.security.upload_guard import scan_upload_or_raise
from app.models.upload import ExtractedText, Transcript, UploadedFile
from app.models.user import User
from app.schemas.upload import BuildFromTextRequest, GeneratedLessonOut
from app.services.extraction_service import (
    ExtractionError, UnsupportedType, ext_of, extract_text, is_audio, is_video,
)
from app.services.lesson_builder import build_lesson_from_text
from app.services.storage_service import storage_service
from app.services.url_ingest import (
    UrlError, fetch as url_fetch, filename_for, normalize_target,
)
from app.services.usage_guard import (
    check_ai_quota, check_transcription_quota, record_ai_usage, record_transcription_usage,
)

settings = get_settings()
router = APIRouter(prefix='/uploads', tags=['uploads'])


def _to_out(result, source: str, filename: str | None = None, transcript: str | None = None, duration: float | None = None) -> GeneratedLessonOut:
    return GeneratedLessonOut(
        lesson_id=result.lesson_id, deck_id=result.deck_id, title=result.title,
        cefr_estimate=result.analysis.get('cefr_estimate', 'A1'),
        summary=result.analysis.get('summary', ''),
        analysis=result.analysis, cards=result.cards, exercises=result.exercises,
        source=source, filename=filename, transcript=transcript, duration_seconds=duration,
    )


@router.post('/text', response_model=GeneratedLessonOut)
async def build_from_text(payload: BuildFromTextRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    check_ai_quota(db, current_user)
    result = await build_lesson_from_text(
        db, current_user, text=payload.text, native_language=payload.native_language,
        cefr_level=payload.cefr_level, source_type='raw_text', title=payload.title,
    )
    record_ai_usage(db, current_user, result.usage, requests=result.usage.get('ai_calls', 1))
    return _to_out(result, 'raw_text')


@router.post('/file', response_model=GeneratedLessonOut)
async def build_from_file(
    file: UploadFile = File(...),
    native_language: str = Form('ru'),
    cefr_level: str = Form('A1'),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    filename = file.filename or 'upload'
    audio = is_audio(filename, file.content_type) or is_video(filename, file.content_type)
    if audio:
        check_transcription_quota(db, current_user)
    check_ai_quota(db, current_user)

    data = await file.read()
    scan_upload_or_raise(data, filename)
    max_bytes = settings.max_upload_mb * 1024 * 1024
    if len(data) > max_bytes:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail=f'File exceeds {settings.max_upload_mb} MB')

    storage_url = storage_service.save(current_user.id, filename, data, file.content_type)
    uploaded = UploadedFile(
        user_id=current_user.id, original_filename=filename, file_type=ext_of(filename),
        mime_type=file.content_type, storage_url=storage_url, file_size=len(data), processing_status='uploaded',
    )
    db.add(uploaded)
    db.flush()

    transcript_text: str | None = None
    duration: float | None = None

    if audio:
        # Speech-to-text -> transcript -> lesson.
        stt = await AgentOrchestrator().transcribe(data=data, filename=filename, language='es')
        transcript_text = (stt.get('text') or '').strip()
        duration = float(stt.get('duration_seconds') or 0.0)
        if not transcript_text:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Empty transcript')
        db.add(Transcript(
            file_id=uploaded.id, user_id=current_user.id, language='es',
            transcript_text=transcript_text, duration_seconds=duration, segments_json=stt.get('segments'),
        ))
        record_transcription_usage(db, current_user, duration)
        uploaded.processing_status = 'transcribed'
        db.flush()
        text, source_type = transcript_text, 'transcript'
    else:
        try:
            text, meta = extract_text(filename, data, file.content_type)
        except UnsupportedType as exc:
            raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail=str(exc)) from exc
        except ExtractionError as exc:
            raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=str(exc)) from exc
        db.add(ExtractedText(file_id=uploaded.id, user_id=current_user.id, language='es', text=text, metadata_json=meta))
        uploaded.processing_status = 'extracted'
        db.flush()
        source_type = 'uploaded_file'

    result = await build_lesson_from_text(
        db, current_user, text=text, native_language=native_language, cefr_level=cefr_level,
        source_type=source_type, source_id=uploaded.id, title=filename,
    )
    uploaded.processing_status = 'lesson_ready'
    record_ai_usage(db, current_user, result.usage, requests=result.usage.get('ai_calls', 1))
    return _to_out(result, source_type, filename=filename, transcript=transcript_text, duration=duration)


class BuildFromUrlRequest(BaseModel):
    url: str = Field(min_length=3, max_length=2000)
    native_language: str = 'ru'
    cefr_level: str = 'A1'


@router.post('/url', response_model=GeneratedLessonOut)
async def build_from_url(payload: BuildFromUrlRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    check_ai_quota(db, current_user)
    try:
        fetch_url, kind, label = normalize_target(payload.url)
    except UrlError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

    max_bytes = settings.max_upload_mb * 1024 * 1024
    try:
        data, ctype, final_url = await url_fetch(fetch_url, max_bytes)
    except UrlError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except Exception as exc:  # network / HTTP errors
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f'Could not fetch URL: {exc}') from exc

    fname = filename_for(kind, ctype)
    try:
        text, meta = extract_text(fname, data, ctype)
    except UnsupportedType as exc:
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail=str(exc)) from exc
    except ExtractionError as exc:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='No readable text found at that URL. For Google Docs, share it as "anyone with the link".') from exc

    display = payload.url.strip()[:200]
    uploaded = UploadedFile(
        user_id=current_user.id, original_filename=display, file_type=('gdoc' if kind == 'gdoc' else 'url'),
        mime_type=ctype or 'text/html', storage_url=final_url, file_size=len(data), processing_status='extracted',
    )
    db.add(uploaded)
    db.flush()
    db.add(ExtractedText(file_id=uploaded.id, user_id=current_user.id, language='es', text=text, metadata_json={**meta, 'url': final_url, 'kind': kind}))

    result = await build_lesson_from_text(
        db, current_user, text=text, native_language=payload.native_language, cefr_level=payload.cefr_level,
        source_type='url', source_id=uploaded.id, title=(label if kind == 'gdoc' else display),
    )
    uploaded.processing_status = 'lesson_ready'
    record_ai_usage(db, current_user, result.usage, requests=result.usage.get('ai_calls', 1))
    return _to_out(result, 'url', filename=display)


@router.get('')
def list_uploads(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    rows = db.query(UploadedFile).filter(UploadedFile.user_id == current_user.id).order_by(UploadedFile.created_at.desc()).limit(50).all()
    return [
        {'id': str(r.id), 'filename': r.original_filename, 'file_type': r.file_type, 'status': r.processing_status, 'size': r.file_size, 'created_at': r.created_at}
        for r in rows
    ]
