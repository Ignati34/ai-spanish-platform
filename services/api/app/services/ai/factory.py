from __future__ import annotations

from functools import lru_cache

from app.core.config import get_settings
from app.services.ai.base import BaseAIProvider
from app.services.ai.stub_provider import StubProvider

settings = get_settings()


@lru_cache
def get_ai_provider() -> BaseAIProvider:
    provider = (settings.ai_provider or 'stub').lower()
    if provider == 'openai' and settings.ai_api_key:
        try:
            from app.services.ai.openai_provider import OpenAIProvider
            return OpenAIProvider()
        except Exception:
            # Missing optional deps or misconfig -> stay runnable on the stub.
            return StubProvider()
    return StubProvider()
