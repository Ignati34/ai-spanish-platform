from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.api.deps import get_current_user
from app.content.tense_guide import tense_info
from app.db.session import get_db
from app.models.user import User
from app.schemas.analyzer import TextAnalyzeRequest, TextAnalyzeResponse
from app.services.usage_guard import check_ai_quota, record_ai_usage

router = APIRouter(prefix='/analyze', tags=['text-analyzer'])


def _as_word_objs(items) -> list[dict]:
    """Normalize a part-of-speech list to [{word, translation}], accepting either
    plain strings (older/model variation) or objects."""
    out = []
    for it in items or []:
        if isinstance(it, dict):
            word = (it.get('word') or it.get('es') or '').strip()
            if word:
                out.append({'word': word, 'translation': (it.get('translation') or it.get('ru') or '').strip()})
        elif isinstance(it, str) and it.strip():
            out.append({'word': it.strip(), 'translation': ''})
    return out


@router.post('/text', response_model=TextAnalyzeResponse)
async def analyze_text(payload: TextAnalyzeRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    check_ai_quota(db, current_user)
    orchestrator = AgentOrchestrator()
    result = await orchestrator.analyze_text(text=payload.text, native_language=payload.native_language)
    record_ai_usage(db, current_user, orchestrator.ai.last_usage, agent_name='analyze')

    # Normalize parts of speech so the UI can always render "word → translation".
    verbs = []
    for v in result.get('verbs') or []:
        if isinstance(v, dict):
            verbs.append({'word': (v.get('word') or '').strip(), 'tense': v.get('tense') or '', 'translation': (v.get('translation') or '').strip()})
        elif isinstance(v, str) and v.strip():
            verbs.append({'word': v.strip(), 'tense': '', 'translation': ''})
    result['verbs'] = verbs
    for key in ('nouns', 'adjectives', 'adverbs'):
        result[key] = _as_word_objs(result.get(key))

    tenses = [t for t in (result.get('tenses') or []) if isinstance(t, str)]
    result['tenses'] = tenses
    result['tense_info'] = tense_info(tenses, payload.native_language)
    result.setdefault('translation', '')
    return TextAnalyzeResponse(**result)
