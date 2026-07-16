# Project overview

Web app **+ Telegram Mini App** for learning Spanish **A1–C2**, with the interface and
explanations in the learner's **native language** (RU / UK / AR-RTL / FR, plus ES/EN). AI turns
any material the learner brings into a personalized lesson and guides them from an onboarding
diagnostic through to scheduled long-term review.

## The core idea: a closed learning loop
The build is not a pile of features — it's a connected cycle where each part feeds the next:

```
diagnostic sets the level
      → lessons / dialogues / simulations produce mistakes
            → weak spots are aggregated
                  → targeted practice + flashcards enter spaced repetition
                        → motivation reminds the learner to come back when reviews are due
```

## What's built

### AI core
Provider-agnostic **AI gateway** (stub + OpenAI-compatible) with response cache, token
metering, and graceful fallback to the stub. Ten tasks run through it: text analysis,
flashcards, exercises, answer checking, **STT**, **TTS**, conversational reply, level
assessment, targeted (weak-spot) exercises, and role-play mission turns.

### Working with material
- **Upload Studio** — text / PDF / DOCX / HTML / audio → a full lesson.
- **Podcast Studio** — long audio → STT → timed, navigable segments → a lesson.

### Speaking
- **STT** for spoken input.
- **Voice Tutor** — spoken/typed Spanish dialogue → reply + native-language correction +
  score, voiced with TTS.
- **Role-play simulations** — mini-missions (clinic, bank, interview, rental, town hall) with a
  role, a goal, hints, and goal-achievement judgement.

### Personalization
- **Onboarding diagnostic** — MC + writing/speaking sample → CEFR placement written to the
  profile.
- **"My mistakes" & progress** — mistakes auto-collected from diagnostic, voice, exercises and
  simulations → aggregated weak spots + study plan → one-tap AI targeted practice.
- **Spaced repetition (SM-2)** — generated flashcards enter a scheduled review queue.
- **Motivation** — daily goals, streaks, and Telegram reminders tied to due reviews.

### Product infrastructure
- **Multi-provider payments** (Stripe incl. Bizum/SEPA, PayPal, Telegram Payments) with
  per-country method hints.
- **Telegram Mini App** — signed-initData auth; the same web build runs inside Telegram.
- **Multilingual UI** — 6 locales, Arabic RTL; per-native-language grammar explanations.
- **Admin + billing** dashboards.

### Deployment
Docker in two modes — hosted **web service** and desktop **self-hosted** (everything in
containers); nginx, Postgres/Redis/MinIO, worker + scheduler, Makefile, `.env` examples.

## By the numbers
~15 frontend screens (6 locales), ~20 backend services/routes, 10 AI gateway tasks, docs per
feature under `docs/`. Content is original / license-clean (no copyrighted textbook).

## Verified vs. not
**Verified:** the whole backend passes byte-compile; key algorithms have smoke tests (gateway
tasks on the stub + fallback, text extraction, podcast segmentation, SM-2 math, streak logic,
diagnostic scoring, simulation goal progression); the frontend builds with zero type errors.

**Now also verified:** the full app imports and all mappers configure (41 tables, 61 routes); an
end-to-end **test suite** runs the real app on SQLite + stub AI and passes (auth, diagnostic,
upload→lesson, SRS, motivation, simulation, billing); the initial **Alembic migration** applies
and rolls back cleanly. Two real bugs were fixed in the process (a bcrypt/passlib version clash,
and a naive/aware datetime comparison in SRS).

**Still not verified live:** a run against a real **Postgres** and with real **AI/payment keys**;
Docker images were not built here. Steps are in `docs/RUNBOOK.md`.

## Honest limitations
- Without a key, everything runs on **deterministic stubs** — great for demos, but real
  analysis / transcription / speech / assessment need a real provider.
- **Pronunciation scoring is text-based** (from the transcript, not phoneme-level).
- **"Goal achieved"** in simulations is the model's judgement, not a hard check (the stub
  completes after a few turns so the flow is demoable).
- Schema is now managed by **Alembic** (initial migration in `services/api/migrations/`); use
  `alembic upgrade head`. `create_all` remains only for throwaway dev DBs.
- Some routes remain stubs (image generation, licensing, per-segment podcast study); **video**
  isn't supported yet (needs ffmpeg); the **Vinogradov textbook is intentionally not included**
  — only original content plus a place for a licensed import.

## What's left from the plan
- One big vertical: **teacher / school mode** (B2B — groups, assignments, reports).
- Remaining hardening: a live Postgres + real-key run, a Stripe test-mode payment, broader test
  coverage, and filling the remaining stubs (images, licensing, per-segment podcast study, video).

## Where to read more
Feature docs live in `docs/` — payments, Telegram Mini App, i18n, deployment, content
licensing, AI gateway, Upload Studio, Voice Tutor, diagnostic, personalization, spaced
repetition, motivation, Podcast Studio, simulations.
