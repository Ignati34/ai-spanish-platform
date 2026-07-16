import uuid
from datetime import date
from sqlalchemy import Integer, Boolean, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base
from app.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin


class MotivationState(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'motivation_state'
    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), unique=True, index=True)
    daily_goal: Mapped[int] = mapped_column(Integer, default=20)          # reviews/day
    today_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    today_count: Mapped[int] = mapped_column(Integer, default=0)
    current_streak: Mapped[int] = mapped_column(Integer, default=0)
    longest_streak: Mapped[int] = mapped_column(Integer, default=0)
    last_goal_date: Mapped[date | None] = mapped_column(Date, nullable=True)
    reminders_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    reminder_hour: Mapped[int] = mapped_column(Integer, default=19)       # local hour 0-23
    last_reminded_date: Mapped[date | None] = mapped_column(Date, nullable=True)
