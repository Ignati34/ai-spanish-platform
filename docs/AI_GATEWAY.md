# AI gateway

Single entry point (`app/services/ai_gateway.py`) that the orchestrator/agents call.
Provider-agnostic, so you swap models without touching routes.

## Providers
- **stub** (default) — deterministic, offline, no key. Keeps the whole app runnable.
- **openai** — OpenAI-compatible chat completions via `AI_BASE_URL` (OpenAI or any
  compatible endpoint). JSON-object responses, parsed into the existing Pydantic schemas.

Select with `AI_PROVIDER`; the factory (`services/ai/factory.py`) picks the implementation
and falls back to the stub if the real one can't be constructed.

## What it does
- **Prompts** are built per task and localized to the learner's native language
  (`services/ai/prompts.py`), so grammar/translations come back in RU/UK/AR/FR/ES/EN.
- **Cache** — identical requests are cached (Redis if reachable, else in-process),
  keyed by task+text+language+model. TTL via `AI_CACHE_TTL_SECONDS`.
- **Usage metering** — each provider reports `last_usage` (prompt/completion tokens).
  Routes call `usage_guard.check_ai_quota` before and `record_ai_usage` after, updating
  `UsageCounter` and enforcing `UserEntitlement.max_ai_requests_month` (402 when exceeded).
- **Graceful fallback** — if the real provider errors (network/parse), the gateway logs a
  warning and returns a valid stub result instead of failing the request.

## Covered tasks (wired end-to-end)
`analyze_text`, `generate_flashcards`, `generate_exercises`, `check_answer`
→ endpoints `/api/analyze/text`, `/api/flashcards/generate`, `/api/exercises/generate`,
`/api/exercises/{id}/submit` (all now require auth + meter usage).

## Speech-to-text (wired)
`transcribe_audio` uses the provider's `/audio/transcriptions` (model = `STT_MODEL`), with the
same graceful fallback to a stub transcript. Used by `POST /api/uploads/file` (audio) and
`POST /api/voice/transcribe`. Metered into `UsageCounter.transcription_seconds_used` against
the plan's monthly minutes.

## Text-to-speech + conversation (wired)
`synthesize_speech` (model = `TTS_MODEL`, `TTS_VOICE`) and `voice_reply` power the Voice Tutor
(`/api/voice/*`), with the same fallback. TTS metered into `UsageCounter.tts_seconds_used`.

## Not yet wired (next)
Image generation / embeddings (RAG) still route through their stubs — add them here using the
same provider pattern.
