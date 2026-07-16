# Runbook — first run, tests, migrations, common errors

## What's verified
- The whole app imports and all SQLAlchemy mappers configure cleanly (no broken relations):
  41 tables, 61 routes.
- An end-to-end **test suite** (`services/api/tests/`) runs the real app on SQLite with stub
  AI and passes: auth, diagnostic, upload→lesson, SRS review, motivation, simulation, billing.
- The initial **Alembic migration** applies and rolls back cleanly.

Not verified here: a live Postgres run and real AI/payment keys (do these on your machine —
steps below).

## A) Quick start — desktop / self-hosted (all in Docker)
```bash
make env            # create .env, .env.selfhosted, apps/web/.env
make selfhosted     # builds everything, runs `alembic upgrade head` + seed, serves :8080
```
Open http://localhost:8080. With `AI_PROVIDER=stub` (default) everything works with demo
output — no keys needed.

## B) Quick start — hosted web service
```bash
make env
make up             # web:8080, api:8000, postgres/redis/minio, worker, scheduler
make migrate        # alembic upgrade head
make seed           # CEFR levels, plans, demo lessons, admin
```

## C) Local dev without Docker
```bash
# needs local Postgres + Redis, and DATABASE_URL in services/api/.env
cd services/api && python -m pip install -r requirements-dev.txt
python -m alembic upgrade head
uvicorn app.main:app --reload         # api on :8000
cd ../../apps/web && npm install && npm run dev   # web on :3000
```

## D) Tests
```bash
make test           # or: cd services/api && python -m pytest -q
```
The suite uses SQLite (a portable UUID shim) and stub AI, so it needs no DB or keys.

## E) Migrations (Alembic)
- Apply latest: `python -m alembic upgrade head` (or `make migrate` in Docker).
- After changing models, autogenerate a migration **against a running DB**:
  `make makemigration m="add teacher groups"` then review the file in
  `services/api/migrations/versions/` before committing.
- `scripts/create_tables.py` (create_all) still exists for throwaway dev DBs, but Alembic is
  the canonical path — don't mix them on the same database.

## F) Turning on real AI and payments
- **AI**: set `AI_PROVIDER=openai`, `AI_API_KEY=...` (and optionally `AI_BASE_URL`, `AI_MODEL`,
  `STT_MODEL`, `TTS_MODEL`). Until then, analysis/transcription/speech are deterministic stubs.
- **Payments**: set `PAYMENT_PROVIDERS` and the Stripe/PayPal/Telegram keys (see `docs/PAYMENTS.md`).
  Test Stripe in test mode; access is granted only on a verified webhook.

## Common errors & fixes
- **`AttributeError: module 'bcrypt' has no attribute '__about__'` / password hashing fails** —
  passlib 1.7.4 is incompatible with bcrypt ≥ 4.1. Fixed by pinning `bcrypt==4.0.1` in
  `requirements.txt`; run `pip install -r requirements.txt` to apply.
- **`relation "users" does not exist` (or similar)** — you skipped migrations. Run
  `alembic upgrade head` (or `make migrate`).
- **`sqlalchemy ... could not connect` on startup** — `DATABASE_URL` is wrong or Postgres isn't
  up. In Docker, wait for the `postgres` healthcheck; locally, start Postgres first.
- **CORS errors in the browser (dev)** — set `CORS_ORIGINS` to include your web origin
  (e.g. `http://localhost:3000`), or run behind nginx where the API is same-origin (`/api`).
- **Frontend calls go to the wrong host** — in dev set `VITE_API_URL=http://localhost:8000`; in
  Docker leave it empty so requests hit same-origin `/api` via nginx.
- **Telegram reminders always fire at UTC hour** — the container lacks tz data; install
  `tzdata` in the worker image (the reminder falls back to UTC otherwise).
- **Audio upload returns 415** — video isn't supported yet; for audio use mp3/wav/m4a/ogg. STT
  needs a real key to produce a real transcript (stub returns a demo transcript).
- **Everything looks generic / demo-ish** — you're on `AI_PROVIDER=stub`. Set a real provider
  (section F).
- **Alembic: "Target database is not up to date"** — run `alembic upgrade head`. To reset a dev
  DB: `alembic downgrade base` then `upgrade head` (destroys data).
