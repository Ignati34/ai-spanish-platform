"""Spaced repetition (SM-2). Turns one-off practice into scheduled long-term memory.

State lives in one FlashcardReview row per (user, card): ease_factor, interval_days,
repetitions, next_review_at. New cards (no row) are treated as due immediately.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

from sqlalchemy import and_, or_
from sqlalchemy.orm import Session

from app.models.flashcard import Flashcard, FlashcardReview
from app.models.user import User

# UI grade -> SM-2 quality (0..5)
GRADE_Q = {'again': 1, 'hard': 3, 'good': 4, 'easy': 5}
_MASTERED_DAYS = 21


def _now() -> datetime:
    return datetime.now(timezone.utc)


def _aware(dt):
    """Coerce a possibly-naive datetime (e.g. from SQLite) to UTC-aware."""
    if dt is None:
        return None
    return dt if dt.tzinfo is not None else dt.replace(tzinfo=timezone.utc)


def _state(db: Session, user: User, card_id) -> FlashcardReview | None:
    return (db.query(FlashcardReview)
            .filter(FlashcardReview.user_id == user.id, FlashcardReview.flashcard_id == card_id)
            .first())


def review(db: Session, user: User, card_id, grade: str) -> dict:
    q = GRADE_Q.get((grade or '').lower(), 4)
    state = _state(db, user, card_id)
    if not state:
        state = FlashcardReview(user_id=user.id, flashcard_id=card_id, ease_factor=2.5, interval_days=0, repetitions=0)
        db.add(state)

    ease = state.ease_factor or 2.5
    reps = state.repetitions or 0
    interval = state.interval_days or 0

    if q < 3:
        reps = 0
        interval = 0                       # relearn: due again this session
    else:
        reps += 1
        if reps == 1:
            interval = 1
        elif reps == 2:
            interval = 6
        else:
            interval = max(1, round(interval * ease))
        ease = max(1.3, ease + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)))

    state.quality_score = q
    state.ease_factor = round(ease, 3)
    state.repetitions = reps
    state.interval_days = interval
    state.reviewed_at = _now()
    state.next_review_at = _now() + timedelta(days=interval) if interval > 0 else _now()
    db.commit()
    return {
        'card_id': str(card_id), 'interval_days': interval, 'ease_factor': state.ease_factor,
        'repetitions': reps, 'next_review_at': state.next_review_at,
    }


def _card_payload(c: Flashcard, status: str) -> dict:
    return {'id': str(c.id), 'front': c.front, 'back': c.back, 'card_type': c.card_type,
            'example_sentence': c.example_sentence, 'status': status}


def due_cards(db: Session, user: User, limit: int = 20) -> list[dict]:
    now = _now()
    reviewed_ids = {r.flashcard_id: r for r in db.query(FlashcardReview).filter(FlashcardReview.user_id == user.id).all()}

    out: list[dict] = []
    # 1) due (previously reviewed, next_review_at <= now)
    due_ids = [cid for cid, r in reviewed_ids.items() if r.next_review_at is None or _aware(r.next_review_at) <= now]
    if due_ids:
        for c in db.query(Flashcard).filter(Flashcard.user_id == user.id, Flashcard.id.in_(due_ids)).limit(limit).all():
            out.append(_card_payload(c, 'review'))
    # 2) new (never reviewed)
    if len(out) < limit:
        new_cards = (db.query(Flashcard)
                     .filter(Flashcard.user_id == user.id, ~Flashcard.id.in_(list(reviewed_ids.keys()) or ['00000000-0000-0000-0000-000000000000']))
                     .limit(limit - len(out)).all())
        out.extend(_card_payload(c, 'new') for c in new_cards)
    return out[:limit]


def stats(db: Session, user: User) -> dict:
    now = _now()
    total_cards = db.query(Flashcard).filter(Flashcard.user_id == user.id).count()
    reviews = db.query(FlashcardReview).filter(FlashcardReview.user_id == user.id).all()
    reviewed = len(reviews)
    due = sum(1 for r in reviews if r.next_review_at is None or _aware(r.next_review_at) <= now)
    mastered = sum(1 for r in reviews if (r.interval_days or 0) >= _MASTERED_DAYS)
    learning = reviewed - mastered
    new = max(0, total_cards - reviewed)
    return {'total': total_cards, 'new': new, 'due': due + new, 'learning': learning, 'mastered': mastered}
