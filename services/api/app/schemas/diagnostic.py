from pydantic import BaseModel, Field


class DiagnosticAnswer(BaseModel):
    id: str
    answer: int | str | None = None


class DiagnosticSubmitRequest(BaseModel):
    answers: list[DiagnosticAnswer] = Field(default_factory=list)
    writing_sample: str = ''
    speaking_sample: str = ''
    native_language: str = 'ru'


class DiagnosticResultOut(BaseModel):
    cefr_estimate: str
    recommended_level: str
    mc_correct: int
    mc_total: int
    mc_ratio: float
    strengths: list[str]
    gaps: list[str]
    summary: str
    study_plan: list[str]
