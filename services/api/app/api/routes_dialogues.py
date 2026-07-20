"""Reading dialogues: graded built-in dialogues (A1→C2) plus a custom generator.

The generator produces a short, level-appropriate two-speaker dialogue on any topic,
capped at ~500 characters of Spanish so it stays a quick read.
"""
from __future__ import annotations

from fastapi import APIRouter, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.content import dialogues as dlg
from app.db.session import get_db
from app.models.user import User
from app.services.usage_guard import check_ai_quota, record_ai_usage

router = APIRouter(prefix='/dialogues', tags=['dialogues'])

MAX_TOPIC = 500
MAX_ES_CHARS = 500


class DialogueGenerateRequest(BaseModel):
    topic: str = Field(min_length=1, max_length=MAX_TOPIC)
    cefr_level: str = 'A1'
    native_language: str = 'ru'


def _cap_lines(lines: list[dict]) -> list[dict]:
    """Keep the dialogue within the Spanish character budget (drop trailing lines)."""
    out, total = [], 0
    for ln in lines or []:
        es = (ln.get('es') or '').strip()
        if not es:
            continue
        total += len(es)
        out.append({'speaker': (ln.get('speaker') or '').strip() or '—', 'es': es,
                    'translation': (ln.get('translation') or '').strip()})
        if total >= MAX_ES_CHARS and len(out) >= 4:
            break
    return out


@router.get('')
def list_dialogues(level: str | None = None, native_language: str = 'ru',
                   current_user: User = Depends(get_current_user)):
    lang = native_language or current_user.native_language or 'ru'
    return {'dialogues': dlg.public_list(level, lang), 'levels': ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']}


@router.post('/generate')
async def generate_dialogue(payload: DialogueGenerateRequest,
                            current_user: User = Depends(get_current_user),
                            db: Session = Depends(get_db)):
    check_ai_quota(db, current_user)
    topic = payload.topic.strip()[:MAX_TOPIC]
    native = payload.native_language or current_user.native_language or 'ru'

    orch = AgentOrchestrator()
    result = await orch.generate_dialogue(topic=topic, cefr_level=payload.cefr_level, native_language=native)
    record_ai_usage(db, current_user, orch.ai.last_usage, agent_name='dialogue')

    lines = _cap_lines(result.get('lines') or [])
    return {
        'title': (result.get('title') or topic)[:120],
        'level': payload.cefr_level,
        'topic': topic,
        'lines': lines,
        'stub': bool(result.get('stub')),
    }
