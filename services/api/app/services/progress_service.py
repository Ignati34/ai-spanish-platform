"""Personalization layer: aggregate mistakes into weak spots and a study plan.

Mistakes are recorded from several sources (diagnostic gaps, voice corrections,
exercise errors) into UserMistake, then aggregated here so the rest of the product
can target the learner's actual weak points.
"""
from __future__ import annotations

from sqlalchemy.orm import Session

from app.models.diagnostic import DiagnosticResult
from app.models.user import User, UserProfile
from app.models.vocabulary import UserMistake


def record_mistake(db: Session, user: User, *, original: str, corrected: str, explanation: str | None = None,
                   grammar_topic: str | None = None, mistake_type: str = 'grammar',
                   source_type: str | None = None, source_id=None) -> None:
    db.add(UserMistake(
        user_id=user.id, mistake_type=mistake_type,
        original_text=(original or '')[:2000] or '-', corrected_text=(corrected or '')[:2000] or '-',
        explanation=explanation, grammar_topic=grammar_topic, source_type=source_type, source_id=source_id,
    ))


def record_gaps(db: Session, user: User, gaps: list[str], source_type: str = 'diagnostic', source_id=None) -> None:
    for gap in (gaps or [])[:8]:
        gap = str(gap).strip()
        if gap:
            record_mistake(db, user, original=gap, corrected=gap, mistake_type='gap',
                           grammar_topic=gap, source_type=source_type, source_id=source_id)


def weak_spots(db: Session, user: User, limit: int = 8) -> list[dict]:
    rows = (db.query(UserMistake)
            .filter(UserMistake.user_id == user.id)
            .order_by(UserMistake.created_at.desc()).limit(500).all())
    agg: dict[str, dict] = {}
    for m in rows:
        key = (m.grammar_topic or m.mistake_type or 'general').strip()
        entry = agg.setdefault(key, {'topic': key, 'count': 0, 'last_at': None, 'examples': []})
        entry['count'] += 1
        if entry['last_at'] is None:
            entry['last_at'] = m.created_at
        if m.explanation and len(entry['examples']) < 2:
            entry['examples'].append(m.explanation[:160])
    ranked = sorted(agg.values(), key=lambda e: e['count'], reverse=True)
    return ranked[:limit]


def current_level(db: Session, user: User) -> str:
    profile = db.query(UserProfile).filter(UserProfile.user_id == user.id).first()
    return (profile.current_cefr_level if profile and profile.current_cefr_level else 'A1')


def study_plan(db: Session, user: User, spots: list[dict]) -> list[str]:
    # Start from the latest diagnostic plan (if any), then add targeted items for top gaps.
    plan: list[str] = []
    latest = (db.query(DiagnosticResult)
              .filter(DiagnosticResult.user_id == user.id)
              .order_by(DiagnosticResult.created_at.desc()).first())
    if latest and latest.plan_json:
        plan.extend([str(x) for x in latest.plan_json][:3])
    for spot in spots[:3]:
        plan.append(f'Practice: {spot["topic"]} ({spot["count"]}×)')
    # de-dup, keep order
    seen, out = set(), []
    for item in plan:
        if item not in seen:
            seen.add(item); out.append(item)
    return out[:6]


def overview(db: Session, user: User) -> dict:
    spots = weak_spots(db, user)
    total = db.query(UserMistake).filter(UserMistake.user_id == user.id).count()
    recent = (db.query(UserMistake).filter(UserMistake.user_id == user.id)
              .order_by(UserMistake.created_at.desc()).limit(10).all())
    return {
        'level': current_level(db, user),
        'total_mistakes': total,
        'weak_spots': spots,
        'study_plan': study_plan(db, user, spots),
        'recent': [
            {'type': m.mistake_type, 'topic': m.grammar_topic, 'original': m.original_text,
             'corrected': m.corrected_text, 'explanation': m.explanation, 'at': m.created_at}
            for m in recent
        ],
    }
