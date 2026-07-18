"""Podcast Studio: audio -> timed segments -> lesson."""
from __future__ import annotations

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.core.config import get_settings
from app.db.session import get_db
from app.services.security.upload_guard import scan_upload_or_raise
from app.models.podcast import Podcast, PodcastSegment
from app.models.user import User
from app.services.extraction_service import is_audio
from app.services.podcast_service import build_podcast_from_audio
from app.services.usage_guard import (
    check_ai_quota, check_transcription_quota, record_ai_usage,
    record_transcription_usage, record_tts_usage,
)

settings = get_settings()
router = APIRouter(prefix='/podcasts', tags=['podcasts'])


@router.get('/status')
def status_():
    return {'module': 'podcasts', 'status': 'ready'}


@router.post('')
async def create_podcast(
    file: UploadFile = File(...),
    native_language: str = Form('ru'),
    cefr_level: str = Form('A1'),
    title: str | None = Form(default=None),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if not is_audio(file.filename or '', file.content_type):
        raise HTTPException(status_code=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE, detail='Expected an audio file')
    check_transcription_quota(db, current_user)
    check_ai_quota(db, current_user)

    data = await file.read()
    scan_upload_or_raise(data, file.filename or 'audio')
    max_bytes = settings.max_upload_mb * 1024 * 1024
    if len(data) > max_bytes:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail=f'File exceeds {settings.max_upload_mb} MB')

    result = await build_podcast_from_audio(
        db, current_user, file.filename or 'podcast.mp3', data,
        native_language=native_language, cefr_level=cefr_level, title=title,
    )
    record_transcription_usage(db, current_user, result.get('transcription_seconds'))
    record_ai_usage(db, current_user, result.get('usage'), requests=(result.get('usage') or {}).get('ai_calls', 1))
    db.commit()
    result.pop('usage', None)
    result.pop('transcription_seconds', None)
    return result


@router.get('')
def list_podcasts(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    rows = (db.query(Podcast).filter(Podcast.user_id == current_user.id)
            .order_by(Podcast.created_at.desc()).limit(50).all())
    return [{'id': str(p.id), 'title': p.title, 'cefr_level': p.cefr_level, 'status': p.status, 'created_at': p.created_at} for p in rows]


@router.get('/{podcast_id}')
def get_podcast(podcast_id: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    p = db.get(Podcast, podcast_id)
    if not p or p.user_id != current_user.id:
        raise HTTPException(status_code=404, detail='Podcast not found')
    segs = (db.query(PodcastSegment).filter(PodcastSegment.podcast_id == p.id)
            .order_by(PodcastSegment.start_time.asc(), PodcastSegment.created_at.asc()).all())
    return {
        'id': str(p.id), 'title': p.title, 'cefr_level': p.cefr_level, 'status': p.status,
        'segments': [{'title': s.title, 'start': s.start_time, 'end': s.end_time, 'text': s.transcript} for s in segs],
    }
