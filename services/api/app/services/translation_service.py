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

from app.models.course import Lesson, LessonTranslation, ReadingResource, ReadingTranslation
from app.services.ai_gateway import AIGateway
from app.services.ai.prompts import LANG_NAMES

logger = logging.getLogger('translation_service')

SUPPORTED = set(LANG_NAMES.keys())  # ru, uk, ar, fr, es, en

_CYRILLIC = None  # lazy regex cache


def _has_cyrillic(text: str) -> bool:
    import re
    global _CYRILLIC
    if _CYRILLIC is None:
        _CYRILLIC = re.compile(r'[\u0400-\u04FF]')
    return bool(_CYRILLIC.search(text or ''))


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


def _hash_obj(obj) -> str:
    """Stable hash of an arbitrary JSON-able object (for cache invalidation)."""
    import json
    return _hash(json.dumps(obj, ensure_ascii=False, sort_keys=True))


async def _tr_field(gw: AIGateway, text: str, target: str, source: str) -> str:
    """Translate one short field, degrading to the source text on any failure."""
    try:
        out = await gw.translate(text, target_language=target, source_language=source)
    except Exception as exc:  # pragma: no cover - provider/network failure
        logger.warning('field translation failed (lang=%s): %s', target, exc)
        return text
    return (out or '').strip() or text


async def get_exercises(db: Session, lesson: Lesson, language: str | None,
                        gateway: AIGateway | None = None) -> list[dict]:
    """Return the lesson's exercises with prompt/explanation in `language`.

    Only Russian text is translated: Spanish practice stems (prompts without Cyrillic),
    options and correct_answer are kept verbatim so the exercise still tests Spanish.
    Cached per (lesson, language) in LessonTranslation.exercises. Degrades to source.
    """
    content = lesson.content_json or {}
    source = content.get('exercises') or []
    source_lang = _norm(lesson.native_language or 'ru')
    target = _norm(language)

    if not source or not needs_translation(target, source_lang):
        return source

    src_hash = _hash_obj(source)
    row = (
        db.query(LessonTranslation)
        .filter(LessonTranslation.lesson_id == lesson.id, LessonTranslation.language == target)
        .first()
    )
    if row and row.exercises_hash == src_hash and row.exercises:
        return row.exercises

    gw = gateway or AIGateway()
    localized: list[dict] = []
    changed = False
    for ex in source:
        new_ex = dict(ex)
        prompt = ex.get('prompt') or ''
        expl = ex.get('explanation') or ''
        # Prompt: translate only if it carries native-language instruction text
        # (Spanish-only fill-in stems like "Yo ___ estudiante." are left untouched).
        if prompt and _has_cyrillic(prompt):
            t = await _tr_field(gw, prompt, target, source_lang)
            if t != prompt:
                new_ex['prompt'] = t
                changed = True
        if expl:
            t = await _tr_field(gw, expl, target, source_lang)
            if t != expl:
                new_ex['explanation'] = t
                changed = True
        localized.append(new_ex)

    if not changed:  # stub/identity provider — nothing cached, serve source
        return source

    try:
        if row:
            row.exercises = localized
            row.exercises_hash = src_hash
        else:
            db.add(LessonTranslation(lesson_id=lesson.id, language=target,
                                     exercises=localized, exercises_hash=src_hash))
        db.commit()
    except Exception as exc:  # pragma: no cover
        db.rollback()
        logger.warning('caching exercise translation failed: %s', exc)
    return localized


async def get_reading_translation(db: Session, resource: ReadingResource, language: str | None,
                                  gateway: AIGateway | None = None) -> dict:
    """Return {title, body} for a reading text in `language` (source language 'es').

    Only kind='text' resources are translated; on any miss/failure the Spanish source
    is returned so the reader always has content. Cached in reading_translations.
    """
    src_title = resource.title or ''
    src_body = resource.body or ''
    target = _norm(language)
    result = {'title': src_title, 'body': src_body}

    if resource.kind != 'text' or not needs_translation(target, 'es'):
        return result

    src_hash = _hash(src_title + '\n' + src_body)
    row = (
        db.query(ReadingTranslation)
        .filter(ReadingTranslation.resource_id == resource.id, ReadingTranslation.language == target)
        .first()
    )
    if row and row.source_hash == src_hash and row.body:
        return {'title': row.title or src_title, 'body': row.body}

    gw = gateway or AIGateway()
    title_t = await _tr_field(gw, src_title, target, 'es') if src_title else src_title
    body_t = await _tr_field(gw, src_body, target, 'es') if src_body else src_body
    if body_t == src_body and title_t == src_title:  # identity/stub — don't cache
        return result

    try:
        if row:
            row.title, row.body, row.source_hash = title_t, body_t, src_hash
        else:
            db.add(ReadingTranslation(resource_id=resource.id, language=target,
                                      title=title_t, body=body_t, source_hash=src_hash))
        db.commit()
    except Exception as exc:  # pragma: no cover
        db.rollback()
        logger.warning('caching reading translation failed: %s', exc)
    return {'title': title_t, 'body': body_t}
