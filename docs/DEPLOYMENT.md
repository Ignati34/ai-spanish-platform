# Deployment — web service and desktop/self-hosted

Both targets use the same images; only the compose file differs.

## A) Web service (hosted)
```bash
make env            # create .env files
# edit .env: DB, JWT_SECRET, Stripe/PayPal/Telegram keys, domain URLs
make up             # builds web + api + worker + scheduler + postgres + redis + minio
make migrate        # once
make seed           # levels A1-C2, plans, demo lessons, admin
```
- Web UI: http://localhost:8080  (nginx serves the SPA and proxies `/api` → api:8000)
- API docs: http://localhost:8000/docs
Put this behind your own TLS terminator / load balancer in production and point DNS at `web`.

## B) Desktop / self-hosted (everything in Docker)
```bash
make env
make selfhosted     # one command: builds all, auto create_tables + seed
```
- Open http://localhost:8080 — the whole platform runs locally in containers.
- `SELF_HOSTED_MODE=true`, `PAYMENT_PROVIDERS=stripe` by default; no external PSP needed to
  browse/learn. Data persists in named Docker volumes (`sh_postgres_data`, `sh_minio_data`).
- Ship it as a folder + `docker compose` for on-prem schools / offline demos, gated by the
  licensing module (`app/services/license_service.py`).

## Local dev without Docker
```bash
make api-dev        # FastAPI on :8000 (needs local postgres+redis)
make web-dev        # Vite on :3000, talks to http://localhost:8000
```
