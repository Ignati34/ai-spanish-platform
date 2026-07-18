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
