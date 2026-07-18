"""Lightweight fixed-window rate limiter backed by Redis (falls back to in-memory).

Used to throttle brute-force attempts on auth and to cap request floods per IP.
"""
from __future__ import annotations

import logging
import time

from fastapi import HTTPException, Request, status

from app.core.config import get_settings

logger = logging.getLogger(__name__)
settings = get_settings()

_redis = None
_redis_tried = False
_MEM: dict[str, tuple[int, float]] = {}  # key -> (count, reset_epoch)


def _client():
    global _redis, _redis_tried
    if _redis_tried:
        return _redis
    _redis_tried = True
    try:
        import redis  # type: ignore
        _redis = redis.Redis.from_url(settings.redis_url, socket_connect_timeout=1, socket_timeout=1)
        _redis.ping()
    except Exception as exc:  # noqa: BLE001
        logger.info('Rate limiter using in-memory store (redis unavailable: %s)', exc)
        _redis = None
    return _redis


def hit(key: str, limit: int, window: int) -> tuple[bool, int]:
    """Register a hit. Returns (allowed, retry_after_seconds)."""
    r = _client()
    if r is not None:
        try:
            n = r.incr(key)
            if n == 1:
                r.expire(key, window)
            if n > limit:
                ttl = r.ttl(key)
                return False, int(ttl if ttl and ttl > 0 else window)
            return True, 0
        except Exception:  # noqa: BLE001 - fall through to memory
            pass
    now = time.time()
    count, reset = _MEM.get(key, (0, now + window))
    if now > reset:
        count, reset = 0, now + window
    count += 1
    _MEM[key] = (count, reset)
    if count > limit:
        return False, int(reset - now)
    return True, 0


def client_ip(request: Request) -> str:
    xff = request.headers.get('x-forwarded-for')
    if xff:
        return xff.split(',')[0].strip()
    return request.client.host if request.client else 'unknown'


def rate_limit(limit: int, window: int, scope: str):
    """Dependency factory: throttle by client IP within a named scope."""
    def _dep(request: Request):
        if not settings.rate_limit_enabled:
            return
        key = f'rl:{scope}:{client_ip(request)}'
        allowed, retry = hit(key, limit, window)
        if not allowed:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail='Too many requests. Please slow down and try again shortly.',
                headers={'Retry-After': str(retry)},
            )
    return _dep
