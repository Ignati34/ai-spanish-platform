import uuid
from datetime import datetime
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from app.db.session import Base
from app.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin


class License(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'licenses'
    organization_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), nullable=True)
    license_key_hash: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    edition: Mapped[str] = mapped_column(String(80), default='self_hosted_basic')
    max_users: Mapped[int] = mapped_column(Integer, default=10)
    max_ai_requests: Mapped[int] = mapped_column(Integer, default=1000)
    valid_from: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    valid_until: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default='active')
    activation_limit: Mapped[int] = mapped_column(Integer, default=1)


class LicenseActivation(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'license_activations'
    license_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('licenses.id', ondelete='CASCADE'))
    instance_id: Mapped[str] = mapped_column(String(255), nullable=False)
    domain: Mapped[str | None] = mapped_column(String(255), nullable=True)
    hardware_fingerprint_hash: Mapped[str | None] = mapped_column(String(255), nullable=True)
    activated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    last_check_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    status: Mapped[str] = mapped_column(String(50), default='active')
