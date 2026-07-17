from pydantic import BaseModel


class GenerateFlashcardsRequest(BaseModel):
    text: str
    native_language: str = 'ru'
    cefr_level: str = 'A1'
    source_language: str = 'es'


class FlashcardOut(BaseModel):
    front: str
    back: str
    card_type: str = 'word_translation'
    example_sentence: str | None = None


class GenerateFlashcardsResponse(BaseModel):
    deck_title: str
    cards: list[FlashcardOut]
