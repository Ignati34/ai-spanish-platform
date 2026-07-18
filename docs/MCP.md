# MCP server — expose lessons to AI assistants

For AI assistants that speak the **Model Context Protocol** (e.g. Claude), the platform runs an
MCP server that exposes its Spanish content as tools. (This is separate from AI-SEO, which is for
web-crawling search engines.)

## Tools
- `list_levels()` — CEFR levels A1–C2.
- `search_lessons(query, level?)` — find curriculum lessons by title/level.
- `get_lesson(lesson_id)` — full lesson: theory + practice exercises.

## Architecture
The MCP server (`services/mcp/`) is a standalone service. It calls the platform's public HTTP API
(`/api/course/...`), so it shares no dependency pins with the backend. In the self-hosted stack it
runs as the `mcp` service on port **8100** with streamable-HTTP transport (endpoint `/mcp`).

## Connect (example: Claude Desktop via a remote/HTTP MCP)
Point your MCP client at `http://<host>:8100/mcp`. For a local Claude Desktop config using an
HTTP/SSE bridge:
```json
{
  "mcpServers": {
    "spanish-tutor": { "url": "http://localhost:8100/mcp" }
  }
}
```
(Exact config depends on your client/version; some clients need an SSE or stdio bridge.)

## Configure
- `MCP_API_BASE` (default `http://api:8000`) — where the platform API lives.
- `MCP_HOST` / `MCP_PORT` (default `0.0.0.0:8100`).

## Security note
The server exposes only **public, read-only** curriculum content (the same data as the public
`/learn` pages), so it needs no auth. If you later expose private data through MCP, add
authentication and put it behind your gateway.
