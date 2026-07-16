import uuid
from pydantic import BaseModel


class GenerateExercisesRequest(BaseModel):
    text: str
    cefr_level: str = 'A1'
    native_language: str = 'ru'


class ExerciseOut(BaseModel):
    id: str | None = None
    exercise_type: str
    prompt: str
    options: list[str] | None = None
    correct_answer: str | None = None
    explanation: str | None = None


class GenerateExercisesResponse(BaseModel):
    exercises: list[ExerciseOut]


class SubmitExerciseRequest(BaseModel):
    answer: str


class SubmitExerciseResponse(BaseModel):
    is_correct: bool
    score: float
    feedback: str
