from pydantic import BaseModel, Field


class TextAnalyzeRequest(BaseModel):
    text: str = Field(min_length=1)
    native_language: str = 'ru'
    target_language: str = 'es'


class TextAnalyzeResponse(BaseModel):
    cefr_estimate: str
    verbs: list[dict]
    tenses: list[str]
    nouns: list[str]
    adjectives: list[str]
    adverbs: list[str]
    conjunctions: list[str]
    vocabulary: list[dict]
    grammar_topics: list[str]
    summary: str
