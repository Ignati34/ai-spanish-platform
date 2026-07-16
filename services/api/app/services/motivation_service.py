"""Motivation: daily goal, streaks, and Telegram reminders tied to due reviews.

Closes the learning loop: learned -> scheduled (SRS) -> reminded -> came back.
"""
from __future__ import annotations

from datetime import date, datetime, timedelta

from sqlalchemy.orm import Session

from app.models.motivation import MotivationState
from app.models.user import User, UserProfile
from app.services import srs_service


def get_or_create(db: Session, user: User) -> MotivationState:
    st = db.query(MotivationState).filter(MotivationState.user_id == user.id).first()
    if not st:
        st = MotivationState(user_id=user.id)
        db.add(st)
        db.flush()
    return st


def record_activity(db: Session, user: User, count: int = 1) -> MotivationState:
    """Count reviews toward today's goal and advance the streak when the goal is met."""
    st = get_or_create(db, user)
    today = date.today()
    if st.today_date != today:
        st.today_date = today
        st.today_count = 0
    st.today_count += count

    if st.today_count >= st.daily_goal and st.last_goal_date != today:
        if st.last_goal_date == today - timedelta(days=1):
            st.current_streak += 1
        else:
            st.current_streak = 1
        st.last_goal_date = today
        st.longest_streak = max(st.longest_streak or 0, st.current_streak)
    db.commit()
    return st


def overview(db: Session, user: User) -> dict:
    st = get_or_create(db, user)
    today = date.today()
    today_count = st.today_count if st.today_date == today else 0
    stats = srs_service.stats(db, user)
    db.commit()
    return {
        'daily_goal': st.daily_goal,
        'today_count': today_count,
        'goal_met': today_count >= st.daily_goal,
        'current_streak': st.current_streak if st.last_goal_date in (today, today - timedelta(days=1)) else 0,
        'longest_streak': st.longest_streak,
        'due': stats.get('due', 0),
        'reminders_enabled': st.reminders_enabled,
        'reminder_hour': st.reminder_hour,
    }


def set_goal(db: Session, user: User, daily_goal: int) -> MotivationState:
    st = get_or_create(db, user)
    st.daily_goal = max(1, min(500, int(daily_goal)))
    db.commit()
    return st


def set_reminders(db: Session, user: User, enabled: bool, hour: int | None = None) -> MotivationState:
    st = get_or_create(db, user)
    st.reminders_enabled = bool(enabled)
    if hour is not None:
        st.reminder_hour = max(0, min(23, int(hour)))
    db.commit()
    return st


def _local_now(tz_name: str) -> datetime:
    try:
        from zoneinfo import ZoneInfo
        return datetime.now(ZoneInfo(tz_name or 'UTC'))
    except Exception:
        return datetime.utcnow()


def send_due_reminders(db: Session) -> int:
    """Scheduler job: nudge users (via Telegram) who have due cards at their reminder hour."""
    from app.services.telegram_service import TelegramService

    tg = TelegramService()
    sent = 0
    states = db.query(MotivationState).filter(MotivationState.reminders_enabled.is_(True)).all()
    for st in states:
        user = db.get(User, st.user_id)
        if not user or not user.telegram_id:
            continue
        profile = db.query(UserProfile).filter(UserProfile.user_id == user.id).first()
        now_local = _local_now(profile.timezone if profile else 'UTC')
        if now_local.hour != st.reminder_hour:
            continue
        if st.last_reminded_date == now_local.date():
            continue
        stats = srs_service.stats(db, user)
        if stats.get('due', 0) <= 0:
            continue
        if st.today_date == now_local.date() and st.today_count >= st.daily_goal:
            continue  # already hit the goal today
        try:
            tg.send_message(
                user.telegram_id,
                f'¡Hola! Tienes {stats["due"]} tarjetas para repasar hoy. 🔥 Racha: {st.current_streak} días.',
            )
            st.last_reminded_date = now_local.date()
            sent += 1
        except Exception:
            continue
    db.commit()
    return sent
