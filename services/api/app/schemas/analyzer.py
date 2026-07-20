from pydantic import BaseModel, Field


class TextAnalyzeRequest(BaseModel):
    text: str = Field(min_length=1)
    native_language: str = 'ru'
    target_language: str = 'es'


class TextAnalyzeResponse(BaseModel):
    cefr_estimate: str = 'A1'
    translation: str = ''            # full translation of the text into the native language
    verbs: list = []                 # [{word, tense, translation}]
    tenses: list[str] = []           # canonical Spanish tense names
    tense_info: list = []            # [{name, explanation, examples[]}] localized (added by route)
    nouns: list = []                 # [{word, translation}]
    adjectives: list = []            # [{word, translation}]
    adverbs: list = []               # [{word, translation}]
    conjunctions: list = []
    vocabulary: list = []            # [{word, translation, cefr}]
    grammar_topics: list[str] = []
    summary: str = ''
