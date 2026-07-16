from fastapi import APIRouter, Depends, Header, Request
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.subscription import Invoice, Subscription
from app.models.user import User
from app.schemas.billing import CheckoutSessionRequest
from app.services.billing_service import EntitlementsService, StripeBillingService, UsageService
from app.services.payments.registry import get_payment_registry

router = APIRouter(prefix='/billing', tags=['billing'])


@router.get('/plans')
def list_plans(db: Session = Depends(get_db)):
    plans = StripeBillingService(db).list_plans()
    return [
        {
            'code': p.code,
            'name': p.name,
            'description': p.description,
            'price_monthly': float(p.price_monthly),
            'price_yearly': float(p.price_yearly),
            'currency': p.currency,
            'voice_tutor_enabled': p.voice_tutor_enabled,
            'podcast_enabled': p.podcast_enabled,
            'image_generation_enabled': p.image_generation_enabled,
            'video_enabled': p.video_enabled,
            'max_ai_requests_per_month': p.max_ai_requests_per_month,
            'max_transcription_minutes': p.max_transcription_minutes,
            'max_generated_images': p.max_generated_images,
            'max_storage_mb': p.max_storage_mb,
        }
        for p in plans
    ]


@router.post('/checkout-session')
def create_checkout_session(payload: CheckoutSessionRequest, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    result = StripeBillingService(db).create_checkout_session(current_user, payload.plan_code, payload.billing_interval)
    db.commit()
    return result


@router.post('/customer-portal')
def create_customer_portal(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return StripeBillingService(db).create_customer_portal(current_user)


@router.post('/webhook/stripe')
async def stripe_webhook(request: Request, stripe_signature: str | None = Header(default=None, alias='Stripe-Signature'), db: Session = Depends(get_db)):
    payload = await request.body()
    service = StripeBillingService(db)
    event = service.construct_webhook_event(payload, stripe_signature)
    payment_event = service.process_webhook_event(event)
    db.commit()
    return {'received': True, 'event_id': payment_event.event_id, 'status': payment_event.processing_status}


@router.get('/subscription')
def current_subscription(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    entitlement = EntitlementsService(db).get_or_create_for_user(current_user)
    subscription = db.query(Subscription).filter(Subscription.user_id == current_user.id).order_by(Subscription.created_at.desc()).first()
    return {
        'status': subscription.status if subscription else 'free',
        'plan_code': entitlement.plan_code,
        'current_period_end': subscription.current_period_end if subscription else None,
        'cancel_at_period_end': subscription.cancel_at_period_end if subscription else False,
        'entitlement': {
            'plan_code': entitlement.plan_code,
            'voice_tutor_enabled': entitlement.voice_tutor_enabled,
            'podcast_enabled': entitlement.podcast_enabled,
            'image_generation_enabled': entitlement.image_generation_enabled,
            'video_upload_enabled': entitlement.video_upload_enabled,
            'max_ai_requests_month': entitlement.max_ai_requests_month,
            'max_transcription_minutes_month': entitlement.max_transcription_minutes_month,
            'max_generated_images_month': entitlement.max_generated_images_month,
            'max_storage_mb': entitlement.max_storage_mb,
            'valid_until': entitlement.valid_until,
        },
    }


@router.get('/usage')
def current_usage(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    counter = UsageService(db).get_or_create_counter(current_user.id)
    return {
        'ai_requests_used': counter.ai_requests_used,
        'input_tokens_used': counter.input_tokens_used,
        'output_tokens_used': counter.output_tokens_used,
        'transcription_seconds_used': counter.transcription_seconds_used,
        'tts_seconds_used': counter.tts_seconds_used,
        'generated_images_used': counter.generated_images_used,
        'storage_mb_used': counter.storage_mb_used,
        'video_minutes_used': counter.video_minutes_used,
    }


@router.get('/invoices')
def invoices(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    rows = db.query(Invoice).filter(Invoice.user_id == current_user.id).order_by(Invoice.created_at.desc()).limit(50).all()
    return [
        {
            'provider_invoice_id': row.provider_invoice_id,
            'amount_due': row.amount_due,
            'amount_paid': row.amount_paid,
            'currency': row.currency,
            'status': row.status,
            'invoice_pdf_url': row.invoice_pdf_url,
            'hosted_invoice_url': row.hosted_invoice_url,
            'created_at': row.created_at,
        }
        for row in rows
    ]


@router.get('/providers')
def list_providers(country: str | None = None, db: Session = Depends(get_db)):
    """List enabled payment providers and their methods, annotated for a country.

    The frontend uses this to show Bizum for Spain, cards internationally,
    Telegram Payments inside the Mini App, PayPal as a fallback, etc.
    """
    return {'country': (country or None), 'providers': get_payment_registry().describe(country)}


@router.post('/checkout')
def create_checkout(payload: dict, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    """Provider-aware checkout.

    Body: {"provider": "stripe", "plan_code": "pro", "billing_interval": "monthly"}
    """
    provider_code = payload.get('provider', 'stripe')
    plan_code = payload.get('plan_code')
    interval = payload.get('billing_interval', 'monthly')
    if not plan_code:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail='plan_code required')
    try:
        provider = get_payment_registry().get(provider_code)
    except KeyError as exc:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    result = provider.create_checkout(db, current_user, plan_code, interval)
    db.commit()
    return {
        'provider': result.provider,
        'checkout_url': result.checkout_url,
        'invoice_payload': result.invoice_payload,
        'session_id': result.session_id,
        'mode': result.mode,
    }
