import uuid
from datetime import datetime
from sqlalchemy import String, Text, ForeignKey, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base
from app.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin


class VoiceSession(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'voice_sessions'
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    scenario: Mapped[str] = mapped_column(String(120), default='restaurant')
    cefr_level: Mapped[str] = mapped_column(String(8), default='A1')
    native_language: Mapped[str] = mapped_column(String(16), default='ru')
    status: Mapped[str] = mapped_column(String(50), default='active')
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    ended_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class VoiceMessage(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'voice_messages'
    session_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('voice_sessions.id', ondelete='CASCADE'))
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    role: Mapped[str] = mapped_column(String(20), default='user')
    audio_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    transcript: Mapped[str | None] = mapped_column(Text, nullable=True)
    feedback_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
