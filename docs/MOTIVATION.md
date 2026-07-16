# Motivation: goals, streaks, reminders

Closes the loop: learned → scheduled (SRS) → **reminded** → came back.

## What it tracks (`motivation_state`, per user)
- `daily_goal` — target reviews per day (default 20).
- `today_count` / `today_date` — progress today (rolls over at date change).
- `current_streak` / `longest_streak` — consecutive days the goal was met.
- `reminders_enabled` / `reminder_hour` — Telegram nudge settings.

## Streak rule
When today's count first reaches the goal: if the goal was also met yesterday, streak += 1;
otherwise it resets to 1. A skipped day breaks the streak. Verified with a unit check
(consecutive days build the streak; a gap resets it; longest is retained).

## Wiring
Every SRS review (`POST /api/srs/review`) calls `record_activity`, so the goal fills as the
learner reviews. Nothing else to instrument — the SRS queue is the activity source.

## Reminders (Telegram)
The scheduler worker (`app/workers/scheduler.py`) ticks every 5 min and calls
`send_due_reminders`, which — for users with reminders on, a Telegram id, due cards, and whose
**local** hour (from `UserProfile.timezone`) matches `reminder_hour` — sends one message/day
via the existing bot. Idempotent per day via `last_reminded_date`.

## Endpoints
- `GET  /api/motivation/overview` — goal, today's progress, streaks, due count, reminder settings.
- `POST /api/motivation/goal` — `{daily_goal}`.
- `POST /api/motivation/reminders` — `{enabled, hour}`.

The Dashboard surfaces streak, daily-goal progress, due count, and the reminder toggle/hour.

## Next
- Weekly summary + goal history chart.
- Reuse the same reminder channel for lesson streaks, not just card reviews.
