"""Onboarding diagnostic: place the learner on the A1-C2 map and surface first gaps.

Reuses the AI gateway (assess_level) and deterministic MC scoring. Writes the result
to UserProfile.current_cefr_level so the rest of the product can personalize.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.content.diagnostic import SPEAKING_PROMPT, WRITING_PROMPT, public_questions, score_answers
from app.db.session import get_db
from app.models.diagnostic import DiagnosticResult
from app.models.user import User, UserProfile
from app.schemas.diagnostic import DiagnosticResultOut, DiagnosticSubmitRequest
from app.services import progress_service
from app.services.usage_guard import check_ai_quota, record_ai_usage

router = APIRouter(prefix='/diagnostic', tags=['diagnostic'])


@router.get('/questions')
def get_questions(native_language: str = 'ru', current_user: User = Depends(get_current_user)):
    lang = (native_language or current_user.native_language or 'ru')[:2]
    return {
        'questions': public_questions(),
        'writing_prompt': WRITING_PROMPT.get(lang, WRITING_PROMPT['en']),
        'speaking_prompt': SPEAKING_PROMPT.get(lang, SPEAKING_PROMPT['en']),
    }


@router.post('/submit', response_model=DiagnosticResultOut)
async def submit(payload: DiagnosticSubmitRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    check_ai_quota(db, current_user)
    native = (payload.native_language or current_user.native_language or 'ru')[:2]

    score = score_answers([a.model_dump() for a in payload.answers])

    orch = AgentOrchestrator()
    assessment = await orch.assess_level(payload.writing_sample, payload.speaking_sample, score, native)
    record_ai_usage(db, current_user, orch.ai.last_usage)

    recommended = assessment.get('recommended_level') or assessment.get('cefr_estimate') or 'A1'

    # Persist result
    db.add(DiagnosticResult(
        user_id=current_user.id, native_language=native,
        cefr_estimate=assessment.get('cefr_estimate', 'A1'), recommended_level=recommended,
        mc_score=score['ratio'], strengths_json=assessment.get('strengths'), gaps_json=assessment.get('gaps'),
        plan_json=assessment.get('study_plan'), summary=assessment.get('summary'),
        writing_sample=payload.writing_sample or None, speaking_sample=payload.speaking_sample or None,
    ))

    # Update the learner's placement so the rest of the app personalizes.
    profile = db.query(UserProfile).filter(UserProfile.user_id == current_user.id).first()
    if not profile:
        profile = UserProfile(user_id=current_user.id)
        db.add(profile)
    profile.current_cefr_level = recommended

    # Seed the personalization layer with the diagnosed gaps.
    progress_service.record_gaps(db, current_user, assessment.get('gaps', []), source_type='diagnostic')
    db.commit()

    return DiagnosticResultOut(
        cefr_estimate=assessment.get('cefr_estimate', 'A1'), recommended_level=recommended,
        mc_correct=score['correct'], mc_total=score['total'], mc_ratio=round(score['ratio'], 2),
        strengths=assessment.get('strengths', []), gaps=assessment.get('gaps', []),
        summary=assessment.get('summary', ''), study_plan=assessment.get('study_plan', []),
    )
