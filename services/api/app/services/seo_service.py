"""Helpers for the public, crawlable (AI-SEO) surface: slugs, robots.txt, sitemap.xml,
llms.txt and structured data for curriculum lessons."""
from __future__ import annotations

import html
import re
import unicodedata

from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.models.course import Lesson

settings = get_settings()

# AI + classic crawlers we explicitly welcome.
AI_CRAWLERS = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-Web',
               'anthropic-ai', 'PerplexityBot', 'Perplexity-User', 'Google-Extended',
               'Applebot-Extended', 'CCBot', 'Bingbot', 'Googlebot']


def slugify(text: str) -> str:
    text = unicodedata.normalize('NFKD', text or '')
    text = text.encode('ascii', 'ignore').decode('ascii')  # drop accents; Cyrillic -> empty
    text = re.sub(r'[^a-zA-Z0-9]+', '-', text).strip('-').lower()
    return text or 'lesson'


def lesson_slug(lesson: Lesson) -> str:
    n = (lesson.content_json or {}).get('syllabus_n')
    base = slugify((lesson.content_json or {}).get('title') or lesson.title or '')
    return f'lesson-{n}-{base}' if n else f'{str(lesson.id)[:8]}-{base}'


def published_lessons(db: Session, limit: int = 1000) -> list[Lesson]:
    return (db.query(Lesson)
            .filter(Lesson.lesson_type == 'curriculum')
            .order_by(Lesson.title.asc())
            .limit(limit).all())


def find_by_slug(db: Session, slug: str) -> Lesson | None:
    for l in published_lessons(db):
        if lesson_slug(l) == slug:
            return l
    return None


def robots_txt() -> str:
    base = settings.public_base_url.rstrip('/')
    if not settings.allow_ai_crawlers:
        lines = ['User-agent: *', 'Disallow: /']
    else:
        lines = []
        for bot in AI_CRAWLERS:
            lines += [f'User-agent: {bot}', 'Allow: /', '']
        lines += ['User-agent: *', 'Allow: /$', 'Allow: /learn', 'Disallow: /app', 'Disallow: /api', '']
    lines.append(f'Sitemap: {base}/sitemap.xml')
    return '\n'.join(lines) + '\n'


def sitemap_xml(db: Session) -> str:
    base = settings.public_base_url.rstrip('/')
    urls = [f'{base}/', f'{base}/learn']
    urls += [f'{base}/learn/{lesson_slug(l)}' for l in published_lessons(db)]
    items = ''.join(f'<url><loc>{html.escape(u)}</loc><changefreq>weekly</changefreq></url>' for u in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{items}</urlset>'


def llms_txt(db: Session) -> str:
    base = settings.public_base_url.rstrip('/')
    lessons = published_lessons(db)
    lines = [
        f'# {settings.app_name}',
        '',
        '> An AI-powered Spanish learning platform (CEFR A1–C2) with free, openly readable '
        'grammar lessons: clear theory and practice for each topic. Native-language support '
        'for Russian, Ukrainian, Arabic, French, Spanish and English.',
        '',
        '## Lessons',
    ]
    for l in lessons[:200]:
        lines.append(f'- [{html.escape(l.title)}]({base}/learn/{lesson_slug(l)}) — CEFR {l.cefr_level}')
    lines += ['', '## About', f'- Home: {base}/', f'- Lessons index: {base}/learn']
    return '\n'.join(lines) + '\n'
