#!/usr/bin/env python3
"""Pre-warm content translations so learners never wait on first open.

Covers three content types, each cached in its own table and idempotent (skips
what's already cached and unchanged, keyed by a source hash):
  * theory     — lesson theory            -> lesson_translations.theory
  * exercises  — exercise prompts/explan.  -> lesson_translations.exercises
  * reading    — library texts (title+body)-> reading_translations

Built-in dialogues ship pre-translated in app/content/dialogues.py, so they need no
warming. Run inside the API container (working dir: services/api) with a real provider
configured (AI_PROVIDER=openai, AI_API_KEY=...). Under the stub provider translations
are identity and are NOT cached (the script warns and does nothing useful).

Examples:
  python scripts/prewarm_translations.py                          # all types, uk,ar,fr,en
  python scripts/prewarm_translations.py --targets theory,exercises
  python scripts/prewarm_translations.py --langs uk,fr --level B1 --limit 5
  python scripts/prewarm_translations.py --force --sleep 0.3
"""
from __future__ import annotations

import argparse
import asyncio
import time

from app.core.config import get_settings
from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.models.course import Lesson, LessonTranslation, ReadingResource, ReadingTranslation
from app.services.ai_gateway import AIGateway
from app.services.ai_pricing import estimate_chat_cost
from app.services.translation_service import (
    SUPPORTED, _norm, get_theory, get_exercises, get_reading_translation, needs_translation,
)

DEFAULT_LANGS = ['uk', 'ar', 'fr', 'en']
ALL_TARGETS = ['theory', 'exercises', 'reading']


def _parse_csv(raw: str, allowed: set[str] | None = None) -> list[str]:
    out = []
    for part in (raw or '').split(','):
        v = part.strip().lower()
        if not v:
            continue
        code = _norm(v) if allowed is None else v
        if allowed is not None and v not in allowed:
            continue
        if allowed is None and (code not in SUPPORTED):
            continue
        if code not in out:
            out.append(code)
    return out


async def run(langs, targets, level, limit, force, sleep) -> int:
    settings = get_settings()
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    gw = AIGateway()

    is_stub = (settings.ai_provider or 'stub').lower() != 'openai' or not settings.ai_api_key
    if is_stub:
        print('WARNING: provider is not OpenAI (or AI_API_KEY is unset). Translations will be '
              'identity and will NOT be cached. Set AI_PROVIDER=openai and AI_API_KEY, then re-run.')

    lessons = []
    if 'theory' in targets or 'exercises' in targets:
        q = db.query(Lesson).filter(Lesson.lesson_type == 'curriculum')
        if level:
            q = q.filter(Lesson.cefr_level == level.upper())
        lessons = q.order_by(Lesson.cefr_level.asc(), Lesson.title.asc()).all()
        if limit:
            lessons = lessons[:limit]

    reading = []
    if 'reading' in targets:
        rq = db.query(ReadingResource).filter(ReadingResource.kind == 'text')
        if level:
            rq = rq.filter(ReadingResource.level == level.upper())
        reading = rq.order_by(ReadingResource.level.asc().nullslast(), ReadingResource.title.asc()).all()
        if limit:
            reading = reading[:limit]

    print(f'Targets: {targets} · Languages: {langs} · Lessons: {len(lessons)} · '
          f'Reading: {len(reading)} · model: {settings.ai_model} · force={force}')
    if not langs or (not lessons and not reading):
        print('Nothing to do.')
        db.close()
        return 0

    if force:
        if lessons:
            ids = [l.id for l in lessons]
            db.query(LessonTranslation).filter(
                LessonTranslation.lesson_id.in_(ids), LessonTranslation.language.in_(langs)
            ).delete(synchronize_session=False)
        if reading:
            rids = [r.id for r in reading]
            db.query(ReadingTranslation).filter(
                ReadingTranslation.resource_id.in_(rids), ReadingTranslation.language.in_(langs)
            ).delete(synchronize_session=False)
        db.commit()
        print('--force: cleared cached translations in scope.')

    stats = {'translated': 0, 'skipped': 0, 'failed': 0, 'attempted': 0}
    tok_in = tok_out = 0
    cost = 0.0
    started = time.time()

    async def warm(label, fn, tokens_matter=True):
        nonlocal tok_in, tok_out, cost
        stats['attempted'] += 1
        gw.last_usage = {'input_tokens': 0, 'output_tokens': 0}
        try:
            await fn()
        except Exception as exc:
            stats['failed'] += 1
            print(f'  ✗ {label}: {exc}')
            return
        used_in = int(gw.last_usage.get('input_tokens', 0))
        used_out = int(gw.last_usage.get('output_tokens', 0))
        if used_in or used_out:
            stats['translated'] += 1
            tok_in += used_in
            tok_out += used_out
            cost += estimate_chat_cost(settings.ai_model, used_in, used_out)
            print(f'  ✓ {label}  (+{used_in}/{used_out} tok)')
            if sleep:
                time.sleep(sleep)
        else:
            stats['skipped'] += 1

    for i, lesson in enumerate(lessons, 1):
        src = _norm(lesson.native_language or 'ru')
        for lang in langs:
            if not needs_translation(lang, src):
                continue
            if 'theory' in targets:
                await warm(f'[{i}/{len(lessons)}] theory · {lesson.title} [{lang}]',
                           lambda l=lesson, x=lang: get_theory(db, l, x, gateway=gw))
            if 'exercises' in targets:
                await warm(f'[{i}/{len(lessons)}] exercises · {lesson.title} [{lang}]',
                           lambda l=lesson, x=lang: get_exercises(db, l, x, gateway=gw))

    for i, res in enumerate(reading, 1):
        for lang in langs:
            if not needs_translation(lang, 'es'):
                continue
            await warm(f'[{i}/{len(reading)}] reading · {res.title} [{lang}]',
                       lambda r=res, x=lang: get_reading_translation(db, r, x, gateway=gw))

    db.close()
    elapsed = time.time() - started
    print('—' * 60)
    print(f"Translated: {stats['translated']} · Skipped (cached/stub): {stats['skipped']} · "
          f"Failed: {stats['failed']} · Attempted: {stats['attempted']}")
    print(f'Tokens in/out: {tok_in}/{tok_out} · Est. cost: ${cost:.4f} · {elapsed:.1f}s')
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description='Pre-warm content translations into the cache.')
    ap.add_argument('--langs', default=','.join(DEFAULT_LANGS), help='target languages (default: uk,ar,fr,en)')
    ap.add_argument('--targets', default=','.join(ALL_TARGETS), help='theory,exercises,reading (default: all)')
    ap.add_argument('--level', default=None, help='only this CEFR level (A1..C2)')
    ap.add_argument('--limit', type=int, default=None, help='cap lessons/texts (after level filter)')
    ap.add_argument('--force', action='store_true', help='ignore cache and re-translate in scope')
    ap.add_argument('--sleep', type=float, default=0.0, help='seconds to sleep between real API calls')
    args = ap.parse_args()

    langs = _parse_csv(args.langs)
    if not langs:
        raise SystemExit(f'No valid languages in --langs (supported: {sorted(SUPPORTED)}).')
    targets = _parse_csv(args.targets, allowed=set(ALL_TARGETS))
    if not targets:
        raise SystemExit(f'No valid targets in --targets (allowed: {ALL_TARGETS}).')
    raise SystemExit(asyncio.run(run(langs, targets, args.level, args.limit, args.force, args.sleep)))


if __name__ == '__main__':
    main()
