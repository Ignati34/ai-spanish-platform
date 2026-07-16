# Course content & licensing (please read)

## Vinogradov textbook
The Vinogradov "Español" course and задачник (problem book) are **copyrighted works**.
You must not copy their text, exercises, tables, or audio into this platform unless you
hold a licence or written permission from the rightsholder/publisher. This repository does
**not** include any Vinogradov content. The seed data in
`services/api/app/content/seed_content.py` is original material written for the platform.

If you have the rights, import the material through the content pipeline:
- store source files in object storage (MinIO/S3),
- create `CourseModule` / `Lesson` rows with `content_json`,
- keep an internal record of the licence covering each imported source.

## License-clean alternatives you can use freely
Useful when you want breadth without licensing a single textbook:
- **CEFR level structure** — organise A1–C2 yourself; the "can-do" idea is a framework, but
  write your own descriptions (as done here) rather than quoting the Council of Europe text.
- **Tatoeba** — large bank of example sentences with translations (CC-BY 2.0). Great for
  flashcards and analyzer examples. Keep attribution.
- **Wikibooks / Wikipedia (Spanish)** — CC BY-SA; good for reading material with attribution.
- **Public-domain literature** (e.g. old texts via Project Gutenberg) for B1+ reading.
- **User-supplied material** — the product's core loop already turns the learner's own
  files into lessons; that content belongs to the user, which sidesteps licensing entirely.

## Practical stance for the MVP
Ship original + user-supplied + openly-licensed content. Treat any named commercial textbook
(Vinogradov included) as a **licensed integration** to enable later, not as bundled data.
