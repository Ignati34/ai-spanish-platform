"""Role-play simulations: mini-missions on top of the Voice Tutor.

A scenario gives the AI a role and the learner a goal. Reuses STT (spoken input),
TTS (voiced reply) and VoiceSession/VoiceMessage for the dialogue; adds the goal +
hints and a per-turn goal-achievement judgement.
"""
from __future__ import annotations

import base64

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.content import simulations as sim_content
from app.core.config import get_settings
from app.db.session import get_db
from app.services.security.upload_guard import scan_upload_or_raise
from app.models.user import User
from app.models.voice import VoiceMessage, VoiceSession
from app.services import progress_service
from app.services.extraction_service import is_audio
from app.services.storage_service import storage_service
from app.services.usage_guard import (
    check_ai_quota, check_transcription_quota, record_ai_usage,
    record_transcription_usage, record_tts_usage,
)

settings = get_settings()
router = APIRouter(prefix='/simulations', tags=['simulations'])
_MIME = 'audio/mpeg'


def _own(db: Session, user: User, session_id: str) -> VoiceSession:
    s = db.get(VoiceSession, session_id)
    if not s or s.user_id != user.id:
        raise HTTPException(status_code=404, detail='Simulation not found')
    return s


async def _voice(orch: AgentOrchestrator, db: Session, user: User, text: str) -> tuple[str | None, str | None]:
    audio = await orch.synthesize(text=text, language='es')
    if not audio:
        return None, None
    record_tts_usage(db, user, max(1, len(text) // 15))
    url = storage_service.save(user.id, f'sim.{settings.tts_format}', audio, _MIME)
    return base64.b64encode(audio).decode('ascii'), url


@router.get('/scenarios')
def scenarios(native_language: str = 'ru', level: str | None = None, current_user: User = Depends(get_current_user)):
    lang = native_language or current_user.native_language or 'ru'
    return {'levels': ['A1', 'A2', 'B1', 'B2', 'C1', 'C2'], 'scenarios': sim_content.public_list(lang, level)}


@router.post('/start')
async def start(payload: dict, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    scenario = sim_content.get(payload.get('scenario_id', ''))
    if not scenario:
        raise HTTPException(status_code=404, detail='Unknown scenario')
    check_ai_quota(db, current_user)
    cefr = payload.get('cefr_level', 'A1')
    native = payload.get('native_language', current_user.native_language or 'ru')

    session = VoiceSession(user_id=current_user.id, scenario=scenario['id'], cefr_level=cefr, native_language=native, status='active')
    db.add(session)
    db.flush()

    orch = AgentOrchestrator()
    turn = await orch.simulation_turn(
        [], '(The student starts. Greet them in your role and invite them to begin.)',
        scenario['role'], scenario['goal_es'], cefr, native)
    record_ai_usage(db, current_user, orch.ai.last_usage)
    reply_es = turn.get('reply_es', '¡Hola! ¿Empezamos?')
    audio_b64, audio_url = await _voice(orch, db, current_user, reply_es)
    db.add(VoiceMessage(session_id=session.id, user_id=current_user.id, role='assistant', transcript=reply_es, audio_url=audio_url))
    db.commit()

    lang = native[:2]
    return {
        'session_id': str(session.id), 'scenario_id': scenario['id'],
        'title': scenario['title'].get(lang, scenario['title']['en']),
        'role': scenario['role'], 'goal': scenario['goal'].get(lang, scenario['goal']['en']),
        'hints': scenario['hints'], 'reply_es': reply_es, 'audio_b64': audio_b64, 'audio_mime': _MIME,
    }


@router.post('/{session_id}/message')
async def message(
    session_id: str,
    audio: UploadFile | None = File(default=None),
    text: str | None = Form(default=None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    session = _own(db, current_user, session_id)
    scenario = sim_content.get(session.scenario)
    if not scenario:
        raise HTTPException(status_code=400, detail='Scenario no longer available')
    check_ai_quota(db, current_user)

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
        raise HTTPException(status_code=422, detail='No message')

    db.add(VoiceMessage(session_id=session.id, user_id=current_user.id, role='user', transcript=user_text))
    db.flush()

    prior = db.query(VoiceMessage).filter(VoiceMessage.session_id == session.id).order_by(VoiceMessage.created_at.asc()).all()
    history = [{'role': m.role, 'text': m.transcript or ''} for m in prior]

    orch = AgentOrchestrator()
    turn = await orch.simulation_turn(history, user_text, scenario['role'], scenario['goal_es'], session.cefr_level, session.native_language)
    record_ai_usage(db, current_user, orch.ai.last_usage)
    reply_es = turn.get('reply_es', '')
    correction = turn.get('correction', '')
    score = turn.get('score', 0.0)
    goal_met = bool(turn.get('goal_met'))
    hint = turn.get('hint', '')

    if correction:
        progress_service.record_mistake(db, current_user, original=user_text, corrected=correction,
                                        explanation=correction, mistake_type='speaking',
                                        source_type='simulation', source_id=session.id)

    audio_b64, audio_url = await _voice(orch, db, current_user, reply_es)
    db.add(VoiceMessage(session_id=session.id, user_id=current_user.id, role='assistant', transcript=reply_es,
                        audio_url=audio_url, feedback_json={'correction': correction, 'score': score, 'goal_met': goal_met, 'hint': hint}))
    if goal_met:
        session.status = 'completed'
    db.commit()

    return {
        'user_text': user_text, 'reply_es': reply_es, 'correction': correction, 'score': score,
        'goal_met': goal_met, 'hint': hint, 'status': session.status,
        'audio_b64': audio_b64, 'audio_mime': _MIME,
    }


@router.get('/{session_id}')
def get_session(session_id: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    session = _own(db, current_user, session_id)
    rows = db.query(VoiceMessage).filter(VoiceMessage.session_id == session.id).order_by(VoiceMessage.created_at.asc()).all()
    return {
        'session_id': str(session.id), 'scenario_id': session.scenario, 'status': session.status,
        'messages': [{'role': m.role, 'text': m.transcript, 'feedback': m.feedback_json} for m in rows],
    }
