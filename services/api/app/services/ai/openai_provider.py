"""OpenAI-compatible chat provider (async).

Works with the OpenAI API or any compatible endpoint via AI_BASE_URL. Requests a
JSON object response, parses it defensively, and reports token usage.
"""
from __future__ import annotations

import json

import httpx

from app.core.config import get_settings
from app.services.ai import prompts
from app.services.ai.base import BaseAIProvider

settings = get_settings()


def _parse_json(content: str) -> dict:
    content = (content or '').strip()
    if content.startswith('```'):
        # strip ```json ... ``` fences defensively
        content = content.strip('`')
        if content.lower().startswith('json'):
            content = content[4:]
        content = content.strip()
    start, end = content.find('{'), content.rfind('}')
    if start != -1 and end != -1:
        content = content[start:end + 1]
    return json.loads(content)


class OpenAIProvider(BaseAIProvider):
    name = 'openai'

    async def _chat_json(self, system: str, user: str) -> dict:
        headers = {'Authorization': f'Bearer {settings.ai_api_key}', 'Content-Type': 'application/json'}
        body = {
            'model': settings.ai_model,
            'temperature': settings.ai_temperature,
            'max_tokens': settings.ai_max_tokens,
            'response_format': {'type': 'json_object'},
            'messages': [
                {'role': 'system', 'content': system},
                {'role': 'user', 'content': user},
            ],
        }
        async with httpx.AsyncClient(timeout=settings.ai_timeout_seconds) as client:
            resp = await client.post(f'{settings.ai_base_url}/chat/completions', headers=headers, json=body)
            resp.raise_for_status()
            data = resp.json()
        usage = data.get('usage', {}) or {}
        self.last_usage = {
            'input_tokens': int(usage.get('prompt_tokens', 0)),
            'output_tokens': int(usage.get('completion_tokens', 0)),
        }
        content = data['choices'][0]['message']['content']
        return _parse_json(content)

    async def analyze_text(self, text: str, native_language: str = 'ru') -> dict:
        system, user = prompts.analyze(text, native_language)
        data = await self._chat_json(system, user)
        data.setdefault('adjectives', [])
        data.setdefault('adverbs', [])
        data.setdefault('conjunctions', [])
        data.setdefault('summary', '')
        return data

    async def generate_flashcards(self, text: str, native_language: str = 'ru', cefr_level: str = 'A1') -> dict:
        system, user = prompts.flashcards(text, native_language, cefr_level)
        data = await self._chat_json(system, user)
        data.setdefault('deck_title', f'{cefr_level} deck')
        data.setdefault('cards', [])
        return data

    async def generate_exercises(self, text: str, cefr_level: str = 'A1', native_language: str = 'ru') -> dict:
        system, user = prompts.exercises(text, native_language, cefr_level)
        data = await self._chat_json(system, user)
        data.setdefault('exercises', [])
        return data

    async def check_answer(self, answer: str, correct_answer: str | None = None) -> dict:
        system, user = prompts.check(answer, correct_answer, 'ru')
        data = await self._chat_json(system, user)
        data.setdefault('is_correct', False)
        data.setdefault('score', 0.0)
        data.setdefault('feedback', '')
        return data

    async def transcribe(self, data: bytes, filename: str, language: str = 'es') -> dict:
        headers = {'Authorization': f'Bearer {settings.ai_api_key}'}
        files = {'file': (filename or 'audio.mp3', data, 'application/octet-stream')}
        # Only whisper-1 supports verbose_json (segments + duration); the newer
        # gpt-4o-*-transcribe models only accept json/text and 400 on verbose_json.
        supports_verbose = 'whisper' in (settings.stt_model or '').lower()
        form = {'model': settings.stt_model, 'response_format': 'verbose_json' if supports_verbose else 'json'}
        if language:
            form['language'] = language[:2]
        async with httpx.AsyncClient(timeout=settings.ai_timeout_seconds) as client:
            resp = await client.post(f'{settings.ai_base_url}/audio/transcriptions', headers=headers, files=files, data=form)
            resp.raise_for_status()
            body = resp.json()
        return {
            'text': body.get('text', ''),
            'duration_seconds': float(body.get('duration', 0.0) or 0.0),
            'segments': body.get('segments', []) or [],
            'language': body.get('language', language),
        }

    async def voice_reply(self, history, user_message, scenario='restaurant', cefr_level='A1', native_language='ru') -> dict:
        system, user = prompts.voice_reply(history, user_message, scenario, cefr_level, native_language)
        data = await self._chat_json(system, user)
        data.setdefault('reply_es', '')
        data.setdefault('correction', '')
        data.setdefault('score', 0.0)
        return data

    async def synthesize(self, text: str, voice: str | None = None, language: str = 'es') -> bytes:
        headers = {'Authorization': f'Bearer {settings.ai_api_key}', 'Content-Type': 'application/json'}
        body = {
            'model': settings.tts_model,
            'voice': voice or settings.tts_voice,
            'input': text,
            'response_format': settings.tts_format,
        }
        async with httpx.AsyncClient(timeout=settings.ai_timeout_seconds) as client:
            resp = await client.post(f'{settings.ai_base_url}/audio/speech', headers=headers, json=body)
            resp.raise_for_status()
            return resp.content

    async def assess_level(self, writing_sample: str, speaking_sample: str, mc_summary: dict, native_language: str = 'ru') -> dict:
        system, user = prompts.assess_level(writing_sample, speaking_sample, mc_summary, native_language)
        data = await self._chat_json(system, user)
        data.setdefault('cefr_estimate', 'A1')
        data.setdefault('recommended_level', data.get('cefr_estimate', 'A1'))
        data.setdefault('strengths', [])
        data.setdefault('gaps', [])
        data.setdefault('summary', '')
        data.setdefault('study_plan', [])
        return data

    async def targeted_exercises(self, topics, cefr_level='A1', native_language='ru') -> dict:
        system, user = prompts.targeted_exercises(list(topics or []), cefr_level, native_language)
        data = await self._chat_json(system, user)
        data.setdefault('vocabulary', [])
        data.setdefault('exercises', [])
        return data

    async def simulation_turn(self, history, user_message, role='', goal_es='', cefr_level='A1', native_language='ru') -> dict:
        system, user = prompts.simulation_turn(history, user_message, role, goal_es, cefr_level, native_language)
        data = await self._chat_json(system, user)
        data.setdefault('reply_es', '')
        data.setdefault('correction', '')
        data.setdefault('score', 0.0)
        data.setdefault('goal_met', False)
        data.setdefault('hint', '')
        return data
