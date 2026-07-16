import uuid
from sqlalchemy import String, Text, Float, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base
from app.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin


class DiagnosticResult(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'diagnostic_results'
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), index=True)
    native_language: Mapped[str] = mapped_column(String(16), default='ru')
    cefr_estimate: Mapped[str] = mapped_column(String(8), default='A1')
    recommended_level: Mapped[str] = mapped_column(String(8), default='A1')
    mc_score: Mapped[float] = mapped_column(Float, default=0.0)
    strengths_json: Mapped[list | dict | None] = mapped_column(JSON, nullable=True)
    gaps_json: Mapped[list | dict | None] = mapped_column(JSON, nullable=True)
    plan_json: Mapped[list | dict | None] = mapped_column(JSON, nullable=True)
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    writing_sample: Mapped[str | None] = mapped_column(Text, nullable=True)
    speaking_sample: Mapped[str | None] = mapped_column(Text, nullable=True)
