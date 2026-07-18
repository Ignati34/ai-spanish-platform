"""Rate limiter behaviour (in-memory path)."""
from app.services.security import rate_limiter


def test_allows_up_to_limit_then_blocks(monkeypatch):
    # force in-memory path
    monkeypatch.setattr(rate_limiter, '_redis', None)
    monkeypatch.setattr(rate_limiter, '_redis_tried', True)
    key = 'rl:test:1.2.3.4'
    rate_limiter._MEM.pop(key, None)
    allowed = [rate_limiter.hit(key, limit=3, window=60)[0] for _ in range(5)]
    assert allowed == [True, True, True, False, False]


def test_security_headers_present(client):
    r = client.get('/api/health')
    assert r.headers.get('x-content-type-options') == 'nosniff'
    assert r.headers.get('x-frame-options') == 'DENY'
    assert 'referrer-policy' in {k.lower() for k in r.headers.keys()}
