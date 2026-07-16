"""Deterministic, offline provider. Keeps the platform fully runnable without any
API key (AI_PROVIDER=stub). Same behavior the MVP scaffold shipped with."""
from __future__ import annotations

from app.services.ai.base import BaseAIProvider

_VERB_HINTS = {'soy', 'eres', 'es', 'somos', 'son', 'estoy', 'está', 'tengo', 'quiero', 'fui', 'compré', 'quería'}


class StubProvider(BaseAIProvider):
    name = 'stub'

    async def analyze_text(self, text: str, native_language: str = 'ru') -> dict:
        words = [w.strip('.,!?¿¡;:()"').lower() for w in text.split() if w.strip()]
        verbs = [w for w in words if w.endswith(('ar', 'er', 'ir')) or w in _VERB_HINTS]
        nouns = [w for w in words if len(w) > 4 and w not in verbs][:10]
        vocabulary = [{'word': w, 'translation': 'demo translation', 'cefr': 'A1'} for w in sorted(set(words))[:10]]
        return {
            'cefr_estimate': 'A1',
            'verbs': [{'word': v, 'tense': 'present/infinitive'} for v in verbs[:10]],
            'tenses': ['presente de indicativo'],
            'nouns': nouns,
            'adjectives': [],
            'adverbs': [],
            'conjunctions': [w for w in words if w in {'y', 'pero', 'porque'}],
            'vocabulary': vocabulary,
            'grammar_topics': ['presente de indicativo', 'artículos', 'ser/estar'],
            'summary': 'Demo analysis. Set AI_PROVIDER=openai and AI_API_KEY to use a real model.',
        }

    async def generate_flashcards(self, text: str, native_language: str = 'ru', cefr_level: str = 'A1') -> dict:
        words: list[str] = []
        for raw in text.split():
            word = raw.strip('.,!?¿¡;:()"').lower()
            if word and word not in words:
                words.append(word)
        cards = [
            {'front': w, 'back': 'demo translation', 'card_type': 'word_translation', 'example_sentence': f'Ejemplo con {w}.'}
            for w in words[:10]
        ]
        return {'deck_title': f'Generated {cefr_level} deck', 'cards': cards}

    async def generate_exercises(self, text: str, cefr_level: str = 'A1', native_language: str = 'ru') -> dict:
        return {
            'exercises': [
                {'exercise_type': 'multiple_choice', 'prompt': '¿Qué significa "hola"?',
                 'options': ['привет', 'спасибо', 'дом', 'работа'], 'correct_answer': 'привет',
                 'explanation': 'Hola means привет/здравствуйте.'},
                {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ estudiante.',
                 'options': ['soy', 'eres', 'son'], 'correct_answer': 'soy', 'explanation': 'For yo, use soy.'},
            ]
        }

    async def check_answer(self, answer: str, correct_answer: str | None = None) -> dict:
        is_correct = bool(correct_answer and answer.strip().lower() == correct_answer.strip().lower())
        return {
            'is_correct': is_correct,
            'score': 1.0 if is_correct else 0.0,
            'feedback': 'Correct.' if is_correct else f'Expected answer: {correct_answer}',
        }

    async def transcribe(self, data: bytes, filename: str, language: str = 'es') -> dict:
        # Deterministic placeholder so the audio->lesson pipeline runs without a key.
        return {
            'text': 'Hola, me llamo Ana y vivo en Madrid. Ayer fui al mercado y compré pan y fruta.',
            'duration_seconds': 0.0,
            'segments': [],
            'language': language,
            'stub': True,
        }

    async def voice_reply(self, history, user_message, scenario='restaurant', cefr_level='A1', native_language='ru') -> dict:
        return {
            'reply_es': '¡Muy bien! ¿Puedes contarme un poco más, por favor?',
            'correction': '',
            'score': 0.7,
            'stub': True,
        }

    async def synthesize(self, text: str, voice: str | None = None, language: str = 'es') -> bytes:
        # No audio without a real provider; the route falls back to text-only.
        return b''

    async def assess_level(self, writing_sample: str, speaking_sample: str, mc_summary: dict, native_language: str = 'ru') -> dict:
        ratio = float((mc_summary or {}).get('ratio', 0.0))
        level = 'A1'
        for threshold, lvl in [(0.25, 'A1'), (0.45, 'A2'), (0.65, 'B1'), (0.82, 'B2'), (1.01, 'C1')]:
            if ratio < threshold:
                level = lvl
                break
        return {
            'cefr_estimate': level,
            'recommended_level': level,
            'strengths': ['Basic vocabulary'],
            'gaps': ['Verb tenses', 'ser/estar'],
            'summary': 'Demo assessment. Set AI_PROVIDER=openai for a real CEFR evaluation.',
            'study_plan': [f'Start at {level}', 'Review ser vs estar', 'Practice past tenses', 'Daily flashcards'],
            'stub': True,
        }

    async def targeted_exercises(self, topics, cefr_level='A1', native_language='ru') -> dict:
        topic = (topics or ['grammar'])[0]
        return {'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': f'[{topic}] Yo ___ estudiante.', 'options': ['soy', 'estoy', 'es'],
             'correct_answer': 'soy', 'explanation': f'Practice for {topic}.'},
            {'exercise_type': 'multiple_choice', 'prompt': f'[{topic}] Elige la forma correcta.', 'options': ['fui', 'era', 'voy'],
             'correct_answer': 'fui', 'explanation': f'Targeted at {topic}.'},
        ]}
