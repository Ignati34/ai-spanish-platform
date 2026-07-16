"""Provider-agnostic payment abstraction.

Every provider (Stripe, PayPal, Telegram Payments, Redsys/Bizum) implements this
interface so the rest of the app never hardcodes a single PSP. This is what lets
the platform offer locally-appropriate methods: Bizum/SEPA in Spain, cards
internationally, Telegram Payments inside the Mini App, PayPal as a fallback.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Protocol, runtime_checkable

from sqlalchemy.orm import Session

from app.models.user import User


@dataclass
class PaymentMethodInfo:
    code: str                      # e.g. "card", "sepa_debit", "bizum", "paypal", "telegram_stars"
    label: str                     # human label
    countries: list[str] = field(default_factory=list)  # ISO-2 codes; [] = worldwide


@dataclass
class CheckoutResult:
    provider: str
    checkout_url: str | None = None
    invoice_payload: str | None = None   # for Telegram in-app invoices
    session_id: str | None = None
    mode: str = 'live'
    extra: dict[str, Any] = field(default_factory=dict)


@runtime_checkable
class PaymentProvider(Protocol):
    """A minimal contract each payment provider must satisfy."""

    code: str

    def is_configured(self) -> bool: ...

    def payment_methods(self) -> list[PaymentMethodInfo]: ...

    def create_checkout(
        self, db: Session, user: User, plan_code: str, billing_interval: str = 'monthly'
    ) -> CheckoutResult: ...
