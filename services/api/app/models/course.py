import uuid
from datetime import datetime
from sqlalchemy import String, Text, ForeignKey, Integer, DateTime, JSON, Float, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base
from app.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin


class CEFRLevel(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'cefr_levels'
    code: Mapped[str] = mapped_column(String(8), unique=True, nullable=False)
    title: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    sort_order: Mapped[int] = mapped_column(Integer, default=0)


class CourseModule(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'course_modules'
    cefr_level_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('cefr_levels.id'))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    sort_order: Mapped[int] = mapped_column(Integer, default=0)


class Lesson(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'lessons'
    module_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('course_modules.id'), nullable=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    cefr_level: Mapped[str] = mapped_column(String(8), default='A1')
    native_language: Mapped[str] = mapped_column(String(16), default='ru')
    lesson_type: Mapped[str] = mapped_column(String(50), default='course')
    content_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    image_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)
    audio_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default='published')


class LessonProgress(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'lesson_progress'
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    lesson_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('lessons.id', ondelete='CASCADE'))
    status: Mapped[str] = mapped_column(String(50), default='not_started')
    score: Mapped[float | None] = mapped_column(Float, nullable=True)


class LessonTranslation(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """Cached translation of a lesson's theory into a target language.

    Filled lazily on first request and reused thereafter so we don't re-spend
    tokens. `source_hash` lets us invalidate when the source theory changes.
    """
    __tablename__ = 'lesson_translations'
    lesson_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('lessons.id', ondelete='CASCADE'), index=True)
    language: Mapped[str] = mapped_column(String(16), index=True)
    theory: Mapped[str] = mapped_column(Text)
    source_hash: Mapped[str] = mapped_column(String(64))

    __table_args__ = (UniqueConstraint('lesson_id', 'language', name='uq_lesson_translation'),)
    started_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    completed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class ReadingResource(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    """A reading-library entry: either a built-in graded text (kind='text', with body)
    or a curated external link (kind='link', with url)."""
    __tablename__ = 'reading_resources'
    kind: Mapped[str] = mapped_column(String(16), index=True, default='text')  # 'text' | 'link'
    level: Mapped[str | None] = mapped_column(String(8), nullable=True, index=True)
    title: Mapped[str] = mapped_column(String(300))
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    body: Mapped[str | None] = mapped_column(Text, nullable=True)          # for kind='text'
    url: Mapped[str | None] = mapped_column(String(500), nullable=True)     # for kind='link'
    category: Mapped[str | None] = mapped_column(String(40), nullable=True)
    language: Mapped[str] = mapped_column(String(8), default='es')
    downloadable: Mapped[bool] = mapped_column(default=True)
