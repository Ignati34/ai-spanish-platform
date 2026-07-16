# Personalization: "My mistakes" & progress

Turns the vertical features into a feedback loop: every module feeds the learner's weak
spots, which then drive targeted practice and the study plan.

## Where mistakes come from (auto-recorded into `user_mistakes`)
- **Diagnostic** — diagnosed gaps are seeded as mistakes (`mistake_type='gap'`).
- **Voice Tutor** — each tutor correction becomes a mistake (`mistake_type='speaking'`).
- **Exercises** — wrong submissions are recorded (`mistake_type='exercise'`).
(Extend the same `progress_service.record_mistake` call anywhere else errors surface.)

## Aggregation (`services/progress_service.py`)
- `weak_spots` groups mistakes by `grammar_topic` (fallback: mistake type), ranked by count.
- `study_plan` starts from the latest diagnostic plan, then appends the top weak topics.
- `overview` returns level + totals + weak spots + plan + recent mistakes.

## Endpoints
- `GET  /api/progress/overview` — dashboard data (level, weak spots, plan, recent).
- `GET  /api/progress/mistakes` — full ranked weak-spot list.
- `POST /api/progress/practice` — AI generates remedial exercises targeting the top weak spots
  (`targeted_exercises` on the gateway; metered; native-language explanations).

## Why this is the glue, not another vertical
It consumes what the other modules already produce (diagnostic, voice, exercises) and closes
the loop back into practice — the "my mistakes → targeted drills" cycle from the brief. Next
natural steps: spaced-repetition scheduling of weak-spot drills, and a daily-goal/streak agent.
