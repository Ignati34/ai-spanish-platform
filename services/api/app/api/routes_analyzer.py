from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.analyzer import TextAnalyzeRequest, TextAnalyzeResponse
from app.services.usage_guard import check_ai_quota, record_ai_usage

router = APIRouter(prefix='/analyze', tags=['text-analyzer'])


@router.post('/text', response_model=TextAnalyzeResponse)
async def analyze_text(payload: TextAnalyzeRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    check_ai_quota(db, current_user)
    orchestrator = AgentOrchestrator()
    result = await orchestrator.analyze_text(text=payload.text, native_language=payload.native_language)
    record_ai_usage(db, current_user, orchestrator.ai.last_usage)
    return TextAnalyzeResponse(**result)
