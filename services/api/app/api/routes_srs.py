"""Spaced repetition review queue (SM-2)."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.services import motivation_service, srs_service

router = APIRouter(prefix='/srs', tags=['srs'])


@router.get('/due')
def due(limit: int = 20, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return {'cards': srs_service.due_cards(db, current_user, limit=limit), 'stats': srs_service.stats(db, current_user)}


@router.get('/stats')
def stats(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return srs_service.stats(db, current_user)


@router.post('/review')
def review(payload: dict, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    card_id = payload.get('card_id')
    grade = payload.get('grade', 'good')
    if not card_id:
        raise HTTPException(status_code=400, detail='card_id required')
    if grade not in srs_service.GRADE_Q:
        raise HTTPException(status_code=400, detail='grade must be one of again|hard|good|easy')
    result = srs_service.review(db, current_user, card_id, grade)
    motivation_service.record_activity(db, current_user, 1)
    return result


@router.delete('/cards')
def clear_cards(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Remove all of the current user's flashcards (e.g. old cards in the wrong language)."""
    deleted = srs_service.clear_user_cards(db, current_user)
    return {'deleted': deleted}
