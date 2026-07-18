"""Voice Tutor: spoken/typed dialogue in Spanish.

Loop: student speaks (STT) or types -> tutor replies in Spanish + correction in the
student's native language + a score -> reply is voiced (TTS). Reuses the STT wired in
the previous phase; adds TTS and the conversational turn via the AI gateway.
"""
from __future__ import annotations

import base64

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.core.config import get_settings
from app.db.session import get_db
from app.services.security.upload_guard import scan_upload_or_raise
from app.models.user import User
from app.models.voice import VoiceMessage, VoiceSession
from app.services.extraction_service import is_audio
from app.services import progress_service
from app.services.storage_service import storage_service
from app.services.usage_guard import (
    check_ai_quota, check_transcription_quota, record_ai_usage,
    record_transcription_usage, record_tts_usage,
)

settings = get_settings()
router = APIRouter(prefix='/voice', tags=['voice'])

_MIME = {'mp3': 'audio/mpeg', 'opus': 'audio/ogg', 'aac': 'audio/aac', 'wav': 'audio/wav', 'flac': 'audio/flac'}


def _own_session(db: Session, user: User, session_id: str) -> VoiceSession:
    s = db.get(VoiceSession, session_id)
    if not s or s.user_id != user.id:
        raise HTTPException(status_code=404, detail='Session not found')
    return s


async def _voice_and_store(orch: AgentOrchestrator, db: Session, user: User, text: str) -> tuple[str | None, str | None]:
    """TTS `text`; return (audio_b64, audio_url). Empty audio degrades to text-only."""
    audio = await orch.synthesize(text=text, language='es')
    if not audio:
        return None, None
    record_tts_usage(db, user, max(1, len(text) // 15))
    url = storage_service.save(user.id, f'tts.{settings.tts_format}', audio, _MIME.get(settings.tts_format, 'audio/mpeg'))
    return base64.b64encode(audio).decode('ascii'), url


@router.get('/status')
def status_():
    return {'module': 'voice', 'status': 'tutor_ready'}


@router.post('/sessions')
async def create_session(payload: dict, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    check_ai_quota(db, current_user)
    scenario = payload.get('scenario', 'restaurant')
    cefr = payload.get('cefr_level', 'A1')
    native = payload.get('native_language', current_user.native_language or 'ru')

    session = VoiceSession(user_id=current_user.id, scenario=scenario, cefr_level=cefr, native_language=native, status='active')
    db.add(session)
    db.flush()

    orch = AgentOrchestrator()
    reply = await orch.voice_reply([], '(The student just joined. Greet them in Spanish and start the scenario.)', scenario, cefr, native)
    record_ai_usage(db, current_user, orch.ai.last_usage)
    reply_es = reply.get('reply_es', '¡Hola! ¿Empezamos?')

    audio_b64, audio_url = await _voice_and_store(orch, db, current_user, reply_es)
    db.add(VoiceMessage(session_id=session.id, user_id=current_user.id, role='assistant', transcript=reply_es, audio_url=audio_url))
    db.commit()

    return {
        'session_id': str(session.id), 'scenario': scenario, 'cefr_level': cefr, 'native_language': native,
        'reply_es': reply_es, 'audio_b64': audio_b64, 'audio_mime': _MIME.get(settings.tts_format, 'audio/mpeg'),
    }


@router.post('/sessions/{session_id}/message')
async def send_message(
    session_id: str,
    audio: UploadFile | None = File(default=None),
    text: str | None = Form(default=None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    session = _own_session(db, current_user, session_id)
    check_ai_quota(db, current_user)

    # 1) Resolve the student's message (speech -> text, or typed text).
    user_text = (text or '').strip()
    if audio is not None:
        if not is_audio(audio.filename or '', audio.content_type):
            raise HTTPException(status_code=415, detail='Expected an audio file')
        check_transcription_quota(db, current_user)
        data = await audio.read()
        scan_upload_or_raise(data, audio.filename or 'clip')
        stt = await AgentOrchestrator().transcribe(data=data, filename=audio.filename or 'clip.webm', language='es')
        user_text = (stt.get('text') or '').strip()
        record_transcription_usage(db, current_user, stt.get('duration_seconds'))
    if not user_text:
        raise HTTPException(status_code=422, detail='No message (empty audio/text)')

    db.add(VoiceMessage(session_id=session.id, user_id=current_user.id, role='user', transcript=user_text))
    db.flush()

    # 2) Build history and get the tutor's turn.
    prior = db.query(VoiceMessage).filter(VoiceMessage.session_id == session.id).order_by(VoiceMessage.created_at.asc()).all()
    history = [{'role': m.role, 'text': m.transcript or ''} for m in prior]

    orch = AgentOrchestrator()
    reply = await orch.voice_reply(history, user_text, session.scenario, session.cefr_level, session.native_language)
    record_ai_usage(db, current_user, orch.ai.last_usage)
    reply_es = reply.get('reply_es', '')
    correction = reply.get('correction', '')
    score = reply.get('score', 0.0)

    # 3) Voice the reply.
    if correction:
        progress_service.record_mistake(db, current_user, original=user_text, corrected=correction,
                                        explanation=correction, mistake_type='speaking',
                                        source_type='voice', source_id=session.id)
    audio_b64, audio_url = await _voice_and_store(orch, db, current_user, reply_es)
    db.add(VoiceMessage(
        session_id=session.id, user_id=current_user.id, role='assistant',
        transcript=reply_es, audio_url=audio_url, feedback_json={'correction': correction, 'score': score},
    ))
    db.commit()

    return {
        'user_text': user_text, 'reply_es': reply_es, 'correction': correction, 'score': score,
        'audio_b64': audio_b64, 'audio_mime': _MIME.get(settings.tts_format, 'audio/mpeg'),
    }


@router.get('/sessions/{session_id}')
def get_session(session_id: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    session = _own_session(db, current_user, session_id)
    rows = db.query(VoiceMessage).filter(VoiceMessage.session_id == session.id).order_by(VoiceMessage.created_at.asc()).all()
    return {
        'session_id': str(session.id), 'scenario': session.scenario, 'cefr_level': session.cefr_level,
        'messages': [
            {'role': m.role, 'text': m.transcript, 'feedback': m.feedback_json, 'created_at': m.created_at}
            for m in rows
        ],
    }


@router.post('/transcribe')
async def transcribe(
    file: UploadFile = File(...),
    language: str = Form('es'),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Standalone STT (also used by Upload Studio's audio path)."""
    if not is_audio(file.filename or '', file.content_type):
        raise HTTPException(status_code=415, detail='Expected an audio file')
    check_transcription_quota(db, current_user)
    data = await file.read()
    scan_upload_or_raise(data, file.filename or 'audio')
    max_bytes = settings.max_upload_mb * 1024 * 1024
    if len(data) > max_bytes:
        raise HTTPException(status_code=413, detail=f'File exceeds {settings.max_upload_mb} MB')
    stt = await AgentOrchestrator().transcribe(data=data, filename=file.filename or 'audio', language=language)
    record_transcription_usage(db, current_user, stt.get('duration_seconds'))
    return {'text': stt.get('text', ''), 'duration_seconds': stt.get('duration_seconds', 0.0), 'segments': stt.get('segments', [])}
