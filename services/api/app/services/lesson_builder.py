"""The core commercial loop: any text -> a personalized lesson.

Runs the live AI gateway (analyze + flashcards + exercises), persists a Lesson plus
a FlashcardDeck/Flashcards and a TextAnalysis row, and returns a structured payload.
Token usage across all three calls is accumulated so the route can meter UsageCounter.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from sqlalchemy.orm import Session

from app.agents.orchestrator import AgentOrchestrator
from app.core.config import get_settings
from app.models.course import Lesson
from app.models.flashcard import Flashcard, FlashcardDeck
from app.models.upload import TextAnalysis
from app.models.user import User

settings = get_settings()


@dataclass
class BuildResult:
    lesson_id: str
    deck_id: str | None
    title: str
    analysis: dict
    cards: list[dict]
    exercises: list[dict]
    usage: dict = field(default_factory=lambda: {'input_tokens': 0, 'output_tokens': 0, 'ai_calls': 0})


async def build_lesson_from_text(
    db: Session,
    user: User,
    text: str,
    native_language: str = 'ru',
    cefr_level: str = 'A1',
    source_type: str = 'raw_text',
    source_id=None,
    title: str | None = None,
) -> BuildResult:
    text = (text or '').strip()[: settings.max_lesson_input_chars]
    orchestrator = AgentOrchestrator()
    usage = {'input_tokens': 0, 'output_tokens': 0, 'ai_calls': 0}

    def _acc():
        u = orchestrator.ai.last_usage or {}
        usage['input_tokens'] += int(u.get('input_tokens', 0))
        usage['output_tokens'] += int(u.get('output_tokens', 0))
        usage['ai_calls'] += 1

    analysis = await orchestrator.analyze_text(text=text, native_language=native_language); _acc()
    cefr = analysis.get('cefr_estimate') or cefr_level

    flash = await orchestrator.generate_flashcards(text=text, native_language=native_language, cefr_level=cefr); _acc()
    ex = await orchestrator.generate_exercises(text=text, cefr_level=cefr, native_language=native_language); _acc()

    cards = flash.get('cards', []) or []
    exercises = ex.get('exercises', []) or []
    lesson_title = title or flash.get('deck_title') or f'Lesson ({cefr})'

    # Persist TextAnalysis
    ta = TextAnalysis(
        user_id=user.id, source_type=source_type, source_id=source_id, cefr_estimate=cefr,
        verbs_json=analysis.get('verbs'), tenses_json=analysis.get('tenses'), nouns_json=analysis.get('nouns'),
        adjectives_json=analysis.get('adjectives'), adverbs_json=analysis.get('adverbs'),
        conjunctions_json=analysis.get('conjunctions'), vocabulary_json=analysis.get('vocabulary'),
        grammar_topics_json=analysis.get('grammar_topics'),
    )
    db.add(ta)

    # Persist a flashcard deck + cards
    deck = FlashcardDeck(user_id=user.id, title=lesson_title, source_type=source_type, source_id=source_id, cefr_level=cefr)
    db.add(deck)
    db.flush()
    for c in cards[:50]:
        db.add(Flashcard(
            deck_id=deck.id, user_id=user.id,
            front=str(c.get('front', ''))[:2000], back=str(c.get('back', ''))[:2000],
            card_type=c.get('card_type', 'word_translation'),
            example_sentence=(c.get('example_sentence') or None),
        ))

    # Persist the generated Lesson (content embeds analysis + cards + exercises)
    lesson = Lesson(
        module_id=None, title=lesson_title, description=analysis.get('summary', '')[:500],
        cefr_level=cefr, native_language=native_language, lesson_type='generated',
        content_json={
            'source_excerpt': text[:1500],
            'analysis': analysis,
            'flashcards': cards,
            'exercises': exercises,
            'deck_id': str(deck.id),
        },
    )
    db.add(lesson)
    db.flush()

    return BuildResult(
        lesson_id=str(lesson.id), deck_id=str(deck.id), title=lesson_title,
        analysis=analysis, cards=cards, exercises=exercises, usage=usage,
    )
