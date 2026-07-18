# AI-SEO — being found and cited by AI search

AI search engines (Google AI Overviews/SGE, Perplexity, ChatGPT Search, Bing) discover you by
**crawling the public web** — they do not use MCP. So the platform exposes a public, crawlable
surface with structured data.

## What ships
- **Public lesson pages** — server-rendered HTML at `/learn` (index) and `/learn/{slug}` (each
  curriculum lesson: theory + practice), free to read, with `schema.org` **JSON-LD**
  (`Course`, `LearningResource`), Open Graph and canonical tags.
- **robots.txt** — explicitly welcomes AI crawlers (GPTBot, OAI-SearchBot, ClaudeBot,
  PerplexityBot, Google-Extended, Applebot-Extended, CCBot, Bingbot, Googlebot) and links the
  sitemap. Toggle with `ALLOW_AI_CRAWLERS`.
- **sitemap.xml** — all public pages + every lesson.
- **llms.txt** — an AI-readable summary + index of lessons (emerging convention).
- The SPA `index.html` carries description, Open Graph and JSON-LD (`WebSite`, `Course`).

## Configure
- `PUBLIC_BASE_URL` — your real public URL (used in canonical/sitemap/llms). Set this to your
  domain in production, e.g. `https://tu-dominio.com`.
- `AI_SEO_ENABLED` — master switch. `ALLOW_AI_CRAWLERS` — allow/deny AI bots.

## Verify
- `curl http://localhost:8080/robots.txt`
- `curl http://localhost:8080/sitemap.xml`
- `curl http://localhost:8080/llms.txt`
- open `http://localhost:8080/learn` and a lesson; view source → JSON-LD present.
- Google Rich Results Test / Schema.org validator on a public lesson URL.

## Notes
- More lessons = more indexable pages. Generate the curriculum (Admin → Curriculum) to expand
  the public surface.
- Content pages are read-only and contain no user data.
