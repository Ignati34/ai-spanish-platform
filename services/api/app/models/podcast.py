import uuid
from sqlalchemy import String, Text, ForeignKey, Float, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base
from app.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin


class Podcast(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'podcasts'
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'))
    source_file_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('uploaded_files.id'), nullable=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    cefr_level: Mapped[str] = mapped_column(String(8), default='A1')
    status: Mapped[str] = mapped_column(String(50), default='created')


class PodcastSegment(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'podcast_segments'
    podcast_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('podcasts.id', ondelete='CASCADE'))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    start_time: Mapped[float] = mapped_column(Float, default=0)
    end_time: Mapped[float] = mapped_column(Float, default=0)
    audio_url: Mapped[str | None] = mapped_column(Text, nullable=True)
    transcript: Mapped[str | None] = mapped_column(Text, nullable=True)
    translation: Mapped[str | None] = mapped_column(Text, nullable=True)
    vocabulary_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    grammar_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
    quiz_json: Mapped[dict | list | None] = mapped_column(JSON, nullable=True)
