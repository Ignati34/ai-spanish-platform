"""Fetch readable text from a web page or a Google Docs link, safely.

Two jobs:
  * normalize_target() — turns a user URL into a fetchable one. Google Docs links are
    rewritten to their plain-text export endpoint; everything else is treated as a web page.
  * assert_safe_url() / fetch() — block SSRF (private, loopback, link-local, reserved IPs)
    and download with a size cap.

The doc/page must be publicly reachable (for Google Docs: "anyone with the link").
"""
from __future__ import annotations

import ipaddress
import re
import socket
from urllib.parse import urlparse, parse_qs


class UrlError(ValueError):
    pass


_GDOC_ID = re.compile(r'/document/d/([a-zA-Z0-9_-]+)')


def normalize_target(url: str) -> tuple[str, str, str]:
    """Return (fetch_url, kind, label). kind in {'gdoc','web'}.

    Raises UrlError for anything that isn't a plain http(s) URL.
    """
    url = (url or '').strip()
    if not url:
        raise UrlError('empty URL')
    if not re.match(r'^https?://', url, re.I):
        # Be forgiving: assume https if the user pasted a bare domain.
        if re.match(r'^[\w.-]+\.[a-z]{2,}(/|$)', url, re.I):
            url = 'https://' + url
        else:
            raise UrlError('only http(s) URLs are supported')

    parsed = urlparse(url)
    host = (parsed.hostname or '').lower()

    # Google Docs -> plain-text export.
    if host in {'docs.google.com', 'www.docs.google.com'}:
        m = _GDOC_ID.search(parsed.path)
        doc_id = m.group(1) if m else (parse_qs(parsed.query).get('id', [None])[0])
        if doc_id:
            return (f'https://docs.google.com/document/d/{doc_id}/export?format=txt', 'gdoc', 'Google Doc')
        # A non-document Google link — fall through and fetch as a page.

    return (url, 'web', host or 'web page')


def _ip_blocked(ip: str) -> bool:
    try:
        addr = ipaddress.ip_address(ip)
    except ValueError:
        return True
    return (addr.is_private or addr.is_loopback or addr.is_link_local
            or addr.is_reserved or addr.is_multicast or addr.is_unspecified)


def assert_safe_url(url: str) -> None:
    """Reject URLs whose host resolves to a non-public address (SSRF guard)."""
    parsed = urlparse(url)
    if parsed.scheme not in {'http', 'https'}:
        raise UrlError('only http(s) URLs are supported')
    host = parsed.hostname
    if not host:
        raise UrlError('invalid URL host')
    # Literal IP address?
    try:
        if _ip_blocked(host):
            raise UrlError('URL points to a non-public address')
        return
    except UrlError:
        raise
    except ValueError:
        pass
    # Resolve DNS and check every returned address.
    try:
        infos = socket.getaddrinfo(host, None)
    except socket.gaierror as exc:
        raise UrlError(f'cannot resolve host: {host}') from exc
    for info in infos:
        ip = info[4][0]
        if _ip_blocked(ip):
            raise UrlError('URL resolves to a non-public address')


async def fetch(url: str, max_bytes: int) -> tuple[bytes, str, str]:
    """Fetch a URL safely. Returns (data, content_type, final_url).

    Follows redirects, then re-validates the final host (post-redirect SSRF guard) and
    enforces a size cap.
    """
    import httpx

    assert_safe_url(url)
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; SpanishPlatformBot/1.0)'}
    async with httpx.AsyncClient(timeout=20.0, follow_redirects=True, headers=headers) as client:
        resp = await client.get(url)
    # Re-validate after redirects.
    assert_safe_url(str(resp.url))
    resp.raise_for_status()
    data = resp.content
    if len(data) > max_bytes:
        raise UrlError('remote content is too large')
    ctype = resp.headers.get('content-type', '')
    return data, ctype, str(resp.url)


def filename_for(kind: str, content_type: str) -> str:
    """A synthetic filename so the extractor picks the right path."""
    if kind == 'gdoc':
        return 'gdoc.txt'
    if 'html' in (content_type or '') or kind == 'web':
        return 'page.html'
    if 'pdf' in (content_type or ''):
        return 'page.pdf'
    return 'page.txt'
