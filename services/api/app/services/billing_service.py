from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.models.subscription import (
    BillingCustomer,
    Invoice,
    PaymentEvent,
    Plan,
    Subscription,
    UsageCounter,
    UserEntitlement,
)
from app.models.user import User

settings = get_settings()

try:
    import stripe
except Exception:  # pragma: no cover
    stripe = None


class EntitlementsService:
    def __init__(self, db: Session):
        self.db = db

    def get_or_create_for_user(self, user: User) -> UserEntitlement:
        entitlement = self.db.query(UserEntitlement).filter(UserEntitlement.user_id == user.id).first()
        if entitlement:
            return entitlement
        free_plan = self.db.query(Plan).filter(Plan.code == 'free').first()
        entitlement = self.from_plan(user, free_plan) if free_plan else UserEntitlement(user_id=user.id, plan_code='free')
        self.db.add(entitlement)
        self.db.flush()
        return entitlement

    def from_plan(self, user: User, plan: Plan | None, source: str = 'system', valid_until: datetime | None = None) -> UserEntitlement:
        if not plan:
            return UserEntitlement(user_id=user.id, plan_code='free', source=source, valid_until=valid_until)
        existing = self.db.query(UserEntitlement).filter(UserEntitlement.user_id == user.id).first()
        entitlement = existing or UserEntitlement(user_id=user.id)
        entitlement.plan_code = plan.code
        entitlement.source = source
        entitlement.voice_tutor_enabled = plan.voice_tutor_enabled
        entitlement.podcast_enabled = plan.podcast_enabled
        entitlement.image_generation_enabled = plan.image_generation_enabled or plan.max_generated_images > 0
        entitlement.video_upload_enabled = plan.video_enabled
        entitlement.max_ai_requests_month = plan.max_ai_requests_per_month
        entitlement.max_transcription_minutes_month = plan.max_transcription_minutes
        entitlement.max_generated_images_month = plan.max_generated_images
        entitlement.max_storage_mb = plan.max_storage_mb
        entitlement.valid_until = valid_until
        if not existing:
            self.db.add(entitlement)
        self.db.flush()
        return entitlement

    def require_feature(self, user: User, feature: str) -> UserEntitlement:
        entitlement = self.get_or_create_for_user(user)
        allowed = getattr(entitlement, feature, False)
        if not allowed:
            raise HTTPException(status_code=status.HTTP_402_PAYMENT_REQUIRED, detail=f'Feature locked: {feature}')
        return entitlement


class UsageService:
    def __init__(self, db: Session):
        self.db = db

    def current_period(self) -> tuple[datetime, datetime]:
        now = datetime.now(timezone.utc)
        start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        if start.month == 12:
            end = start.replace(year=start.year + 1, month=1)
        else:
            end = start.replace(month=start.month + 1)
        return start, end

    def get_or_create_counter(self, user_id) -> UsageCounter:
        start, end = self.current_period()
        counter = (
            self.db.query(UsageCounter)
            .filter(UsageCounter.user_id == user_id, UsageCounter.period_start == start, UsageCounter.period_end == end)
            .first()
        )
        if counter:
            return counter
        counter = UsageCounter(user_id=user_id, period_start=start, period_end=end)
        self.db.add(counter)
        self.db.flush()
        return counter

    def increment(self, user_id, **increments: int) -> UsageCounter:
        counter = self.get_or_create_counter(user_id)
        for key, value in increments.items():
            if not hasattr(counter, key):
                continue
            setattr(counter, key, getattr(counter, key) + int(value))
        self.db.flush()
        return counter


class StripeBillingService:
    def __init__(self, db: Session):
        self.db = db
        if stripe and settings.stripe_secret_key:
            stripe.api_key = settings.stripe_secret_key

    def list_plans(self) -> list[Plan]:
        return self.db.query(Plan).filter(Plan.is_active.is_(True)).order_by(Plan.price_monthly.asc()).all()

    def create_checkout_session(self, user: User, plan_code: str, billing_interval: str = 'monthly') -> dict[str, Any]:
        plan = self.db.query(Plan).filter(Plan.code == plan_code, Plan.is_active.is_(True)).first()
        if not plan:
            raise HTTPException(status_code=404, detail='Plan not found')

        price_id = plan.provider_price_id_monthly if billing_interval == 'monthly' else plan.provider_price_id_yearly
        if not price_id:
            # Dev fallback: no Stripe configured yet. The frontend can display this in mock/dev mode.
            return {
                'checkout_url': f'{settings.app_url}/billing?dev_checkout_plan={plan.code}',
                'session_id': None,
                'mode': 'dev_fallback',
            }

        if not stripe or not settings.stripe_secret_key:
            raise HTTPException(status_code=500, detail='Stripe is not configured')

        checkout_kwargs = dict(
            mode='subscription',
            customer_email=user.email,
            line_items=[{'price': price_id, 'quantity': 1}],
            success_url=settings.stripe_success_url,
            cancel_url=settings.stripe_cancel_url,
            metadata={'user_id': str(user.id), 'plan_code': plan.code},
        )
        # Offer locally-appropriate methods (card + SEPA + Bizum for ES/EU).
        method_types = settings.stripe_payment_method_type_list
        if method_types:
            checkout_kwargs['payment_method_types'] = method_types
        session = stripe.checkout.Session.create(**checkout_kwargs)
        return {'checkout_url': session.url, 'session_id': session.id, 'mode': 'stripe'}

    def create_customer_portal(self, user: User) -> dict[str, str]:
        customer = self.db.query(BillingCustomer).filter(BillingCustomer.user_id == user.id, BillingCustomer.provider == 'stripe').first()
        if not customer:
            raise HTTPException(status_code=404, detail='Stripe customer not found')
        if not stripe or not settings.stripe_secret_key:
            raise HTTPException(status_code=500, detail='Stripe is not configured')
        portal = stripe.billing_portal.Session.create(customer=customer.provider_customer_id, return_url=f'{settings.app_url}/billing')
        return {'portal_url': portal.url}

    def construct_webhook_event(self, payload: bytes, signature: str | None):
        if not stripe or not settings.stripe_webhook_secret:
            raise HTTPException(status_code=500, detail='Stripe webhook is not configured')
        try:
            return stripe.Webhook.construct_event(payload=payload, sig_header=signature, secret=settings.stripe_webhook_secret)
        except Exception as exc:
            raise HTTPException(status_code=400, detail=f'Invalid Stripe webhook: {exc}') from exc

    def store_event_once(self, event: dict[str, Any]) -> PaymentEvent:
        event_id = event['id']
        existing = self.db.query(PaymentEvent).filter(PaymentEvent.event_id == event_id).first()
        if existing:
            return existing
        payment_event = PaymentEvent(
            provider='stripe',
            event_id=event_id,
            event_type=event['type'],
            payload_json=dict(event),
            processing_status='received',
        )
        self.db.add(payment_event)
        self.db.flush()
        return payment_event

    def process_webhook_event(self, event: dict[str, Any]) -> PaymentEvent:
        payment_event = self.store_event_once(event)
        if payment_event.processing_status == 'processed':
            return payment_event
        try:
            event_type = event['type']
            data_object = event['data']['object']
            if event_type == 'checkout.session.completed':
                self._handle_checkout_completed(data_object)
            elif event_type in {'customer.subscription.created', 'customer.subscription.updated'}:
                self._handle_subscription_updated(data_object)
            elif event_type == 'customer.subscription.deleted':
                self._handle_subscription_deleted(data_object)
            elif event_type in {'invoice.paid', 'invoice.payment_failed'}:
                self._handle_invoice(data_object)
            payment_event.processing_status = 'processed'
            payment_event.processed_at = datetime.now(timezone.utc)
        except Exception as exc:  # pragma: no cover
            payment_event.processing_status = 'failed'
            payment_event.error_message = str(exc)[:1000]
            raise
        finally:
            self.db.flush()
        return payment_event

    def _handle_checkout_completed(self, session: dict[str, Any]) -> None:
        user_id = session.get('metadata', {}).get('user_id')
        plan_code = session.get('metadata', {}).get('plan_code')
        customer_id = session.get('customer')
        subscription_id = session.get('subscription')
        if not user_id or not plan_code:
            return
        user = self.db.get(User, user_id)
        plan = self.db.query(Plan).filter(Plan.code == plan_code).first()
        if not user or not plan:
            return
        if customer_id:
            self._upsert_customer(user, str(customer_id))
        self._upsert_subscription(user, plan, str(subscription_id) if subscription_id else None, str(customer_id) if customer_id else None, 'active')
        EntitlementsService(self.db).from_plan(user, plan, source='stripe')

    def _handle_subscription_updated(self, subscription: dict[str, Any]) -> None:
        customer_id = subscription.get('customer')
        status_value = subscription.get('status', 'active')
        user = self._find_user_by_customer(customer_id)
        if not user:
            return
        price_id = subscription.get('items', {}).get('data', [{}])[0].get('price', {}).get('id')
        plan = self._find_plan_by_price(price_id)
        if not plan:
            return
        current_period_end = self._from_ts(subscription.get('current_period_end'))
        self._upsert_subscription(user, plan, subscription.get('id'), customer_id, status_value, current_period_end)
        if status_value in {'active', 'trialing'}:
            EntitlementsService(self.db).from_plan(user, plan, source='stripe', valid_until=current_period_end)
        else:
            free_plan = self.db.query(Plan).filter(Plan.code == 'free').first()
            EntitlementsService(self.db).from_plan(user, free_plan, source='stripe')

    def _handle_subscription_deleted(self, subscription: dict[str, Any]) -> None:
        existing = self.db.query(Subscription).filter(Subscription.provider_subscription_id == subscription.get('id')).first()
        if existing:
            existing.status = 'canceled'
            user = self.db.get(User, existing.user_id)
            free_plan = self.db.query(Plan).filter(Plan.code == 'free').first()
            if user and free_plan:
                EntitlementsService(self.db).from_plan(user, free_plan, source='stripe')

    def _handle_invoice(self, invoice: dict[str, Any]) -> None:
        invoice_id = invoice.get('id')
        if not invoice_id:
            return
        customer_id = invoice.get('customer')
        user = self._find_user_by_customer(customer_id)
        existing = self.db.query(Invoice).filter(Invoice.provider_invoice_id == invoice_id).first()
        target = existing or Invoice(provider_invoice_id=invoice_id)
        target.user_id = user.id if user else None
        target.provider_customer_id = customer_id
        target.amount_due = invoice.get('amount_due') or 0
        target.amount_paid = invoice.get('amount_paid') or 0
        target.currency = invoice.get('currency') or 'eur'
        target.status = invoice.get('status') or 'unknown'
        target.invoice_pdf_url = invoice.get('invoice_pdf')
        target.hosted_invoice_url = invoice.get('hosted_invoice_url')
        if not existing:
            self.db.add(target)

    def _upsert_customer(self, user: User, customer_id: str) -> BillingCustomer:
        existing = self.db.query(BillingCustomer).filter(BillingCustomer.provider == 'stripe', BillingCustomer.provider_customer_id == customer_id).first()
        if existing:
            existing.user_id = user.id
            existing.email = user.email
            return existing
        customer = BillingCustomer(user_id=user.id, provider='stripe', provider_customer_id=customer_id, email=user.email)
        self.db.add(customer)
        self.db.flush()
        return customer

    def _upsert_subscription(self, user: User, plan: Plan, subscription_id: str | None, customer_id: str | None, status_value: str, current_period_end: datetime | None = None) -> Subscription:
        existing = None
        if subscription_id:
            existing = self.db.query(Subscription).filter(Subscription.provider_subscription_id == subscription_id).first()
        if not existing:
            existing = self.db.query(Subscription).filter(Subscription.user_id == user.id, Subscription.provider == 'stripe').first()
        target = existing or Subscription(user_id=user.id, provider='stripe')
        target.plan_id = plan.id
        target.provider_customer_id = customer_id
        target.provider_subscription_id = subscription_id
        target.status = status_value
        target.current_period_end = current_period_end
        if not existing:
            self.db.add(target)
        self.db.flush()
        return target

    def _find_user_by_customer(self, customer_id: str | None) -> User | None:
        if not customer_id:
            return None
        customer = self.db.query(BillingCustomer).filter(BillingCustomer.provider == 'stripe', BillingCustomer.provider_customer_id == customer_id).first()
        if not customer:
            return None
        return self.db.get(User, customer.user_id)

    def _find_plan_by_price(self, price_id: str | None) -> Plan | None:
        if not price_id:
            return None
        return (
            self.db.query(Plan)
            .filter((Plan.provider_price_id_monthly == price_id) | (Plan.provider_price_id_yearly == price_id))
            .first()
        )

    def _from_ts(self, value) -> datetime | None:
        if not value:
            return None
        return datetime.fromtimestamp(value, tz=timezone.utc)
