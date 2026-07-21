"""Reading library: graded built-in texts (readable inline / downloadable) and curated
online resource links, filterable by level and kind."""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.course import ReadingResource
from app.models.user import User

router = APIRouter(prefix='/reading', tags=['reading'])

_LEVELS = ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']


def _row(r: ReadingResource, with_body: bool = False) -> dict:
    d = {
        'id': str(r.id), 'kind': r.kind, 'level': r.level, 'title': r.title,
        'description': r.description, 'url': r.url, 'category': r.category,
        'language': r.language, 'downloadable': r.downloadable,
    }
    if with_body:
        d['body'] = r.body
    else:
        d['excerpt'] = (r.body[:160] + '…') if (r.kind == 'text' and r.body and len(r.body) > 160) else (r.body or None)
    return d


@router.get('')
def list_reading(kind: str | None = None, level: str | None = None,
                 current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    q = db.query(ReadingResource)
    if kind in ('text', 'link'):
        q = q.filter(ReadingResource.kind == kind)
    if level:
        q = q.filter(ReadingResource.level == level.upper())
    rows = q.order_by(ReadingResource.kind.asc(), ReadingResource.level.asc().nullslast(), ReadingResource.title.asc()).all()
    return {'levels': _LEVELS, 'resources': [_row(r) for r in rows]}


@router.get('/{resource_id}')
async def get_reading(resource_id: str, lang: str | None = None,
                      current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    r = db.get(ReadingResource, resource_id)
    if not r:
        raise HTTPException(status_code=404, detail='Resource not found')
    data = _row(r, with_body=True)
    # The text itself stays in Spanish (that's the reading practice); when a native
    # language is requested we attach a cached translation the reader can toggle on.
    if lang and r.kind == 'text':
        from app.services.translation_service import get_reading_translation, needs_translation
        if needs_translation(lang, 'es'):
            tr = await get_reading_translation(db, r, lang)
            data['title_translation'] = tr.get('title')
            data['body_translation'] = tr.get('body')
            data['translation_language'] = (lang or '')[:2].lower()
    return data
