# Upload Studio (file/text → lesson)

The product's core loop: a learner brings material and gets a personalized lesson.

## Flow
```
paste text OR upload file
  → extract plain text        (services/extraction_service.py)
  → AI gateway: analyze + flashcards + exercises   (live, native-language)
  → persist Lesson + FlashcardDeck/Flashcards + TextAnalysis  (services/lesson_builder.py)
  → return the assembled lesson
```

## Endpoints (auth + quota metered)
- `POST /api/uploads/text` — `{text, native_language, cefr_level, title?}` → generated lesson.
- `POST /api/uploads/file` — multipart `file` + `native_language` + `cefr_level` → generated lesson.
- `GET  /api/uploads` — list the user's uploaded files and their processing status.

## Supported inputs now
- **Text/docs**: TXT / MD / CSV / HTML, **PDF** (text layer, via `pypdf`), **DOCX** (via `python-docx`).
- **Audio**: MP3 / WAV / M4A / OGG → **STT transcript → lesson** (same builder). The transcript is
  persisted (`transcripts` table) and returned alongside the lesson.
- **Video**: still `415` for now (extract audio first); wiring ffmpeg is a small follow-up.

## Storage
`services/storage_service.py` writes to **local disk** (`UPLOAD_DIR`) by default and to
**S3/MinIO** when configured (boto3). For persistence in Docker, mount a volume at `UPLOAD_DIR`.

## Cost control
`MAX_LESSON_INPUT_CHARS` caps the text sent to the model; each build = 3 AI calls, metered
into `UsageCounter` and checked against the plan's monthly quota before running.
