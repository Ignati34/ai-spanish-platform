import uuid
from sqlalchemy import String, Text, ForeignKey, Integer, JSON, Float
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base
from app.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin


class UploadedFile(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'uploaded_files'
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    original_filename: Mapped[str] = mapped_column(String(255), nullable=False)
    file_type: Mapped[str] = mapped_column(String(50), nullable=False)
    mime_type: Mapped[str | None] = mapped_column(String(120), nullable=True)
    storage_url: Mapped[str] = mapped_column(Text, nullable=False)
    file_size: Mapped[int] = mapped_column(Integer, default=0)
    processing_status: Mapped[str] = mapped_column(String(50), default='uploaded')


class ExtractedText(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'extracted_texts'
    file_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('uploaded_files.id'), nullable=True)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    language: Mapped[str] = mapped_column(String(16), default='es')
    text: Mapped[str] = mapped_column(Text, nullable=False)
    metadata_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)


class Transcript(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'transcripts'
    file_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('uploaded_files.id'), nullable=True)
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    language: Mapped[str] = mapped_column(String(16), default='es')
    transcript_text: Mapped[str] = mapped_column(Text, nullable=False)
    duration_seconds: Mapped[float | None] = mapped_column(Float, nullable=True)
    segments_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    status: Mapped[str] = mapped_column(String(50), default='completed')


class TextAnalysis(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'text_analyses'
    user_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), nullable=True)
    source_type: Mapped[str] = mapped_column(String(50), default='raw_text')
    source_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)
    cefr_estimate: Mapped[str] = mapped_column(String(8), default='A1')
    verbs_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    tenses_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    nouns_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    adjectives_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    adverbs_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    conjunctions_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    vocabulary_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    grammar_topics_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
