"""Telegram Mini App auth + Telegram Payments webhook.

- POST /api/telegram/auth       : Mini App logs in with signed initData -> JWT
- POST /api/telegram/webhook     : bot updates (pre_checkout_query, successful_payment)
"""
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.security import create_access_token
from app.db.session import get_db
from app.models.subscription import Plan
from app.models.user import User, UserProfile
from app.services.billing_service import EntitlementsService
from app.services.telegram_service import TelegramService

settings = get_settings()
router = APIRouter(prefix='/telegram', tags=['telegram'])


@router.post('/auth')
def telegram_auth(payload: dict, db: Session = Depends(get_db)):
    """Authenticate a Telegram Mini App user from initData and return a JWT.

    Body: {"init_data": "<raw initData string>", "native_language": "ru"}
    """
    init_data = payload.get('init_data')
    if not init_data:
        raise HTTPException(status_code=400, detail='init_data required')
    try:
        tg_user = TelegramService().validate_init_data(init_data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(exc)) from exc

    tg_id = str(tg_user.get('id'))
    if not tg_id:
        raise HTTPException(status_code=400, detail='no telegram user id')

    user = db.query(User).filter(User.telegram_id == tg_id).first()
    if not user:
        native = payload.get('native_language') or (tg_user.get('language_code') or 'ru')[:2]
        # Telegram users may have no email; synthesize a stable placeholder.
        user = User(
            email=f'tg_{tg_id}@telegram.local',
            password_hash='!telegram',  # login via Telegram only
            telegram_id=tg_id,
            native_language=native,
            interface_language=native,
        )
        db.add(user)
        db.flush()
        db.add(UserProfile(user_id=user.id, first_name=tg_user.get('first_name'), current_cefr_level='A1'))
        EntitlementsService(db).get_or_create_for_user(user)
        db.commit()

    token = create_access_token(str(user.id))
    return {'access_token': token, 'user': {'id': str(user.id), 'telegram_id': tg_id, 'native_language': user.native_language}}


@router.post('/webhook')
async def telegram_webhook(request: Request, db: Session = Depends(get_db)):
    """Receive Telegram bot updates. Handles the payments handshake."""
    update = await request.json()
    tg = TelegramService()

    # 1) Pre-checkout: must answer within 10s to approve the charge.
    pre = update.get('pre_checkout_query')
    if pre:
        tg.answer_pre_checkout_query(pre['id'], ok=True)
        return {'ok': True}

    # 2) Successful payment: grant entitlement.
    message = update.get('message') or {}
    sp = message.get('successful_payment')
    if sp:
        invoice_payload = sp.get('invoice_payload', '')
        parts = invoice_payload.split(':')
        if len(parts) >= 2:
            user_id, plan_code = parts[0], parts[1]
            user = db.get(User, user_id)
            plan = db.query(Plan).filter(Plan.code == plan_code).first()
            if user and plan:
                EntitlementsService(db).from_plan(user, plan, source='telegram')
                db.commit()
                tg.send_message(message['chat']['id'], f'✅ Subscription activated: {plan.name}')
        return {'ok': True}

    return {'ok': True}
