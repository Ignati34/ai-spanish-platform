"""Generate full curriculum lessons (theory + exercises) from the syllabus via the AI
gateway, and store them as course lessons. Idempotent by syllabus number."""
from __future__ import annotations

from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.models.course import Lesson


def _title(entry: dict) -> str:
    return f"{entry['n']:03d}. {entry['ru']}"


def existing_numbers(db: Session) -> set[int]:
    nums: set[int] = set()
    for l in db.query(Lesson).filter(Lesson.lesson_type == 'curriculum').all():
        n = (l.content_json or {}).get('syllabus_n')
        if isinstance(n, int):
            nums.add(n)
    return nums


async def generate_and_store(db: Session, entry: dict, native_language: str = 'ru') -> dict:
    orch = AgentOrchestrator()
    data = await orch.generate_lesson(entry['es'], entry['ru'], entry['level'], native_language, entry.get('focus', ''))
    lesson = Lesson(
        module_id=None, title=_title(entry), description=(data.get('theory') or entry['ru'])[:400],
        cefr_level=entry['level'], native_language=native_language, lesson_type='curriculum',
        content_json={'theory': data.get('theory', ''), 'exercises': data.get('exercises', []), 'syllabus_n': entry['n']},
    )
    db.add(lesson)
    db.commit()
    return orch.ai.last_usage
