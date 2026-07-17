"""Media helpers: extract an audio track from a video file using ffmpeg.

ffmpeg is installed in the API/worker images. Used to turn uploaded video (mp4, ...)
into audio for STT before building flashcards/lessons.
"""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path


class MediaError(Exception):
    pass


def extract_audio_from_video(data: bytes, filename: str = 'video.mp4') -> bytes:
    """Return mp3 audio bytes extracted from a video. Raises MediaError on failure."""
    suffix = Path(filename).suffix or '.mp4'
    with tempfile.TemporaryDirectory() as tmp:
        src = Path(tmp) / f'in{suffix}'
        out = Path(tmp) / 'out.mp3'
        src.write_bytes(data)
        try:
            subprocess.run(
                ['ffmpeg', '-y', '-i', str(src), '-vn', '-acodec', 'libmp3lame', '-q:a', '4', str(out)],
                check=True, capture_output=True, timeout=300,
            )
        except FileNotFoundError as exc:
            raise MediaError('ffmpeg not available') from exc
        except subprocess.CalledProcessError as exc:
            raise MediaError(f'ffmpeg failed: {exc.stderr.decode()[:300]}') from exc
        except subprocess.TimeoutExpired as exc:
            raise MediaError('ffmpeg timed out') from exc
        if not out.exists() or out.stat().st_size == 0:
            raise MediaError('no audio track extracted')
        return out.read_bytes()
