"""Extract plain text from uploaded material.

Supported now: txt, md, csv, html(ish), pdf (text layer), docx.
Audio/video/image go through STT/vision later (Voice/Upload phase 2) — for those we
raise a clear NotImplemented so the API can respond 415 instead of guessing.
"""
from __future__ import annotations

import io
import re

TEXT_EXT = {'txt', 'md', 'markdown', 'csv', 'text'}
AUDIO_EXT = {'mp3', 'wav', 'ogg', 'oga', 'm4a', 'webm'}
VIDEO_EXT = {'mp4', 'mov', 'mkv', 'avi'}


class ExtractionError(Exception):
    pass


class UnsupportedType(ExtractionError):
    pass


def ext_of(filename: str) -> str:
    return (filename.rsplit('.', 1)[-1].lower() if '.' in filename else '').strip()


def is_audio(filename: str, mime_type: str | None = None) -> bool:
    return ext_of(filename) in AUDIO_EXT or (mime_type or '').startswith('audio/')


def is_video(filename: str, mime_type: str | None = None) -> bool:
    return ext_of(filename) in VIDEO_EXT or (mime_type or '').startswith('video/')


def extract_text(filename: str, data: bytes, mime_type: str | None = None) -> tuple[str, dict]:
    """Return (clean_text, metadata). Raises UnsupportedType for non-text media."""
    ext = ext_of(filename)
    meta: dict = {'ext': ext, 'bytes': len(data)}

    if ext in AUDIO_EXT or (mime_type or '').startswith('audio/'):
        raise UnsupportedType('audio requires transcription (STT) — coming in the Voice phase')
    if ext in VIDEO_EXT or (mime_type or '').startswith('video/'):
        raise UnsupportedType('video requires transcription (STT) — coming in the Voice phase')

    if ext in TEXT_EXT or (mime_type or '').startswith('text/') or ext == '':
        text = data.decode('utf-8', errors='replace')
    elif ext == 'pdf' or (mime_type == 'application/pdf'):
        text, pages = _extract_pdf(data)
        meta['pages'] = pages
    elif ext in {'docx'} or (mime_type or '').endswith('wordprocessingml.document'):
        text = _extract_docx(data)
    elif ext in {'html', 'htm'}:
        text = _strip_html(data.decode('utf-8', errors='replace'))
    else:
        raise UnsupportedType(f'unsupported file type: .{ext}')

    text = _normalize(text)
    if not text.strip():
        raise ExtractionError('no extractable text found')
    meta['chars'] = len(text)
    return text, meta


def _extract_pdf(data: bytes) -> tuple[str, int]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover
        raise ExtractionError('pypdf not installed') from exc
    reader = PdfReader(io.BytesIO(data))
    parts = []
    for page in reader.pages:
        try:
            parts.append(page.extract_text() or '')
        except Exception:
            parts.append('')
    return '\n'.join(parts), len(reader.pages)


def _extract_docx(data: bytes) -> str:
    try:
        import docx  # python-docx
    except Exception as exc:  # pragma: no cover
        raise ExtractionError('python-docx not installed') from exc
    document = docx.Document(io.BytesIO(data))
    return '\n'.join(p.text for p in document.paragraphs)


def _strip_html(html: str) -> str:
    html = re.sub(r'<(script|style)[^>]*>.*?</\1>', ' ', html, flags=re.S | re.I)
    return re.sub(r'<[^>]+>', ' ', html)


def _normalize(text: str) -> str:
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()
