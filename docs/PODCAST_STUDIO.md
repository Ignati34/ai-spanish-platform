# Podcast Studio (audio → timed segments → lesson)

Where Upload Studio collapses audio into one lesson, Podcast Studio keeps the timeline:
long audio is transcribed, split into timed segments you can navigate, and turned into a
lesson. Reuses the STT wired earlier and the `lesson_builder`.

## Flow
```
upload audio
  → STT (reused): transcript + word/segment timings + duration
  → segment: merge STT timings into ~25s chunks (mm:ss titles);
             no timings (stub / provider w/o timestamps) → group by sentences
  → persist Podcast + PodcastSegment rows
  → build one lesson from the full transcript (analyze + flashcards + exercises)
```

## Endpoints (auth + metered: transcription minutes + AI)
- `POST /api/podcasts` — multipart `file` (+ `native_language`, `cefr_level`, `title`) → segments + lesson.
- `GET  /api/podcasts` — list the user's podcasts.
- `GET  /api/podcasts/{id}` — segments (title, start/end, text).

## UI
The Podcast Studio screen shows the timed segment list plus the generated lesson (summary,
flashcards, exercises). Without a key (`AI_PROVIDER=stub`) it still works: a demo transcript
is segmented by sentences so the screen is fully demoable.

## Next
- Per-segment study (translation + vocab + a mini-quiz per segment — the `PodcastSegment`
  model already has `translation_json` / `vocabulary_json` / `quiz_json` fields for this).
- Clip playback per segment using the stored audio and segment start/end.
- Import from a URL (YouTube/RSS) once you add a fetch+extract step (mind content rights).
