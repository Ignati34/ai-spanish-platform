# Voice Tutor

Spoken or typed Spanish conversation with correction and scoring.

## Loop
```
student speaks (mic -> STT) OR types
  -> tutor turn via AI gateway: reply_es + correction (native language) + score
  -> reply voiced with TTS
  -> both turns saved to voice_sessions / voice_messages
```
Reuses the STT wired in the previous phase; adds TTS (`synthesize_speech`) and the
conversational turn (`voice_reply`) to the gateway — same provider pattern and fallback.

## Endpoints (auth + metered)
- `POST /api/voice/sessions` — `{scenario, cefr_level, native_language}` → session + opening line (+ audio).
- `POST /api/voice/sessions/{id}/message` — multipart `audio` (a clip) **or** `text` → tutor reply (+ audio).
- `GET  /api/voice/sessions/{id}` — full transcript with corrections/scores.
- `POST /api/voice/transcribe` — standalone STT.

## Audio
The tutor reply is returned as base64 (`audio_b64` + `audio_mime`) for instant playback in the
browser, and also stored via `storage_service`. The web client records mic audio with
`MediaRecorder` (webm) and posts it to the message endpoint.

## Metering
STT seconds → `transcription_seconds_used`; the LLM turn → `ai_requests_used` (+ tokens);
TTS → `tts_seconds_used` (estimated from reply length). All checked against plan quotas.

## Notes / next
- Without a key (`AI_PROVIDER=stub`) the dialogue still works with canned replies and no audio.
- Pronunciation scoring here is the model's judgment of the text; true phoneme-level scoring
  would add an audio-based assessment step later.
- Configure the voice via `TTS_VOICE`; Spanish output uses the `TTS_MODEL`.
