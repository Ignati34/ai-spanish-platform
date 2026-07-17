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
