from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import uuid
from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging
from app.services.security.rate_limiter import hit as _rl_hit, client_ip as _client_ip
from starlette.responses import JSONResponse

configure_logging()
settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version='0.1.0',
    description='Backend MVP scaffold for AI Spanish Learning Platform',
)


class RequestIDMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_id = request.headers.get('x-request-id', str(uuid.uuid4()))
        request.state.request_id = request_id
        response = await call_next(request)
        response.headers['x-request-id'] = request_id
        return response


class SecurityHeadersMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        if settings.security_headers_enabled:
            h = response.headers
            h.setdefault('X-Content-Type-Options', 'nosniff')
            h.setdefault('X-Frame-Options', 'DENY')
            h.setdefault('Referrer-Policy', 'strict-origin-when-cross-origin')
            h.setdefault('Permissions-Policy', 'geolocation=(), microphone=(self), camera=()')
            h.setdefault('Cross-Origin-Opener-Policy', 'same-origin')
            if settings.hsts_enabled:
                h.setdefault('Strict-Transport-Security', 'max-age=31536000; includeSubDomains')
        return response


class GlobalRateLimitMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if settings.rate_limit_enabled and request.url.path.startswith('/api'):
            allowed, retry = _rl_hit(f'rl:api:{_client_ip(request)}', settings.rate_limit_api_per_min, 60)
            if not allowed:
                return JSONResponse({'detail': 'Too many requests. Please slow down.'},
                                    status_code=429, headers={'Retry-After': str(retry)})
        return await call_next(request)


app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(GlobalRateLimitMiddleware)
app.add_middleware(RequestIDMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(api_router)


@app.get('/')
def root():
    return {
        'app': settings.app_name,
        'status': 'running',
        'docs': '/docs',
        'health': '/api/health',
    }
