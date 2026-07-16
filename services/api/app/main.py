from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import uuid
from app.api.router import api_router
from app.core.config import get_settings
from app.core.logging import configure_logging

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
