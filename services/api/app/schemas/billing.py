from datetime import datetime
from pydantic import BaseModel


class PlanOut(BaseModel):
    code: str
    name: str
    description: str | None = None
    price_monthly: float
    price_yearly: float
    currency: str
    voice_tutor_enabled: bool
    podcast_enabled: bool
    image_generation_enabled: bool
    video_enabled: bool
    max_ai_requests_per_month: int
    max_transcription_minutes: int
    max_generated_images: int
    max_storage_mb: int

    model_config = {'from_attributes': True}


class CheckoutSessionRequest(BaseModel):
    plan_code: str
    billing_interval: str = 'monthly'


class CheckoutSessionResponse(BaseModel):
    checkout_url: str
    session_id: str | None = None
    mode: str = 'stripe'


class CustomerPortalResponse(BaseModel):
    portal_url: str


class EntitlementOut(BaseModel):
    plan_code: str
    voice_tutor_enabled: bool
    podcast_enabled: bool
    image_generation_enabled: bool
    video_upload_enabled: bool
    max_ai_requests_month: int
    max_transcription_minutes_month: int
    max_generated_images_month: int
    max_storage_mb: int
    valid_until: datetime | None = None

    model_config = {'from_attributes': True}


class UsageOut(BaseModel):
    ai_requests_used: int = 0
    input_tokens_used: int = 0
    output_tokens_used: int = 0
    transcription_seconds_used: int = 0
    tts_seconds_used: int = 0
    generated_images_used: int = 0
    storage_mb_used: int = 0
    video_minutes_used: int = 0


class SubscriptionOut(BaseModel):
    status: str
    plan_code: str
    current_period_end: datetime | None = None
    cancel_at_period_end: bool = False
    entitlement: EntitlementOut


class InvoiceOut(BaseModel):
    provider_invoice_id: str
    amount_due: int
    amount_paid: int
    currency: str
    status: str
    invoice_pdf_url: str | None = None
    hosted_invoice_url: str | None = None
    created_at: datetime

    model_config = {'from_attributes': True}
