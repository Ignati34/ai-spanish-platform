"""Stripe provider. Reuses the existing StripeBillingService (webhooks, portal,
entitlements) and adds Spain-friendly payment methods (card, SEPA, Bizum).

Stripe natively supports Bizum and SEPA Direct Debit for EUR merchants, which
covers the majority of Spanish + EU subscribers without a separate Redsys
integration. Redsys remains available as an optional native provider.
"""
from __future__ import annotations

from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.models.user import User
from app.services.billing_service import StripeBillingService
from app.services.payments.base import CheckoutResult, PaymentMethodInfo

settings = get_settings()


class StripeProvider:
    code = 'stripe'

    _METHOD_LABELS = {
        'card': 'Bank card (Visa / Mastercard)',
        'sepa_debit': 'SEPA Direct Debit (EU)',
        'bizum': 'Bizum (Spain)',
        'paypal': 'PayPal',
        'ideal': 'iDEAL (Netherlands)',
        'sofort': 'Sofort',
    }
    _METHOD_COUNTRIES = {
        'bizum': ['ES'],
        'sepa_debit': ['ES', 'FR', 'DE', 'IT', 'PT', 'NL', 'BE', 'IE', 'AT'],
        'ideal': ['NL'],
    }

    def is_configured(self) -> bool:
        return bool(settings.stripe_secret_key)

    def payment_methods(self) -> list[PaymentMethodInfo]:
        out: list[PaymentMethodInfo] = []
        for code in settings.stripe_payment_method_type_list:
            out.append(
                PaymentMethodInfo(
                    code=code,
                    label=self._METHOD_LABELS.get(code, code),
                    countries=self._METHOD_COUNTRIES.get(code, []),
                )
            )
        return out

    def create_checkout(self, db: Session, user: User, plan_code: str, billing_interval: str = 'monthly') -> CheckoutResult:
        result = StripeBillingService(db).create_checkout_session(user, plan_code, billing_interval)
        return CheckoutResult(
            provider=self.code,
            checkout_url=result.get('checkout_url'),
            session_id=result.get('session_id'),
            mode=result.get('mode', 'stripe'),
        )
