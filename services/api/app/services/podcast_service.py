"""Podcast Studio: long audio -> timed segments -> a lesson.

Unlike Upload Studio (audio collapses into one lesson), here the value is segmentation:
the transcript is split into timed chunks you can navigate and study piece by piece.
Reuses the STT wired earlier and the lesson_builder for the overall lesson.
"""
from __future__ import annotations

import re

from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.models.podcast import Podcast, PodcastSegment
from app.models.upload import UploadedFile
from app.models.user import User
from app.services.extraction_service import ext_of
from app.services.lesson_builder import build_lesson_from_text
from app.services.storage_service import storage_service

# chunking targets when merging STT segments
_MAX_CHUNK_SECONDS = 25.0
_MAX_CHUNK_CHARS = 240


def _fmt(t: float) -> str:
    t = int(t or 0)
    return f'{t // 60:02d}:{t % 60:02d}'


def segment_transcript(text: str, stt_segments: list[dict] | None) -> list[dict]:
    """Return coarse study segments [{start, end, text, title}].

    Uses real STT timings when available (merged into ~25s chunks); otherwise falls
    back to sentence grouping with zero timings (stub / providers without timestamps).
    """
    if stt_segments:
        chunks: list[dict] = []
        cur = None
        for seg in stt_segments:
            s = float(seg.get('start', 0) or 0)
            e = float(seg.get('end', 0) or 0)
            txt = (seg.get('text') or '').strip()
            if not txt:
                continue
            if cur is None:
                cur = {'start': s, 'end': e, 'text': txt}
            else:
                cur['end'] = e
                cur['text'] = (cur['text'] + ' ' + txt).strip()
            if (cur['end'] - cur['start']) >= _MAX_CHUNK_SECONDS or len(cur['text']) >= _MAX_CHUNK_CHARS:
                chunks.append(cur); cur = None
        if cur:
            chunks.append(cur)
        for c in chunks:
            c['title'] = _fmt(c['start'])
        return chunks

    # Fallback: split into sentences, group in pairs.
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', text) if s.strip()]
    chunks = []
    for i in range(0, len(sentences), 2):
        piece = ' '.join(sentences[i:i + 2])
        chunks.append({'start': 0.0, 'end': 0.0, 'text': piece, 'title': f'#{i // 2 + 1}'})
    return chunks or [{'start': 0.0, 'end': 0.0, 'text': text, 'title': '#1'}]


async def build_podcast_from_audio(db: Session, user: User, filename: str, data: bytes,
                                   native_language: str = 'ru', cefr_level: str = 'A1',
                                   title: str | None = None) -> dict:
    # 1) store raw audio
    storage_url = storage_service.save(user.id, filename, data, 'audio/mpeg')
    uploaded = UploadedFile(
        user_id=user.id, original_filename=filename, file_type=ext_of(filename),
        mime_type='audio/mpeg', storage_url=storage_url, file_size=len(data), processing_status='uploaded',
    )
    db.add(uploaded)
    db.flush()

    # 2) transcribe (reuse STT) -> text + timings
    orch = AgentOrchestrator()
    stt = await orch.transcribe(data=data, filename=filename, language='es')
    transcript = (stt.get('text') or '').strip()
    duration = float(stt.get('duration_seconds') or 0.0)
    transcription_seconds = duration
    stt_segments = stt.get('segments') or []

    # 3) segment
    segments = segment_transcript(transcript, stt_segments)

    podcast = Podcast(
        user_id=user.id, source_file_id=uploaded.id, title=(title or filename or 'Podcast'),
        description=transcript[:400], cefr_level=cefr_level, status='segmented',
    )
    db.add(podcast)
    db.flush()
    for seg in segments:
        db.add(PodcastSegment(
            podcast_id=podcast.id, title=seg['title'], start_time=seg['start'], end_time=seg['end'],
            transcript=seg['text'],
        ))

    # 4) one lesson from the whole transcript (reuse lesson_builder)
    lesson = await build_lesson_from_text(
        db, user, text=transcript, native_language=native_language, cefr_level=cefr_level,
        source_type='podcast', source_id=podcast.id, title=(title or filename),
    )
    podcast.status = 'lesson_ready'
    db.flush()

    return {
        'podcast_id': str(podcast.id),
        'title': podcast.title,
        'duration_seconds': duration,
        'transcript': transcript,
        'segments': [{'title': s['title'], 'start': s['start'], 'end': s['end'], 'text': s['text']} for s in segments],
        'lesson': {
            'lesson_id': lesson.lesson_id, 'cefr_estimate': lesson.analysis.get('cefr_estimate', cefr_level),
            'summary': lesson.analysis.get('summary', ''), 'analysis': lesson.analysis,
            'cards': lesson.cards, 'exercises': lesson.exercises,
        },
        'usage': lesson.usage,
        'transcription_seconds': transcription_seconds,
    }
