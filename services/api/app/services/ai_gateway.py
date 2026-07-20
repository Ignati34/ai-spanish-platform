"""AI gateway: single entry point the agents/orchestrator call.

Responsibilities:
  * pick the configured provider (stub or a real OpenAI-compatible model),
  * cache identical requests (Redis if available, else in-process),
  * expose token usage via `last_usage` so routes can meter UsageCounter,
  * degrade gracefully — if the real provider errors, fall back to the stub so
    the endpoint still returns a valid (if simpler) result.
"""
from __future__ import annotations

import hashlib
import json
import logging

from app.core.config import get_settings
from app.services.ai.factory import get_ai_provider
from app.services.ai.stub_provider import StubProvider

logger = logging.getLogger('ai_gateway')
settings = get_settings()

try:
    import redis  # type: ignore
except Exception:  # pragma: no cover
    redis = None


class _Cache:
    """Tiny cache: Redis when reachable, otherwise an in-process dict."""

    def __init__(self) -> None:
        self._mem: dict[str, str] = {}
        self._redis = None
        if settings.ai_cache_enabled and redis is not None:
            try:
                self._redis = redis.Redis.from_url(settings.redis_url, socket_connect_timeout=1)
                self._redis.ping()
            except Exception:
                self._redis = None

    def get(self, key: str):
        if not settings.ai_cache_enabled:
            return None
        try:
            raw = self._redis.get(key) if self._redis else self._mem.get(key)
        except Exception:
            raw = self._mem.get(key)
        return json.loads(raw) if raw else None

    def set(self, key: str, value: dict) -> None:
        if not settings.ai_cache_enabled:
            return
        raw = json.dumps(value, ensure_ascii=False)
        try:
            if self._redis:
                self._redis.setex(key, settings.ai_cache_ttl_seconds, raw)
            else:
                self._mem[key] = raw
        except Exception:
            self._mem[key] = raw


_cache = _Cache()


def _key(task: str, **parts) -> str:
    payload = json.dumps({'task': task, 'model': settings.ai_model, 'provider': settings.ai_provider, **parts}, sort_keys=True, ensure_ascii=False)
    return 'ai:' + hashlib.sha256(payload.encode()).hexdigest()


class AIGateway:
    """Provider-agnostic facade with cache + graceful fallback."""

    def __init__(self) -> None:
        self.provider = get_ai_provider()
        self._stub = StubProvider()
        self.last_usage: dict[str, int] = {'input_tokens': 0, 'output_tokens': 0}

    async def _run(self, task: str, cache_parts: dict, call, stub_call):
        self.last_usage = {'input_tokens': 0, 'output_tokens': 0}
        key = _key(task, **cache_parts)
        cached = _cache.get(key)
        if cached is not None:
            return cached
        try:
            result = await call(self.provider)
            self.last_usage = getattr(self.provider, 'last_usage', self.last_usage)
        except Exception as exc:  # provider/network/parse failure -> stub
            logger.warning('AI provider "%s" failed on %s: %s; using stub fallback', self.provider.name, task, exc)
            result = await stub_call(self._stub)
        _cache.set(key, result)
        return result

    async def analyze_text(self, text: str, native_language: str = 'ru') -> dict:
        return await self._run(
            'analyze', {'text': text, 'native': native_language},
            lambda p: p.analyze_text(text=text, native_language=native_language),
            lambda p: p.analyze_text(text=text, native_language=native_language),
        )

    async def generate_flashcards(self, text: str, native_language: str = 'ru', cefr_level: str = 'A1', source_language: str = 'es') -> dict:
        return await self._run(
            'flashcards', {'text': text, 'native': native_language, 'cefr': cefr_level},
            lambda p: p.generate_flashcards(text=text, native_language=native_language, cefr_level=cefr_level, source_language=source_language),
            lambda p: p.generate_flashcards(text=text, native_language=native_language, cefr_level=cefr_level, source_language=source_language),
        )

    async def generate_exercises(self, text: str, cefr_level: str = 'A1', native_language: str = 'ru') -> dict:
        return await self._run(
            'exercises', {'text': text, 'native': native_language, 'cefr': cefr_level},
            lambda p: p.generate_exercises(text=text, cefr_level=cefr_level, native_language=native_language),
            lambda p: p.generate_exercises(text=text, cefr_level=cefr_level, native_language=native_language),
        )

    async def check_answer(self, answer: str, correct_answer: str | None = None) -> dict:
        # Not cached: answers are user-specific and cheap.
        self.last_usage = {'input_tokens': 0, 'output_tokens': 0}
        try:
            result = await self.provider.check_answer(answer=answer, correct_answer=correct_answer)
            self.last_usage = getattr(self.provider, 'last_usage', self.last_usage)
            return result
        except Exception as exc:
            logger.warning('AI provider failed on check_answer: %s; using stub', exc)
            return await self._stub.check_answer(answer=answer, correct_answer=correct_answer)

    async def transcribe_audio(self, data: bytes, filename: str, language: str = 'es') -> dict:
        """Speech-to-text with graceful fallback. Not cached (audio is large/unique)."""
        try:
            return await self.provider.transcribe(data=data, filename=filename, language=language)
        except Exception as exc:
            logger.warning('AI provider "%s" failed on transcribe: %s; using stub', self.provider.name, exc)
            return await self._stub.transcribe(data=data, filename=filename, language=language)

    async def extract_image_text(self, data: bytes, mime_type: str = 'image/png') -> str:
        """Vision OCR with graceful fallback."""
        try:
            return await self.provider.extract_image_text(data=data, mime_type=mime_type)
        except Exception as exc:
            logger.warning('AI provider "%s" failed on image OCR: %s; using stub', self.provider.name, exc)
            return await self._stub.extract_image_text(data=data, mime_type=mime_type)

    async def generate_lesson(self, topic_es: str, topic_native: str, cefr_level: str = 'A1', native_language: str = 'ru', focus: str = '') -> dict:
        """Author a full lesson (theory + exercises). Not cached."""
        self.last_usage = {'input_tokens': 0, 'output_tokens': 0}
        try:
            result = await self.provider.generate_lesson(topic_es, topic_native, cefr_level, native_language, focus)
            self.last_usage = getattr(self.provider, 'last_usage', self.last_usage)
            return result
        except Exception as exc:
            logger.warning('AI provider failed on generate_lesson: %s; using stub', exc)
            return await self._stub.generate_lesson(topic_es, topic_native, cefr_level, native_language, focus)

    async def generate_dialogue(self, topic: str, cefr_level: str = 'A1', native_language: str = 'ru') -> dict:
        """Generate a short, level-graded two-speaker dialogue on a topic. Not cached."""
        self.last_usage = {'input_tokens': 0, 'output_tokens': 0}
        try:
            result = await self.provider.generate_dialogue(topic, cefr_level, native_language)
            self.last_usage = getattr(self.provider, 'last_usage', self.last_usage)
            return result
        except Exception as exc:
            logger.warning('AI provider failed on generate_dialogue: %s; using stub', exc)
            return await self._stub.generate_dialogue(topic, cefr_level, native_language)

    async def voice_reply(self, history: list[dict], user_message: str, scenario: str = 'restaurant', cefr_level: str = 'A1', native_language: str = 'ru') -> dict:
        """Conversational tutor reply + correction + score. Not cached."""
        self.last_usage = {'input_tokens': 0, 'output_tokens': 0}
        try:
            result = await self.provider.voice_reply(history, user_message, scenario, cefr_level, native_language)
            self.last_usage = getattr(self.provider, 'last_usage', self.last_usage)
            return result
        except Exception as exc:
            logger.warning('AI provider failed on voice_reply: %s; using stub', exc)
            return await self._stub.voice_reply(history, user_message, scenario, cefr_level, native_language)

    async def synthesize_speech(self, text: str, voice: str | None = None, language: str = 'es') -> bytes:
        """Text-to-speech with graceful fallback (empty bytes if unavailable)."""
        try:
            return await self.provider.synthesize(text=text, voice=voice, language=language)
        except Exception as exc:
            logger.warning('AI provider "%s" failed on synthesize: %s; no audio', self.provider.name, exc)
            return b''

    async def assess_level(self, writing_sample: str, speaking_sample: str, mc_summary: dict, native_language: str = 'ru') -> dict:
        """CEFR assessment from MC performance + free production. Not cached."""
        self.last_usage = {'input_tokens': 0, 'output_tokens': 0}
        try:
            result = await self.provider.assess_level(writing_sample, speaking_sample, mc_summary, native_language)
            self.last_usage = getattr(self.provider, 'last_usage', self.last_usage)
            return result
        except Exception as exc:
            logger.warning('AI provider failed on assess_level: %s; using stub', exc)
            return await self._stub.assess_level(writing_sample, speaking_sample, mc_summary, native_language)

    async def targeted_exercises(self, topics: list, cefr_level: str = 'A1', native_language: str = 'ru') -> dict:
        """Remedial exercises focused on the learner's weak topics. Not cached."""
        self.last_usage = {'input_tokens': 0, 'output_tokens': 0}
        try:
            result = await self.provider.targeted_exercises(topics, cefr_level, native_language)
            self.last_usage = getattr(self.provider, 'last_usage', self.last_usage)
            return result
        except Exception as exc:
            logger.warning('AI provider failed on targeted_exercises: %s; using stub', exc)
            return await self._stub.targeted_exercises(topics, cefr_level, native_language)

    async def simulation_turn(self, history: list, user_message: str, role: str, goal_es: str, cefr_level: str = 'A1', native_language: str = 'ru') -> dict:
        """One turn of a role-play mission: reply + correction + score + goal_met. Not cached."""
        self.last_usage = {'input_tokens': 0, 'output_tokens': 0}
        try:
            result = await self.provider.simulation_turn(history, user_message, role, goal_es, cefr_level, native_language)
            self.last_usage = getattr(self.provider, 'last_usage', self.last_usage)
            return result
        except Exception as exc:
            logger.warning('AI provider failed on simulation_turn: %s; using stub', exc)
            return await self._stub.simulation_turn(history, user_message, role, goal_es, cefr_level, native_language)

    async def translate(self, text: str, target_language: str, source_language: str = 'ru') -> str:
        """Translate explanatory text (cached). On any provider failure, returns the
        source text unchanged via the stub so callers always get usable content."""
        result = await self._run(
            'translate',
            {'text': text, 'target': target_language, 'source': source_language},
            lambda p: p.translate(text=text, target_language=target_language, source_language=source_language),
            lambda p: p.translate(text=text, target_language=target_language, source_language=source_language),
        )
        return result if isinstance(result, str) else text
