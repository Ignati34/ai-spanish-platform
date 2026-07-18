"""Batch-generate curriculum lessons from the syllabus (needs a real AI key).

Usage (inside the api container):
    python scripts/generate_curriculum.py --limit 20 --native ru
    python scripts/generate_curriculum.py --level B1 --limit 10
Runs idempotently: already-generated lessons are skipped, so you can grow the course
in cost-controlled batches toward the full 150.
"""
import argparse
import asyncio

from app.content.syllabus import SYLLABUS
from app.db.session import SessionLocal
from app.services.lesson_generator import existing_numbers, generate_and_store


async def main(limit: int, native: str, level: str | None) -> None:
    db = SessionLocal()
    try:
        done = existing_numbers(db)
        todo = [e for e in SYLLABUS if e['n'] not in done and (not level or e['level'] == level)][:limit]
        print(f'Syllabus: {len(SYLLABUS)} topics | already generated: {len(done)} | generating now: {len(todo)}')
        for e in todo:
            try:
                await generate_and_store(db, e, native)
                print(f"  ✓ [{e['n']:03d}] {e['level']} — {e['es']}")
            except Exception as ex:
                print(f"  ✗ [{e['n']:03d}] failed: {ex}")
        print('Done.')
    finally:
        db.close()


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--limit', type=int, default=10)
    ap.add_argument('--native', default='ru')
    ap.add_argument('--level', default='')
    a = ap.parse_args()
    asyncio.run(main(a.limit, a.native, a.level or None))
