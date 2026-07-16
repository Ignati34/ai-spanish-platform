import uuid
from sqlalchemy import String, Boolean, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base
from app.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin


class User(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'users'

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    telegram_id: Mapped[str | None] = mapped_column(String(128), unique=True, nullable=True)
    native_language: Mapped[str] = mapped_column(String(16), default='ru')
    interface_language: Mapped[str] = mapped_column(String(16), default='ru')
    target_language: Mapped[str] = mapped_column(String(16), default='es')
    role: Mapped[str] = mapped_column(String(32), default='student')
    status: Mapped[str] = mapped_column(String(32), default='active')
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    profile: Mapped['UserProfile'] = relationship(back_populates='user', cascade='all, delete-orphan')


class UserProfile(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'user_profiles'

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), unique=True)
    first_name: Mapped[str | None] = mapped_column(String(120), nullable=True)
    country: Mapped[str | None] = mapped_column(String(120), nullable=True)
    timezone: Mapped[str] = mapped_column(String(80), default='Europe/Madrid')
    learning_goal: Mapped[str | None] = mapped_column(String(120), nullable=True)
    current_cefr_level: Mapped[str] = mapped_column(String(8), default='A1')
    preferred_voice: Mapped[str | None] = mapped_column(String(80), nullable=True)
    daily_goal_minutes: Mapped[int] = mapped_column(Integer, default=20)

    user: Mapped[User] = relationship(back_populates='profile')
