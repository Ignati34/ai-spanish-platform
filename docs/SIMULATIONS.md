# Role-play simulations

Mini-missions built on top of the Voice Tutor. A scenario gives the AI a **role** and the
learner a **goal**; the model judges when the goal is achieved.

## What's added over the Voice Tutor
- **Scenarios** (`content/simulations.py`, original/license-clean): clinic appointment, bank
  complaint, job interview, flat rental, town-hall registration (empadronamiento) — the
  real-life situations from the brief. Titles/goals localized; role/hints/setup in Spanish.
- **Goal + hints** shown to the learner; **goal-achievement** judged each turn by the model.
- Everything else is reused: STT (spoken input), TTS (voiced reply), `VoiceSession` /
  `VoiceMessage` for the dialogue, and mistake recording into the personalization layer.

## Flow / endpoints (auth + metered: STT + AI + TTS)
- `GET  /api/simulations/scenarios?native_language=ru` — available missions.
- `POST /api/simulations/start` — `{scenario_id, cefr_level, native_language}` → in-character
  opening (+ audio), goal and hints.
- `POST /api/simulations/{id}/message` — multipart `audio` or `text` → reply + correction +
  score + `goal_met` + next hint (+ audio). When `goal_met`, the session is marked completed.
- `GET  /api/simulations/{id}` — transcript with per-turn feedback.

## UI
Pick a scenario (role + goal shown) → dialogue with a goal banner, tappable hint chips,
per-turn correction/score, and a "goal reached" state that ends the mission.

## Honest limitation
"Goal achieved" is the model's judgement of the conversation, not a hard check. On the stub
(no key) it completes after a few turns so the flow is demoable; with a real model it's
meaningful. Pronunciation scoring is still text-based (see Voice Tutor notes).

## Next
- Per-scenario final report (what went well, what to review) written to the progress layer.
- More scenarios + difficulty scaling; DELE oral exam format as a scenario.
