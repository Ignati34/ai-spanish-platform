"""MCP server exposing the platform's Spanish-learning content to AI assistants (Claude,
etc.). Decoupled: it talks to the platform's public HTTP API, so it shares no code or
dependency pins with the backend.

Tools:
  - list_levels()                     -> CEFR levels
  - search_lessons(query, level?)     -> matching curriculum lessons (title, level, id)
  - get_lesson(lesson_id)             -> full lesson (theory + exercises)

Run: python server.py  (streamable-http transport; host/port via env).
"""
from __future__ import annotations

import os

import httpx
from mcp.server.fastmcp import FastMCP

API_BASE = os.environ.get('MCP_API_BASE', 'http://api:8000').rstrip('/')
HOST = os.environ.get('MCP_HOST', '0.0.0.0')
PORT = int(os.environ.get('MCP_PORT', '8100'))
TIMEOUT = float(os.environ.get('MCP_TIMEOUT', '20'))

mcp = FastMCP('spanish-tutor', host=HOST, port=PORT)


async def _get(path: str) -> object:
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        r = await client.get(f'{API_BASE}{path}')
        r.raise_for_status()
        return r.json()


@mcp.tool()
async def list_levels():
    """List the available CEFR levels (A1–C2) taught by the platform."""
    return await _get('/api/course/levels')


@mcp.tool()
async def search_lessons(query: str = '', level: str = ''):
    """Search the built-in curriculum. `query` matches lesson titles (case-insensitive);
    `level` optionally filters by CEFR level (e.g. 'B1'). Returns title, level and id."""
    lessons = await _get('/api/course/lessons')
    q = (query or '').strip().lower()
    lvl = (level or '').strip().upper()
    out = []
    for l in lessons:
        if lvl and (l.get('cefr_level') or '').upper() != lvl:
            continue
        if q and q not in (l.get('title') or '').lower():
            continue
        out.append({'id': l.get('id'), 'title': l.get('title'), 'level': l.get('cefr_level')})
    return out[:50]


@mcp.tool()
async def get_lesson(lesson_id: str):
    """Fetch a full lesson by id: title, CEFR level, theory text and practice exercises."""
    l = await _get(f'/api/course/lessons/{lesson_id}')
    return {
        'id': l.get('id'), 'title': l.get('title'), 'level': l.get('cefr_level'),
        'theory': l.get('theory') or l.get('summary') or '',
        'exercises': [{'prompt': e.get('prompt'), 'options': e.get('options'),
                       'answer': e.get('correct_answer'), 'explanation': e.get('explanation')}
                      for e in (l.get('exercises') or [])],
    }


if __name__ == '__main__':
    mcp.run(transport='streamable-http')
