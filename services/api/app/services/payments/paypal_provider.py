"""PayPal provider (subscriptions via PayPal REST API).

Used as an international fallback where users prefer PayPal over cards/SEPA.
Falls back to a dev URL when credentials are not configured so the flow can be
demoed end-to-end without live keys.
"""
from __future__ import annotations

import httpx
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.models.subscription import Plan
from app.models.user import User
from app.services.payments.base import CheckoutResult, PaymentMethodInfo

settings = get_settings()

_API_BASE = {
    'sandbox': 'https://api-m.sandbox.paypal.com',
    'live': 'https://api-m.paypal.com',
}


class PayPalProvider:
    code = 'paypal'

    def is_configured(self) -> bool:
        return bool(settings.paypal_client_id and settings.paypal_client_secret)

    def payment_methods(self) -> list[PaymentMethodInfo]:
        return [PaymentMethodInfo(code='paypal', label='PayPal', countries=[])]

    def _base(self) -> str:
        return _API_BASE.get(settings.paypal_env, _API_BASE['sandbox'])

    def _access_token(self) -> str:
        resp = httpx.post(
            f'{self._base()}/v1/oauth2/token',
            data={'grant_type': 'client_credentials'},
            auth=(settings.paypal_client_id or '', settings.paypal_client_secret or ''),
            timeout=20,
        )
        resp.raise_for_status()
        return resp.json()['access_token']

    def create_checkout(self, db: Session, user: User, plan_code: str, billing_interval: str = 'monthly') -> CheckoutResult:
        plan = db.query(Plan).filter(Plan.code == plan_code, Plan.is_active.is_(True)).first()
        if not plan:
            raise HTTPException(status_code=404, detail='Plan not found')

        if not self.is_configured():
            return CheckoutResult(
                provider=self.code,
                checkout_url=f'{settings.app_url}/billing?dev_checkout_plan={plan.code}&provider=paypal',
                mode='dev_fallback',
            )

        # Provider-side plan id must be created ahead of time and stored in features_json.
        paypal_plan_id = (plan.features_json or {}).get('paypal_plan_id') if plan.features_json else None
        if not paypal_plan_id:
            raise HTTPException(status_code=500, detail='PayPal plan id not configured for this plan')

        token = self._access_token()
        resp = httpx.post(
            f'{self._base()}/v1/billing/subscriptions',
            headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'},
            json={
                'plan_id': paypal_plan_id,
                'custom_id': f'{user.id}:{plan.code}',
                'application_context': {
                    'return_url': settings.stripe_success_url,
                    'cancel_url': settings.stripe_cancel_url,
                },
            },
            timeout=20,
        )
        resp.raise_for_status()
        data = resp.json()
        approve = next((l['href'] for l in data.get('links', []) if l['rel'] == 'approve'), None)
        return CheckoutResult(provider=self.code, checkout_url=approve, session_id=data.get('id'), mode='paypal')
