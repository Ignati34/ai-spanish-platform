from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.exercise import (
    GenerateExercisesRequest, GenerateExercisesResponse,
    SubmitExerciseRequest, SubmitExerciseResponse,
)
from app.services import progress_service
from app.services.usage_guard import check_ai_quota, record_ai_usage

router = APIRouter(prefix='/exercises', tags=['exercises'])


@router.post('/generate', response_model=GenerateExercisesResponse)
async def generate_exercises(payload: GenerateExercisesRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    check_ai_quota(db, current_user)
    orchestrator = AgentOrchestrator()
    result = await orchestrator.generate_exercises(
        text=payload.text, cefr_level=payload.cefr_level, native_language=payload.native_language,
    )
    record_ai_usage(db, current_user, orchestrator.ai.last_usage)
    return GenerateExercisesResponse(**result)


@router.post('/{exercise_id}/submit', response_model=SubmitExerciseResponse)
async def submit_exercise(exercise_id: str, payload: SubmitExerciseRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    check_ai_quota(db, current_user)
    orchestrator = AgentOrchestrator()
    # MVP: correct answer will later be fetched from DB by exercise_id.
    result = await orchestrator.check_answer(answer=payload.answer, correct_answer='привет')
    if not result.get('is_correct'):
        progress_service.record_mistake(db, current_user, original=payload.answer, corrected='',
                                        explanation=result.get('feedback'), mistake_type='exercise',
                                        source_type='exercise', source_id=None)
        db.commit()
    record_ai_usage(db, current_user, orchestrator.ai.last_usage)
    return SubmitExerciseResponse(**result)
