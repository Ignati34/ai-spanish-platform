from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.flashcard import GenerateFlashcardsRequest, GenerateFlashcardsResponse
from app.services.usage_guard import check_ai_quota, record_ai_usage

router = APIRouter(prefix='/flashcards', tags=['flashcards'])


@router.post('/generate', response_model=GenerateFlashcardsResponse)
async def generate_flashcards(payload: GenerateFlashcardsRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    check_ai_quota(db, current_user)
    orchestrator = AgentOrchestrator()
    result = await orchestrator.generate_flashcards(
        text=payload.text, native_language=payload.native_language, cefr_level=payload.cefr_level,
    )
    record_ai_usage(db, current_user, orchestrator.ai.last_usage)
    return GenerateFlashcardsResponse(**result)
