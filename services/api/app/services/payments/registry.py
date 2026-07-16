"""Registry that exposes enabled providers and computes method availability by
country. The frontend calls GET /api/billing/providers to render only the
methods relevant to the user's country (e.g. Bizum for ES)."""
from __future__ import annotations

from functools import lru_cache

from app.core.config import get_settings
from app.services.payments.base import PaymentProvider
from app.services.payments.paypal_provider import PayPalProvider
from app.services.payments.stripe_provider import StripeProvider
from app.services.payments.telegram_provider import TelegramProvider

settings = get_settings()

_ALL = {
    'stripe': StripeProvider,
    'paypal': PayPalProvider,
    'telegram': TelegramProvider,
}


class PaymentRegistry:
    def __init__(self) -> None:
        self.providers: dict[str, PaymentProvider] = {}
        for code in settings.payment_provider_list:
            cls = _ALL.get(code)
            if cls:
                self.providers[code] = cls()

    def get(self, code: str) -> PaymentProvider:
        provider = self.providers.get(code)
        if not provider:
            raise KeyError(f'Payment provider not enabled: {code}')
        return provider

    def describe(self, country: str | None = None) -> list[dict]:
        """Return providers + methods, optionally filtered/annotated for a country."""
        country = (country or '').upper() or None
        out = []
        for code, provider in self.providers.items():
            methods = []
            for m in provider.payment_methods():
                available = (not m.countries) or (country in m.countries if country else True)
                methods.append(
                    {'code': m.code, 'label': m.label, 'countries': m.countries, 'recommended': bool(country and country in m.countries)}
                )
            out.append(
                {
                    'code': code,
                    'configured': provider.is_configured(),
                    'methods': methods,
                }
            )
        return out


@lru_cache
def get_payment_registry() -> PaymentRegistry:
    return PaymentRegistry()
