"""Flashcards: generate from pasted text, from a file of any type (text/doc/pdf/image/
audio/video), or from voice. Directional: material can be Spanish (→ native back) or the
learner's native language (→ Spanish front). Generated cards are saved to a deck so they
enter spaced-repetition review.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.core.config import get_settings
from app.db.session import get_db
from app.models.flashcard import Flashcard, FlashcardDeck
from app.models.user import User
from app.schemas.flashcard import GenerateFlashcardsRequest, GenerateFlashcardsResponse
from app.services.extraction_service import (
    ExtractionError, UnsupportedType, extract_text, is_audio, is_image, is_video,
)
from app.services.media_service import MediaError, extract_audio_from_video
from app.services.usage_guard import (
    check_ai_quota, check_transcription_quota, record_ai_usage, record_transcription_usage,
)

settings = get_settings()
router = APIRouter(prefix='/flashcards', tags=['flashcards'])


def _persist_deck(db: Session, user: User, title: str, cards: list[dict], cefr: str, source_type: str) -> None:
    deck = FlashcardDeck(user_id=user.id, title=title[:255], source_type=source_type, cefr_level=cefr)
    db.add(deck)
    db.flush()
    for c in (cards or [])[:60]:
        db.add(Flashcard(
            deck_id=deck.id, user_id=user.id,
            front=str(c.get('front', ''))[:2000], back=str(c.get('back', ''))[:2000],
            card_type=c.get('card_type', 'word_translation'),
            example_sentence=(c.get('example_sentence') or None),
        ))
    db.commit()


@router.post('/generate', response_model=GenerateFlashcardsResponse)
async def generate_flashcards(payload: GenerateFlashcardsRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    check_ai_quota(db, current_user)
    orch = AgentOrchestrator()
    result = await orch.generate_flashcards(
        text=payload.text, native_language=payload.native_language, cefr_level=payload.cefr_level,
        source_language=payload.source_language,
    )
    record_ai_usage(db, current_user, orch.ai.last_usage)
    _persist_deck(db, current_user, result.get('deck_title', 'Deck'), result.get('cards', []), payload.cefr_level, 'flashcards_text')
    return GenerateFlashcardsResponse(**result)


@router.post('/from-file', response_model=GenerateFlashcardsResponse)
async def flashcards_from_file(
    file: UploadFile = File(...),
    native_language: str = Form('ru'),
    cefr_level: str = Form('A1'),
    source_language: str = Form('es'),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    filename = file.filename or 'material'
    mime = file.content_type
    check_ai_quota(db, current_user)
    data = await file.read()
    max_bytes = settings.max_upload_mb * 1024 * 1024
    if len(data) > max_bytes:
        raise HTTPException(status_code=413, detail=f'File exceeds {settings.max_upload_mb} MB')

    orch = AgentOrchestrator()
    text = ''

    if is_image(filename, mime):
        text = await orch.extract_image_text(data=data, mime_type=(mime or 'image/png'))
    elif is_audio(filename, mime):
        check_transcription_quota(db, current_user)
        stt = await orch.transcribe(data=data, filename=filename, language='es' if source_language == 'es' else source_language)
        text = (stt.get('text') or '').strip()
        record_transcription_usage(db, current_user, stt.get('duration_seconds'))
    elif is_video(filename, mime):
        check_transcription_quota(db, current_user)
        try:
            audio = extract_audio_from_video(data, filename)
        except MediaError as exc:
            raise HTTPException(status_code=422, detail=f'Could not process video: {exc}') from exc
        stt = await orch.transcribe(data=audio, filename='audio.mp3', language='es' if source_language == 'es' else source_language)
        text = (stt.get('text') or '').strip()
        record_transcription_usage(db, current_user, stt.get('duration_seconds'))
    else:
        try:
            text, _ = extract_text(filename, data, mime)
        except UnsupportedType as exc:
            raise HTTPException(status_code=415, detail=str(exc)) from exc
        except ExtractionError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    if not text.strip():
        raise HTTPException(status_code=422, detail='No text could be extracted from the file')

    result = await orch.generate_flashcards(
        text=text, native_language=native_language, cefr_level=cefr_level, source_language=source_language,
    )
    record_ai_usage(db, current_user, orch.ai.last_usage)
    _persist_deck(db, current_user, result.get('deck_title', filename), result.get('cards', []), cefr_level, 'flashcards_file')
    return GenerateFlashcardsResponse(**result)
