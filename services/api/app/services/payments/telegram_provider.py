"""Telegram Payments provider (for the Telegram Mini App / bot).

Instead of a redirect URL, Telegram uses an "invoice link" that opens the native
in-app payment sheet. Payment confirmation arrives via bot updates
(pre_checkout_query -> successful_payment), handled in routes_telegram.
"""
from __future__ import annotations

from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.models.subscription import Plan
from app.models.user import User
from app.services.payments.base import CheckoutResult, PaymentMethodInfo
from app.services.telegram_service import TelegramService

settings = get_settings()


class TelegramProvider:
    code = 'telegram'

    def is_configured(self) -> bool:
        return bool(settings.telegram_bot_token and settings.telegram_payment_provider_token)

    def payment_methods(self) -> list[PaymentMethodInfo]:
        return [PaymentMethodInfo(code='telegram', label='Telegram Payments', countries=[])]

    def create_checkout(self, db: Session, user: User, plan_code: str, billing_interval: str = 'monthly') -> CheckoutResult:
        plan = db.query(Plan).filter(Plan.code == plan_code, Plan.is_active.is_(True)).first()
        if not plan:
            raise HTTPException(status_code=404, detail='Plan not found')

        amount = float(plan.price_yearly if billing_interval == 'yearly' else plan.price_monthly)
        payload = f'{user.id}:{plan.code}:{billing_interval}'

        if not self.is_configured():
            return CheckoutResult(provider=self.code, invoice_payload=payload, mode='dev_fallback')

        currency = settings.telegram_payment_currency
        minor_units = int(round(amount * 100))
        link = TelegramService().create_invoice_link(
            title=f'{plan.name} ({billing_interval})',
            description=plan.description or f'Subscription: {plan.name}',
            payload=payload,
            currency=currency,
            prices=[{'label': plan.name, 'amount': minor_units}],
        )
        return CheckoutResult(provider=self.code, checkout_url=link, invoice_payload=payload, mode='telegram')
