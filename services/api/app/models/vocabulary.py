import uuid
from datetime import datetime
from sqlalchemy import String, Text, ForeignKey, Float, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base
from app.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin


class VocabularyItem(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'vocabulary_items'
    lemma: Mapped[str] = mapped_column(String(255), index=True)
    word: Mapped[str] = mapped_column(String(255), index=True)
    language: Mapped[str] = mapped_column(String(16), default='es')
    part_of_speech: Mapped[str | None] = mapped_column(String(50), nullable=True)
    cefr_level: Mapped[str] = mapped_column(String(8), default='A1')
    translation_ru: Mapped[str | None] = mapped_column(Text, nullable=True)
    translation_uk: Mapped[str | None] = mapped_column(Text, nullable=True)
    translation_ar: Mapped[str | None] = mapped_column(Text, nullable=True)
    translation_fr: Mapped[str | None] = mapped_column(Text, nullable=True)
    translation_zh: Mapped[str | None] = mapped_column(Text, nullable=True)
    translation_ja: Mapped[str | None] = mapped_column(Text, nullable=True)
    examples_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)


class UserVocabulary(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'user_vocabulary'
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    vocabulary_item_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('vocabulary_items.id', ondelete='CASCADE'))
    source_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    source_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default='learning')
    mastery_score: Mapped[float] = mapped_column(Float, default=0)
    last_seen_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class UserMistake(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'user_mistakes'
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    mistake_type: Mapped[str] = mapped_column(String(80), default='grammar')
    original_text: Mapped[str] = mapped_column(Text, nullable=False)
    corrected_text: Mapped[str] = mapped_column(Text, nullable=False)
    explanation: Mapped[str | None] = mapped_column(Text, nullable=True)
    grammar_topic: Mapped[str | None] = mapped_column(String(120), nullable=True)
    source_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    source_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)
