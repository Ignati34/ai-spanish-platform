# Backend MVP Notes

## First API scenario

1. Register user: `POST /api/auth/register`
2. Analyze text: `POST /api/analyze/text`
3. Generate flashcards: `POST /api/flashcards/generate`
4. Generate exercises: `POST /api/exercises/generate`
5. Submit exercise answer: `POST /api/exercises/{id}/submit`

## Database strategy

- Development: PostgreSQL container with Docker volume.
- SaaS production: managed PostgreSQL, managed Redis, S3.
- Self-hosted: PostgreSQL/Redis/MinIO inside Docker Compose or external services.

## Next implementation steps

1. Replace AI stubs in `AIGateway` with real provider calls.
2. Persist generated analysis/cards/exercises into PostgreSQL.
3. Add real file upload to MinIO.
4. Add transcription worker.
5. Add billing entitlement checks.
6. Add license activation checks for self-hosted edition.
