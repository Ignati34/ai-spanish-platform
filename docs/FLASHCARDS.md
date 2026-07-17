# Flashcards from any material

Build flashcards from whatever the learner has, in either direction.

## Inputs
- **Text** — paste words or a passage.
- **File** — `POST /api/flashcards/from-file` accepts:
  - documents: txt / md / html / pdf / docx (extracted),
  - images: jpg / png / webp (text read via the multimodal model — OCR),
  - audio: mp3 / wav / m4a / ogg (STT),
  - video: mp4 / mov / mkv (ffmpeg extracts the audio track → STT).
- **Voice** — record with the mic; the clip is transcribed (STT) into the text box.

## Direction
A toggle sets the material's language:
- **Material: Spanish** → cards with front = Spanish, back = native translation
  (read Spanish, get the back-translation).
- **Material: my language** → each word is translated to natural Spanish first, then the
  card is built (read your language, get Spanish cards).

## Persistence
Generated cards are saved to a `FlashcardDeck`, so they immediately enter the
spaced-repetition **Review** queue (SM-2).

## Notes / honest limits
- Without a real key, image OCR / STT return demo text (stub), so cards are generic.
- Image OCR uses the vision model (`AI_MODEL` must be multimodal, e.g. gpt-4o-mini).
- Video needs `ffmpeg` (present in the api image); large videos are capped by the upload limit.
