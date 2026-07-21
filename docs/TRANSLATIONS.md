# Content translations (native-language learning)

The interface is localized via `apps/web/src/i18n.ts` (ru/uk/ar/fr/es/en, Arabic RTL).
This note covers **content** translations — the learning material itself.

## What ships pre-translated (no AI key needed)

- **Dialogues** (`services/api/app/content/dialogues.py`): every line carries a gloss in
  ru/uk/ar/fr/en. `public_list(level, lang)` serves the learner's own language with
  graceful fallback (requested → ru → en → es). Titles are localized too.
- **Vocabulary bank** (`services/api/app/content/vocab_bank.json`): proofread; es + ru.

## What is translated lazily and cached (needs a real AI provider)

The Spanish practice content is authored once (Spanish stems + Russian explanations) and
translated into the learner's language on first use, then cached so nobody waits twice.

| Content   | Serves via                         | Cache table / column                  |
|-----------|------------------------------------|---------------------------------------|
| Theory    | `GET /api/course/lessons/{id}?lang=` | `lesson_translations.theory`          |
| Exercises | same endpoint (prompt+explanation) | `lesson_translations.exercises`       |
| Reading   | `GET /api/reading/{id}?lang=`      | `reading_translations` (title, body)  |

Notes:
- Only Russian text is translated. Spanish fill-in stems (e.g. `Yo ___ estudiante.`),
  options and `correct_answer` are kept verbatim so the exercise still tests Spanish.
- Under the stub provider (no key) translations are identity and are **not** cached; the
  Spanish/Russian source is served unchanged.

## Pre-warming (fill the caches ahead of time)

Run inside the API container (`services/api`) with a real provider configured:

```bash
export AI_PROVIDER=openai AI_API_KEY=sk-...
python scripts/prewarm_translations.py                          # theory+exercises+reading, uk,ar,fr,en
python scripts/prewarm_translations.py --targets exercises      # just exercises
python scripts/prewarm_translations.py --langs uk,fr --level B1 --limit 5   # a cheap slice first
python scripts/prewarm_translations.py --force --sleep 0.3      # re-translate, gentle throttle
```

Idempotent and interrupt-safe: cached, unchanged items are skipped (invalidated by a
source hash), and each translation commits as it completes. Built-in dialogues are already
pre-translated in code, so they are not part of the warm run.
