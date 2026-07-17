"""Progress & "My mistakes": aggregated weak spots, study plan, targeted practice."""
from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.services import progress_service
from app.services.usage_guard import check_ai_quota, record_ai_usage

router = APIRouter(prefix='/progress', tags=['progress'])


@router.get('/overview')
def overview(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return progress_service.overview(db, current_user)


@router.get('/mistakes')
def mistakes(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return {'weak_spots': progress_service.weak_spots(db, current_user, limit=20)}


@router.post('/record')
def record(payload: dict, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Record a concrete mistake made in an interactive exercise, so it shows up in
    'my mistakes' with the specific prompt, correct answer and explanation."""
    progress_service.record_mistake(
        db, current_user,
        original=str(payload.get('original', ''))[:2000],
        corrected=str(payload.get('corrected', ''))[:2000],
        explanation=payload.get('explanation'),
        grammar_topic=payload.get('topic'),
        mistake_type='exercise', source_type='practice',
    )
    db.commit()
    return {'ok': True}


@router.post('/practice')
async def practice(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Generate remedial exercises targeting the learner's top weak spots."""
    check_ai_quota(db, current_user)
    spots = progress_service.weak_spots(db, current_user, limit=4)
    topics = [s['topic'] for s in spots] or ['ser/estar', 'artículos']
    level = progress_service.current_level(db, current_user)
    orch = AgentOrchestrator()
    result = await orch.targeted_exercises(topics, level, current_user.native_language or 'ru')
    record_ai_usage(db, current_user, orch.ai.last_usage)
    return {'topics': topics, 'level': level, 'vocabulary': result.get('vocabulary', []), 'exercises': result.get('exercises', [])}
