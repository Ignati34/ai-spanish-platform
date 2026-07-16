"""AI quota enforcement + usage recording, backed by UserEntitlement / UsageCounter."""
from __future__ import annotations

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.services.billing_service import EntitlementsService, UsageService


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


def record_ai_usage(db: Session, user: User, usage: dict | None, requests: int = 1) -> None:
    usage = usage or {}
    UsageService(db).increment(
        user.id,
        ai_requests_used=int(requests),
        input_tokens_used=int(usage.get('input_tokens', 0)),
        output_tokens_used=int(usage.get('output_tokens', 0)),
    )
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
    UsageService(db).increment(user.id, transcription_seconds_used=int(seconds or 0))
    db.commit()


def record_tts_usage(db: Session, user: User, seconds: float | int | None) -> None:
    UsageService(db).increment(user.id, tts_seconds_used=int(seconds or 0))
    db.commit()
