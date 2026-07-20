"""AI quota enforcement + usage recording, backed by UserEntitlement / UsageCounter.

Besides bumping the per-period UsageCounter, each metered call also appends a
per-request AIUsageLog row with an estimated cost, so the admin Usage & Costs view
has real time-series/breakdown data. Logging never breaks the request path.
"""
from __future__ import annotations

import logging

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.models.usage import AIUsageLog
from app.models.user import User
from app.services.ai_pricing import estimate_audio_cost, estimate_chat_cost
from app.services.billing_service import EntitlementsService, UsageService

logger = logging.getLogger('usage_guard')
settings = get_settings()


def _log_ai(db: Session, user: User, agent_name: str, model_name: str | None,
            input_tokens: int = 0, output_tokens: int = 0, audio_seconds: float = 0.0,
            image_count: int = 0, estimated_cost: float = 0.0) -> None:
    """Append a per-request AIUsageLog row. Best-effort: never raises."""
    try:
        db.add(AIUsageLog(
            user_id=user.id,
            agent_name=agent_name,
            model_name=model_name,
            input_tokens=int(input_tokens),
            output_tokens=int(output_tokens),
            audio_seconds=float(audio_seconds),
            image_count=int(image_count),
            estimated_cost=float(estimated_cost),
        ))
    except Exception as exc:  # pragma: no cover - logging must not break requests
        logger.warning('AIUsageLog append failed: %s', exc)


def check_ai_quota(db: Session, user: User):
    """Raise 402 if the user hit their monthly AI request cap. Returns entitlement."""
    entitlement = EntitlementsService(db).get_or_create_for_user(user)
    counter = UsageService(db).get_or_create_counter(user.id)
    limit = entitlement.max_ai_requests_month or 0
    if limit and counter.ai_requests_used >= limit:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail='Monthly AI request limit reached for your plan',
        )
    return entitlement


def record_ai_usage(db: Session, user: User, usage: dict | None, requests: int = 1,
                    agent_name: str = 'chat') -> None:
    usage = usage or {}
    in_tok = int(usage.get('input_tokens', 0))
    out_tok = int(usage.get('output_tokens', 0))
    UsageService(db).increment(
        user.id,
        ai_requests_used=int(requests),
        input_tokens_used=in_tok,
        output_tokens_used=out_tok,
    )
    _log_ai(db, user, agent_name, settings.ai_model, input_tokens=in_tok, output_tokens=out_tok,
            estimated_cost=estimate_chat_cost(settings.ai_model, in_tok, out_tok))
    db.commit()


def check_transcription_quota(db: Session, user: User):
    """Raise 402 if the user hit their monthly transcription-minutes cap."""
    entitlement = EntitlementsService(db).get_or_create_for_user(user)
    counter = UsageService(db).get_or_create_counter(user.id)
    limit_minutes = entitlement.max_transcription_minutes_month or 0
    if limit_minutes and counter.transcription_seconds_used >= limit_minutes * 60:
        raise HTTPException(
            status_code=status.HTTP_402_PAYMENT_REQUIRED,
            detail='Monthly transcription limit reached for your plan',
        )
    return entitlement


def record_transcription_usage(db: Session, user: User, seconds: float | int | None) -> None:
    secs = float(seconds or 0)
    UsageService(db).increment(user.id, transcription_seconds_used=int(secs))
    _log_ai(db, user, 'transcription', settings.stt_model, audio_seconds=secs,
            estimated_cost=estimate_audio_cost(secs, 'stt'))
    db.commit()


def record_tts_usage(db: Session, user: User, seconds: float | int | None) -> None:
    secs = float(seconds or 0)
    UsageService(db).increment(user.id, tts_seconds_used=int(secs))
    _log_ai(db, user, 'tts', settings.tts_model, audio_seconds=secs,
            estimated_cost=estimate_audio_cost(secs, 'tts'))
    db.commit()
