# Onboarding diagnostic

Places a new learner on the A1–C2 map and surfaces their first gaps, so the rest of the
product can personalize. This is the "who just arrived?" step that ties the vertical
features (Upload Studio, analyzer, flashcards, voice) into a single learning path.

## Flow
```
GET  /api/diagnostic/questions?native_language=ru
  → 8 original multiple-choice items (A1→B2, answer key kept server-side)
  + a writing prompt and a speaking prompt (localized)

learner answers MC + writes a few sentences (+ optional mic → STT transcript)

POST /api/diagnostic/submit
  → deterministic MC scoring (content/diagnostic.py)
  → AI gateway assess_level(writing, speaking, mc_summary, native_language)
  → persist DiagnosticResult + set UserProfile.current_cefr_level = recommended_level
  → return {cefr_estimate, recommended_level, strengths, gaps, summary, study_plan}
```

## Why it reuses everything
- MC scoring is deterministic (no model needed, no cost).
- The free-production assessment is one `assess_level` call through the same gateway
  (native-language output, graceful stub fallback, usage metered).
- The optional speaking sample reuses the STT wired for the Voice Tutor (`/voice/transcribe`).

## Result is the unlock
`UserProfile.current_cefr_level` stops being a hardcoded "A1" and reflects a real placement.
`GET /api/users/me` now returns it, and the Dashboard shows it. This is the hook the next
layer (progress tracking, "my mistakes", personalized plan, lesson recommendations) builds on.

## Content & copyright
All diagnostic items and prompts are original (see `content/diagnostic.py`) — no copyrighted
test material. Extend or randomize the item bank freely.
