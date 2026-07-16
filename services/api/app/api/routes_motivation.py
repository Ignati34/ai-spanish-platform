"""Motivation: daily goal, streaks, reminder settings."""
from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.user import User
from app.services import motivation_service

router = APIRouter(prefix='/motivation', tags=['motivation'])


@router.get('/overview')
def overview(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return motivation_service.overview(db, current_user)


@router.post('/goal')
def set_goal(payload: dict, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    st = motivation_service.set_goal(db, current_user, int(payload.get('daily_goal', 20)))
    return {'daily_goal': st.daily_goal}


@router.post('/reminders')
def set_reminders(payload: dict, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    st = motivation_service.set_reminders(db, current_user, bool(payload.get('enabled', False)), payload.get('hour'))
    return {'reminders_enabled': st.reminders_enabled, 'reminder_hour': st.reminder_hour}
