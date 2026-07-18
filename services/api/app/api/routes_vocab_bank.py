"""Personal vocabulary knowledge base: browse/search the learner's imported word bank."""
from fastapi import APIRouter, Depends, Query

from app.api.deps import get_current_user
from app.content.vocab_bank import counts, sample, search

router = APIRouter(prefix='/vocab-bank', tags=['vocab-bank'])


@router.get('/stats')
def bank_stats(user=Depends(get_current_user)):
    return {'counts': counts()}


@router.get('/search')
def bank_search(q: str = Query('', max_length=100), kind: str | None = None,
                limit: int = Query(50, le=200), user=Depends(get_current_user)):
    return {'items': search(q, kind, limit)}


@router.get('/sample')
def bank_sample(kind: str = 'phrases', n: int = Query(10, le=50), user=Depends(get_current_user)):
    return {'items': sample(kind, n)}
