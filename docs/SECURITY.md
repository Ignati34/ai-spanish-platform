# Security — upload malware scanning (ClamAV)

The app accepts many uploads (documents, images, audio, video), so every uploaded file is
scanned for malware **before** it is processed.

## How it works
- A `clamav` container runs the ClamAV daemon (`clamd`) with up-to-date signatures.
- The API scans each upload over the clamd INSTREAM protocol (`services/security/clamav_service.py`).
- Wired into every upload path: Upload Studio, Flashcards-from-file, Podcasts, Voice tutor
  and Simulations (`scan_upload_or_raise`).
- Infected files are rejected with HTTP 422 and the detection is logged.

## Configuration (.env.selfhosted)
- `MALWARE_SCAN_ENABLED` (default true in self-hosted) — master switch.
- `CLAMAV_HOST` / `CLAMAV_PORT` — where clamd listens (defaults `clamav:3310`).
- `MALWARE_SCAN_FAIL_CLOSED` — if the scanner is unreachable: `false` allows uploads with a
  logged warning (default), `true` rejects them (HTTP 503).

## Operating notes
- On first start clamd loads its signature database (~1–2 min). During that window it may be
  unreachable; with the default fail-open, uploads still work and are logged as unscanned.
- Admins can check status at `GET /api/admin/security/status` or the Admin → Security panel
  (enabled / reachable / engine version).
- ClamAV's default stream limit is 25 MB (matches `MAX_UPLOAD_MB`); raise both together if needed.
- Test safely with the EICAR test string (a harmless standard AV test file) — it will be
  flagged as `Eicar-Test-Signature` and rejected.

---

# Security headers, rate limiting & dependency audit

## Security headers
Every response carries hardening headers. The API sets them via middleware; nginx also sets
them for the SPA/static files:
`X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`,
`Referrer-Policy: strict-origin-when-cross-origin`, `Permissions-Policy` (camera off, mic self),
and a `Content-Security-Policy` scoped to same-origin. `Strict-Transport-Security` (HSTS) is
off by default — enable `HSTS_ENABLED=true` only when serving over HTTPS.

## Rate limiting (brute-force / flood protection)
Backed by Redis (in-memory fallback). Two layers:
- **Per-IP API limit** across all `/api` (default 240/min) — blunts floods.
- **Strict login/register limit** per IP (default 10 per 5 min) — blunts credential brute force.
Exceeding a limit returns HTTP 429 with `Retry-After`. Tune via `RATE_LIMIT_*` env vars, or turn
off with `RATE_LIMIT_ENABLED=false`.

## Dependency vulnerability audit
Admin → Security → **Проверить зависимости** runs `pip-audit` against the installed Python
packages and lists any known vulnerabilities (id + fix versions). Needs outbound network to the
OSV/PyPI advisory DB; runs on demand (up to ~2 min). For the frontend, run `npm audit` in CI or
locally (`cd apps/web && npm audit`) — it isn't executed from the running container.

## Admin security panel
`GET /api/admin/security/status` returns malware-scan, headers and rate-limit posture;
`POST /api/admin/security/audit-dependencies` runs the audit. Both require an admin token.
