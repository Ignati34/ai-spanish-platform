"""Common interface for AI providers used by the gateway.

Each provider implements the four learning tasks and reports token usage via
`last_usage`, so the gateway can enforce quotas and record UsageCounter.
"""
from __future__ import annotations


class BaseAIProvider:
    name = 'base'

    def __init__(self) -> None:
        self.last_usage: dict[str, int] = {'input_tokens': 0, 'output_tokens': 0}

    async def analyze_text(self, text: str, native_language: str = 'ru') -> dict:
        raise NotImplementedError

    async def generate_flashcards(self, text: str, native_language: str = 'ru', cefr_level: str = 'A1') -> dict:
        raise NotImplementedError

    async def generate_exercises(self, text: str, cefr_level: str = 'A1', native_language: str = 'ru') -> dict:
        raise NotImplementedError

    async def check_answer(self, answer: str, correct_answer: str | None = None) -> dict:
        raise NotImplementedError

    async def transcribe(self, data: bytes, filename: str, language: str = 'es') -> dict:
        """Speech-to-text. Returns {text, duration_seconds, segments, language}."""
        raise NotImplementedError

    async def voice_reply(self, history: list[dict], user_message: str, scenario: str, cefr_level: str, native_language: str) -> dict:
        raise NotImplementedError

    async def synthesize(self, text: str, voice: str | None = None, language: str = 'es') -> bytes:
        """Text-to-speech. Returns audio bytes (empty if unavailable)."""
        raise NotImplementedError

    async def assess_level(self, writing_sample: str, speaking_sample: str, mc_summary: dict, native_language: str = 'ru') -> dict:
        raise NotImplementedError

    async def targeted_exercises(self, topics: list, cefr_level: str = 'A1', native_language: str = 'ru') -> dict:
        raise NotImplementedError

    async def simulation_turn(self, history: list, user_message: str, role: str, goal_es: str, cefr_level: str = 'A1', native_language: str = 'ru') -> dict:
        raise NotImplementedError
