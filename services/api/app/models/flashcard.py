import uuid
from datetime import datetime
from sqlalchemy import String, Text, ForeignKey, Integer, Float, DateTime, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base
from app.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin


class FlashcardDeck(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'flashcard_decks'
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    source_type: Mapped[str | None] = mapped_column(String(50), nullable=True)
    source_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)
    cefr_level: Mapped[str] = mapped_column(String(8), default='A1')


class Flashcard(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'flashcards'
    deck_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('flashcard_decks.id', ondelete='CASCADE'))
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    front: Mapped[str] = mapped_column(Text, nullable=False)
    back: Mapped[str] = mapped_column(Text, nullable=False)
    card_type: Mapped[str] = mapped_column(String(50), default='word_translation')
    example_sentence: Mapped[str | None] = mapped_column(Text, nullable=True)
    audio_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    image_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    metadata_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)


class FlashcardReview(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'flashcard_reviews'
    flashcard_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('flashcards.id', ondelete='CASCADE'))
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    quality_score: Mapped[int] = mapped_column(Integer, default=3)
    next_review_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    interval_days: Mapped[int] = mapped_column(Integer, default=0)
    ease_factor: Mapped[float] = mapped_column(Float, default=2.5)
    repetitions: Mapped[int] = mapped_column(Integer, default=0)
    reviewed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
