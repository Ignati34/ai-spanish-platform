"""Lazy, cached translation of lesson theory into the learner's language.

Flow: if the requested language equals the source (or is unsupported), return the
original theory untouched. Otherwise return a cached LessonTranslation when the source
hasn't changed; on a miss, translate via the AI gateway, cache it, and return. Any
failure degrades gracefully to the source text.
"""
from __future__ import annotations

import hashlib
import logging

from sqlalchemy.orm import Session

from app.models.course import Lesson, LessonTranslation
from app.services.ai_gateway import AIGateway
from app.services.ai.prompts import LANG_NAMES

logger = logging.getLogger('translation_service')

SUPPORTED = set(LANG_NAMES.keys())  # ru, uk, ar, fr, es, en


def _norm(lang: str | None) -> str:
    return (lang or 'ru')[:2].lower()


def needs_translation(target: str | None, source: str | None) -> bool:
    """True only when we should call the translator for `target`."""
    t = _norm(target)
    s = _norm(source)
    return bool(t) and t in SUPPORTED and t != s


def _hash(text: str) -> str:
    return hashlib.sha256((text or '').encode('utf-8')).hexdigest()


async def get_theory(db: Session, lesson: Lesson, language: str | None,
                     gateway: AIGateway | None = None) -> str:
    """Return the lesson's theory in `language`, translating+caching on first use."""
    content = lesson.content_json or {}
    source_theory = content.get('theory', '') or ''
    source_lang = _norm(lesson.native_language or 'ru')
    target = _norm(language)

    if not source_theory or not needs_translation(target, source_lang):
        return source_theory

    src_hash = _hash(source_theory)
    row = (
        db.query(LessonTranslation)
        .filter(LessonTranslation.lesson_id == lesson.id, LessonTranslation.language == target)
        .first()
    )
    if row and row.source_hash == src_hash and row.theory:
        return row.theory

    try:
        gw = gateway or AIGateway()
        translated = await gw.translate(source_theory, target_language=target, source_language=source_lang)
    except Exception as exc:  # pragma: no cover - network/provider failure
        logger.warning('theory translation failed (lesson=%s, lang=%s): %s', lesson.id, target, exc)
        return source_theory

    translated = (translated or '').strip() or source_theory
    # Only cache a genuine translation (skip identity results from the stub).
    if translated != source_theory:
        try:
            if row:
                row.theory = translated
                row.source_hash = src_hash
            else:
                db.add(LessonTranslation(lesson_id=lesson.id, language=target, theory=translated, source_hash=src_hash))
            db.commit()
        except Exception as exc:  # pragma: no cover
            db.rollback()
            logger.warning('caching translation failed: %s', exc)
    return translated
