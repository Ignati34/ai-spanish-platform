import uuid
from datetime import datetime
from sqlalchemy import String, Integer, Numeric, ForeignKey, DateTime, Boolean, JSON, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.session import Base
from app.models.mixins import UUIDPrimaryKeyMixin, TimestampMixin


class Plan(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'plans'

    code: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String(120), nullable=False)
    description: Mapped[str | None] = mapped_column(String(255), nullable=True)
    provider_product_id: Mapped[str | None] = mapped_column(String(255), nullable=True)
    provider_price_id_monthly: Mapped[str | None] = mapped_column(String(255), nullable=True)
    provider_price_id_yearly: Mapped[str | None] = mapped_column(String(255), nullable=True)
    price_monthly: Mapped[float] = mapped_column(Numeric(10, 2), default=0)
    price_yearly: Mapped[float] = mapped_column(Numeric(10, 2), default=0)
    currency: Mapped[str] = mapped_column(String(8), default='eur')
    max_ai_requests_per_month: Mapped[int] = mapped_column(Integer, default=100)
    max_transcription_minutes: Mapped[int] = mapped_column(Integer, default=0)
    max_storage_mb: Mapped[int] = mapped_column(Integer, default=100)
    max_generated_images: Mapped[int] = mapped_column(Integer, default=3)
    voice_tutor_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    podcast_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    video_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    image_generation_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    features_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    limits_json: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)


class BillingCustomer(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'billing_customers'

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), index=True)
    provider: Mapped[str] = mapped_column(String(50), default='stripe')
    provider_customer_id: Mapped[str] = mapped_column(String(255), index=True)
    email: Mapped[str | None] = mapped_column(String(255), nullable=True)

    __table_args__ = (UniqueConstraint('provider', 'provider_customer_id', name='uq_billing_customer_provider_id'),)


class Subscription(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'subscriptions'

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), index=True)
    plan_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('plans.id'))
    provider: Mapped[str] = mapped_column(String(50), default='stripe')
    provider_customer_id: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
    provider_subscription_id: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
    status: Mapped[str] = mapped_column(String(50), default='active', index=True)
    current_period_start: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    current_period_end: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    trial_end: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    cancel_at_period_end: Mapped[bool] = mapped_column(Boolean, default=False)

    plan: Mapped['Plan'] = relationship()


class Invoice(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'invoices'

    user_id: Mapped[uuid.UUID | None] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='SET NULL'), nullable=True, index=True)
    provider_invoice_id: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    provider_customer_id: Mapped[str | None] = mapped_column(String(255), nullable=True, index=True)
    amount_due: Mapped[int] = mapped_column(Integer, default=0)
    amount_paid: Mapped[int] = mapped_column(Integer, default=0)
    currency: Mapped[str] = mapped_column(String(8), default='eur')
    status: Mapped[str] = mapped_column(String(50), default='draft')
    invoice_pdf_url: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    hosted_invoice_url: Mapped[str | None] = mapped_column(String(1000), nullable=True)


class PaymentEvent(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'payment_events'

    provider: Mapped[str] = mapped_column(String(50), default='stripe')
    event_id: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    event_type: Mapped[str] = mapped_column(String(255), index=True)
    payload_json: Mapped[dict] = mapped_column(JSON)
    processing_status: Mapped[str] = mapped_column(String(50), default='received')
    processed_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    error_message: Mapped[str | None] = mapped_column(String(1000), nullable=True)


class UserEntitlement(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'user_entitlements'

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), unique=True, index=True)
    plan_code: Mapped[str] = mapped_column(String(50), default='free')
    source: Mapped[str] = mapped_column(String(50), default='system')
    voice_tutor_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    podcast_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    image_generation_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    video_upload_enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    max_ai_requests_month: Mapped[int] = mapped_column(Integer, default=100)
    max_transcription_minutes_month: Mapped[int] = mapped_column(Integer, default=0)
    max_generated_images_month: Mapped[int] = mapped_column(Integer, default=3)
    max_storage_mb: Mapped[int] = mapped_column(Integer, default=100)
    valid_until: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class UsageCounter(Base, UUIDPrimaryKeyMixin, TimestampMixin):
    __tablename__ = 'usage_counters'

    user_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), ForeignKey('users.id', ondelete='CASCADE'), index=True)
    period_start: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    period_end: Mapped[datetime] = mapped_column(DateTime(timezone=True), index=True)
    ai_requests_used: Mapped[int] = mapped_column(Integer, default=0)
    input_tokens_used: Mapped[int] = mapped_column(Integer, default=0)
    output_tokens_used: Mapped[int] = mapped_column(Integer, default=0)
    transcription_seconds_used: Mapped[int] = mapped_column(Integer, default=0)
    tts_seconds_used: Mapped[int] = mapped_column(Integer, default=0)
    generated_images_used: Mapped[int] = mapped_column(Integer, default=0)
    storage_mb_used: Mapped[int] = mapped_column(Integer, default=0)
    video_minutes_used: Mapped[int] = mapped_column(Integer, default=0)

    __table_args__ = (UniqueConstraint('user_id', 'period_start', 'period_end', name='uq_usage_user_period'),)
