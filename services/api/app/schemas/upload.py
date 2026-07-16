from pydantic import BaseModel, Field


class UploadOut(BaseModel):
    id: str
    filename: str
    status: str


class BuildFromTextRequest(BaseModel):
    text: str = Field(min_length=1)
    native_language: str = 'ru'
    cefr_level: str = 'A1'
    title: str | None = None


class GeneratedLessonOut(BaseModel):
    lesson_id: str
    deck_id: str | None = None
    title: str
    cefr_estimate: str
    summary: str = ''
    analysis: dict
    cards: list[dict]
    exercises: list[dict]
    source: str = 'raw_text'
    filename: str | None = None
    transcript: str | None = None
    duration_seconds: float | None = None
