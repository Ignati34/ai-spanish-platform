# Spaced repetition (SM-2)

Turns generated flashcards into scheduled long-term memory: the system decides what to show
each day instead of the learner re-reading everything.

## Algorithm
Classic SM-2. UI grades map to a quality score: again→1, hard→3, good→4, easy→5.
- Fail (q<3): repetitions reset, card becomes due again this session.
- Pass: interval grows 1 → 6 → round(interval × ease); ease adjusts per grade (floor 1.3).
- `next_review_at = now + interval days`.

Example (all "good"): intervals 1, 6, 15, 38, 95 days. "Easy" grows faster and raises ease.

## State
One `FlashcardReview` row per (user, card) holds the live schedule
(`ease_factor`, `interval_days`, `repetitions`, `next_review_at`). Cards with no row are
**new** and due immediately — so every deck built by Upload Studio / lessons enters the queue
automatically.

## Endpoints
- `GET  /api/srs/due?limit=20` — today's queue (due + new) plus counts.
- `POST /api/srs/review` — `{card_id, grade: again|hard|good|easy}` → next schedule.
- `GET  /api/srs/stats` — total / new / due / learning / mastered.

## UI
The Review screen shows one card at a time: front → reveal → four grade buttons, advancing
through the queue, with a done state when nothing is due.

## Next
- Schedule the targeted (weak-spot) exercises the same way, not just vocabulary cards.
- A daily-goal / streak agent (reuses the Telegram bot) to bring learners back when cards are due.
