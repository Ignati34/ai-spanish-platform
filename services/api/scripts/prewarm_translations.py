#!/usr/bin/env python3
"""Pre-warm lesson-theory translations so learners never wait on first open.

Translates every built-in curriculum lesson's theory into the requested languages via
the AI gateway and caches the result in `lesson_translations`. Idempotent: translations
that are already cached and up to date (source hash unchanged) are skipped, so re-running
is cheap. Interrupt-safe: each translation is committed as it completes.

Run inside the API container (working dir: services/api), with a real provider configured
(AI_PROVIDER=openai, AI_API_KEY=...). Under the stub provider translations are identity and
are NOT cached (the script warns and does nothing useful).

Examples:
  python scripts/prewarm_translations.py                      # uk,ar,fr,en · all lessons
  python scripts/prewarm_translations.py --langs uk,fr        # a subset of languages
  python scripts/prewarm_translations.py --level B1 --limit 5 # a slice, to test cost first
  python scripts/prewarm_translations.py --force              # re-translate (ignore cache)
  python scripts/prewarm_translations.py --sleep 0.3          # gentle throttle between calls
"""
from __future__ import annotations

import argparse
import asyncio
import time

from app.core.config import get_settings
from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.models.course import Lesson, LessonTranslation
from app.services.ai_gateway import AIGateway
from app.services.ai_pricing import estimate_chat_cost
from app.services.translation_service import (
    SUPPORTED, _norm, get_theory, needs_translation,
)

DEFAULT_LANGS = ['uk', 'ar', 'fr', 'en']


def _parse_langs(raw: str) -> list[str]:
    out = []
    for part in (raw or '').split(','):
        code = _norm(part.strip())
        if code and code in SUPPORTED and code not in out:
            out.append(code)
    return out


async def run(langs: list[str], level: str | None, limit: int | None, force: bool, sleep: float) -> int:
    settings = get_settings()
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    gw = AIGateway()

    is_stub = (settings.ai_provider or 'stub').lower() != 'openai' or not settings.ai_api_key
    if is_stub:
        print('WARNING: provider is not OpenAI (or AI_API_KEY is unset). Translations will be '
              'identity and will NOT be cached. Set AI_PROVIDER=openai and AI_API_KEY, then re-run.')

    q = db.query(Lesson).filter(Lesson.lesson_type == 'curriculum')
    if level:
        q = q.filter(Lesson.cefr_level == level.upper())
    lessons = q.order_by(Lesson.cefr_level.asc(), Lesson.title.asc()).all()
    if limit:
        lessons = lessons[:limit]

    print(f'Lessons: {len(lessons)} · Languages: {langs} · model: {settings.ai_model} · force={force}')
    if not lessons or not langs:
        print('Nothing to do.')
        db.close()
        return 0

    if force:
        ids = [l.id for l in lessons]
        deleted = (db.query(LessonTranslation)
                   .filter(LessonTranslation.lesson_id.in_(ids), LessonTranslation.language.in_(langs))
                   .delete(synchronize_session=False))
        db.commit()
        if deleted:
            print(f'--force: cleared {deleted} cached translations in scope.')

    attempted = translated = skipped = failed = 0
    tok_in = tok_out = 0
    cost = 0.0
    started = time.time()

    for i, lesson in enumerate(lessons, 1):
        source_lang = _norm(lesson.native_language or 'ru')
        for lang in langs:
            if not needs_translation(lang, source_lang):
                continue
            attempted += 1
            # Reset so a non-zero usage after the call reliably means a fresh provider hit
            # (DB-cache and gateway-cache hits leave usage at zero).
            gw.last_usage = {'input_tokens': 0, 'output_tokens': 0}
            try:
                await get_theory(db, lesson, lang, gateway=gw)
            except Exception as exc:  # keep going; one bad lesson shouldn't stop the batch
                failed += 1
                print(f'  [{i}/{len(lessons)}] ✗ {lesson.title} [{lang}]: {exc}')
                continue
            used_in = int(gw.last_usage.get('input_tokens', 0))
            used_out = int(gw.last_usage.get('output_tokens', 0))
            if used_in or used_out:
                translated += 1
                tok_in += used_in
                tok_out += used_out
                cost += estimate_chat_cost(settings.ai_model, used_in, used_out)
                print(f'  [{i}/{len(lessons)}] ✓ {lesson.title} [{lang}]  (+{used_in}/{used_out} tok)')
                if sleep:
                    time.sleep(sleep)
            else:
                skipped += 1

    db.close()
    elapsed = time.time() - started
    print('—' * 56)
    print(f'Translated: {translated} · Skipped (cached/stub): {skipped} · Failed: {failed} · Attempted: {attempted}')
    print(f'Tokens in/out: {tok_in}/{tok_out} · Est. cost: ${cost:.4f} · {elapsed:.1f}s')
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description='Pre-warm lesson theory translations into the cache.')
    ap.add_argument('--langs', default=','.join(DEFAULT_LANGS), help='comma-separated target languages (default: uk,ar,fr,en)')
    ap.add_argument('--level', default=None, help='only this CEFR level (A1..C2)')
    ap.add_argument('--limit', type=int, default=None, help='cap number of lessons (after level filter)')
    ap.add_argument('--force', action='store_true', help='ignore cache and re-translate in scope')
    ap.add_argument('--sleep', type=float, default=0.0, help='seconds to sleep between real API calls')
    args = ap.parse_args()

    langs = _parse_langs(args.langs)
    if not langs:
        raise SystemExit(f'No valid languages in --langs (supported: {sorted(SUPPORTED)}).')
    raise SystemExit(asyncio.run(run(langs, args.level, args.limit, args.force, args.sleep)))


if __name__ == '__main__':
    main()
