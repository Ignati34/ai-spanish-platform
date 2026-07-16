import uuid
from sqlalchemy import String, Text, ForeignKey, JSON, Float, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base
from app.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin


class Exercise(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'exercises'
    user_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=True)
    lesson_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('lessons.id', ondelete='CASCADE'), nullable=True)
    source_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    source_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)
    exercise_type: Mapped[str] = mapped_column(String(50), nullable=False)
    prompt: Mapped[str] = mapped_column(Text, nullable=False)
    options_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    correct_answer_json: Mapped[dict | list | str | None] = mapped_column(JSON, nullable=True)
    explanation: Mapped[str | None] = mapped_column(Text, nullable=True)
    cefr_level: Mapped[str] = mapped_column(String(8), default='A1')


class ExerciseSubmission(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'exercise_submissions'
    exercise_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('exercises.id', ondelete='CASCADE'))
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    answer_json: Mapped[dict | list | str | None] = mapped_column(JSON, nullable=True)
    is_correct: Mapped[bool] = mapped_column(Boolean, default=False)
    score: Mapped[float] = mapped_column(Float, default=0)
    feedback: Mapped[str | None] = mapped_column(Text, nullable=True)
