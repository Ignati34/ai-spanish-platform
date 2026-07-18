"""Public, crawlable AI-SEO surface (no /api prefix, no auth): robots.txt, sitemap.xml,
llms.txt and server-rendered lesson pages with structured data (JSON-LD)."""
from __future__ import annotations

import html
import json

from fastapi import APIRouter, Depends, HTTPException, Response
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.db.session import get_db
from app.services import seo_service

settings = get_settings()
router = APIRouter(tags=['public'])


def _page(title: str, description: str, body: str, jsonld: dict | None = None, path: str = '/') -> str:
    base = settings.public_base_url.rstrip('/')
    url = base + path
    ld = f'<script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>' if jsonld else ''
    t = html.escape(title)
    d = html.escape(description)
    return f'''<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>{t}</title>
<meta name="description" content="{d}"/>
<link rel="canonical" href="{html.escape(url)}"/>
<meta property="og:type" content="website"/>
<meta property="og:title" content="{t}"/>
<meta property="og:description" content="{d}"/>
<meta property="og:url" content="{html.escape(url)}"/>
<meta name="twitter:card" content="summary"/>
{ld}
<style>body{{font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;max-width:720px;margin:2rem auto;padding:0 1rem;line-height:1.6;color:#0f172a}}a{{color:#4f46e5}}.cta{{display:inline-block;margin-top:1.5rem;padding:.6rem 1rem;background:#4f46e5;color:#fff;border-radius:.5rem;text-decoration:none}}nav{{font-size:.9rem;margin-bottom:1rem}}</style>
</head>
<body>
<nav><a href="{base}/">{html.escape(settings.app_name)}</a> · <a href="{base}/learn">Lecciones</a></nav>
{body}
<a class="cta" href="{base}/app">Empieza a aprender →</a>
</body>
</html>'''


@router.get('/robots.txt', response_class=Response)
def robots():
    if not settings.ai_seo_enabled:
        return Response('User-agent: *\nDisallow: /\n', media_type='text/plain')
    return Response(seo_service.robots_txt(), media_type='text/plain')


@router.get('/sitemap.xml', response_class=Response)
def sitemap(db: Session = Depends(get_db)):
    return Response(seo_service.sitemap_xml(db), media_type='application/xml')


@router.get('/llms.txt', response_class=Response)
def llms(db: Session = Depends(get_db)):
    return Response(seo_service.llms_txt(db), media_type='text/plain')


@router.get('/learn', response_class=Response)
def learn_index(db: Session = Depends(get_db)):
    if not settings.ai_seo_enabled:
        raise HTTPException(status_code=404)
    lessons = seo_service.published_lessons(db)
    by_level: dict[str, list] = {}
    for l in lessons:
        by_level.setdefault(l.cefr_level or 'A1', []).append(l)
    parts = ['<h1>Lecciones de español</h1>',
             '<p>Teoría clara y práctica para cada tema, de A1 a C2. Acceso libre.</p>']
    for lvl in ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']:
        items = by_level.get(lvl, [])
        if not items:
            continue
        parts.append(f'<h2>{lvl}</h2><ul>')
        for l in items:
            parts.append(f'<li><a href="/learn/{seo_service.lesson_slug(l)}">{html.escape(l.title)}</a></li>')
        parts.append('</ul>')
    jsonld = {'@context': 'https://schema.org', '@type': 'Course',
              'name': 'Curso de español A1–C2', 'provider': {'@type': 'Organization', 'name': settings.app_name},
              'numberOfCredits': len(lessons)}
    return Response(_page('Lecciones de español A1–C2', 'Teoría y práctica de gramática española, de A1 a C2.',
                          '\n'.join(parts), jsonld, '/learn'), media_type='text/html')


@router.get('/learn/{slug}', response_class=Response)
def learn_lesson(slug: str, db: Session = Depends(get_db)):
    if not settings.ai_seo_enabled:
        raise HTTPException(status_code=404)
    lesson = seo_service.find_by_slug(db, slug)
    if not lesson:
        raise HTTPException(status_code=404, detail='Lesson not found')
    content = lesson.content_json or {}
    theory = content.get('theory') or lesson.description or ''
    paragraphs = ''.join(f'<p>{html.escape(p.strip())}</p>' for p in theory.split('\n') if p.strip())
    exercises = content.get('exercises') or []
    ex_html = ''
    if exercises:
        ex_html = '<h2>Práctica</h2><ol>' + ''.join(
            f'<li>{html.escape(e.get("prompt", ""))}</li>' for e in exercises[:6]) + '</ol>'
    desc = (theory[:150] + '…') if len(theory) > 150 else (theory or lesson.title)
    jsonld = {'@context': 'https://schema.org', '@type': 'LearningResource',
              'name': lesson.title, 'educationalLevel': lesson.cefr_level,
              'inLanguage': 'es', 'teaches': lesson.title,
              'learningResourceType': 'lesson',
              'isAccessibleForFree': True,
              'provider': {'@type': 'Organization', 'name': settings.app_name}}
    body = f'<h1>{html.escape(lesson.title)}</h1><p><em>CEFR {html.escape(lesson.cefr_level or "")}</em></p>{paragraphs}{ex_html}'
    return Response(_page(lesson.title, desc, body, jsonld, f'/learn/{slug}'), media_type='text/html')
