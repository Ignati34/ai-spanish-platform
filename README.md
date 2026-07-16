# AI Spanish Learning Platform

Web app **+ Telegram Mini App** for learning Spanish **A1 → C2**, with the interface and
grammar explanations in the learner's **native language (RU / UK / AR-RTL / FR**, plus ES/EN).
Core loop: the learner brings any text/audio/video → the system turns it into a lesson with
grammar (in their language), flashcards, exercises, voice practice and progress.

Monorepo: FastAPI backend + Vite/React/TypeScript/Tailwind frontend, deployable **as a hosted
web service** and **as a desktop/self-hosted Docker bundle**.

## Repository layout
```
ai-spanish-platform/
├─ apps/web/                 # React + TS + Tailwind SPA (also runs as Telegram Mini App)
│  └─ src/{pages,components,lib,store,i18n.ts}
├─ services/api/             # FastAPI backend
│  └─ app/{api,agents,services,models,schemas,core,content,workers,db}
│     └─ services/payments/  # provider abstraction: stripe / paypal / telegram / registry
├─ infra/
│  ├─ docker/                # Dockerfile.api, Dockerfile.worker, Dockerfile.web
│  ├─ nginx/web.conf         # serves SPA + proxies /api
│  └─ compose/               # docker-compose.yml (web), docker-compose.selfhosted.yml (desktop)
├─ docs/                     # PAYMENTS, TELEGRAM_MINI_APP, CONTENT_LICENSING, DEPLOYMENT, I18N
├─ .env.example / .env.selfhosted.example
└─ Makefile
```

## Quick start
```bash
make env            # create .env, .env.selfhosted, apps/web/.env
# --- hosted web service ---
make up && make migrate && make seed     # http://localhost:8080  (API on :8000/docs)
# --- desktop / self-hosted (all in Docker, auto migrate+seed) ---
make selfhosted                          # http://localhost:8080
```

## What was built on top of the original scaffold + billing patch
- **Multi-provider payments** (Spain + international): Stripe (card + **Bizum** + SEPA),
  PayPal, Telegram Payments, behind one interface with per-country method hints.
  See `docs/PAYMENTS.md`.
- **Telegram Mini App**: signed-`initData` auth, bot webhook, in-app Telegram Payments.
  See `docs/TELEGRAM_MINI_APP.md`.
- **Role-play simulations**: mini-missions (clinic, bank, interview, rental, town hall) on top
  of the Voice Tutor — a role + a goal + hints + goal-achievement judgement. See `docs/SIMULATIONS.md`.
- **Voice Tutor**: spoken (mic→STT) or typed Spanish dialogue → tutor reply + native-language
  correction + score, voiced with TTS. See `docs/VOICE_TUTOR.md`.
- **Onboarding diagnostic**: MC + writing/speaking sample → CEFR placement, strengths, gaps and
  a study plan; writes `UserProfile.current_cefr_level`. See `docs/DIAGNOSTIC.md`.
- **Personalization ("My mistakes" & progress)**: mistakes auto-collected from the diagnostic,
  voice and exercises → aggregated weak spots + study plan → one-tap AI targeted practice.
  See `docs/PERSONALIZATION.md`.
- **Spaced repetition (SM-2)**: generated flashcards enter a review queue that schedules
  long-term memory (again/hard/good/easy). See `docs/SPACED_REPETITION.md`.
- **Motivation**: daily goals, streaks, and Telegram reminders tied to due reviews (scheduler
  worker). See `docs/MOTIVATION.md`.
- **Native-language UI**: i18next for RU/UK/AR(RTL)/FR/ES/EN; per-language grammar
  explanations in lesson content. See `docs/I18N.md`.
- **Frontend**: SPA shell, routing, auth, Dashboard, Text Analyzer, Flashcards, Course,
  Billing (provider/country-aware), Admin.
- **Podcast Studio**: long audio → STT → timed segments (navigable) → a lesson. Reuses STT +
  lesson builder. See `docs/PODCAST_STUDIO.md`.
- **Upload Studio**: paste text or upload TXT/PDF/DOCX **or audio (MP3/WAV)** → extract or
  **transcribe (STT)** → live AI → a full lesson (analysis + flashcards + exercises), persisted.
  See `docs/UPLOAD_STUDIO.md`.
- **CEFR A1–C2** seed + original demo lessons (no copyrighted textbook — see below).
- **Unified Docker**: hosted web compose + desktop self-hosted compose.

## Course content / Vinogradov — important
The Vinogradov textbook is copyrighted and is **not** bundled. Ship original + user-supplied
+ openly-licensed content, and treat any commercial textbook as a licensed integration to
enable once you hold the rights. See `docs/CONTENT_LICENSING.md`.

## Status
Runnable skeleton with the requested capabilities wired end-to-end. The AI gateway now
supports a **real OpenAI-compatible LLM** for text analysis, flashcards, exercises and
answer-checking — with per-native-language prompts, response caching, token metering
against plan quotas, and automatic fallback to the offline stub (`AI_PROVIDER=stub` needs
no key). See `docs/AI_GATEWAY.md`. STT/TTS/image and several screens remain scaffolded for
the next iterations (Upload Studio, Voice Tutor).
