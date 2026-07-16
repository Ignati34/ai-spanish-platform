"""Telegram integration: Mini App auth (initData validation) + Bot/Payments API.

Security note: the Mini App sends `initData` (a signed query string). We validate
its HMAC signature against the bot token before trusting any user identity, per
Telegram's WebApp spec.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import time
from urllib.parse import parse_qsl

import httpx

from app.core.config import get_settings

settings = get_settings()


class TelegramService:
    def __init__(self, bot_token: str | None = None) -> None:
        self.bot_token = bot_token or settings.telegram_bot_token
        self.api = f'https://api.telegram.org/bot{self.bot_token}' if self.bot_token else None

    # ---- Mini App auth ------------------------------------------------------
    def validate_init_data(self, init_data: str, max_age_seconds: int = 86400) -> dict:
        """Validate Telegram WebApp initData and return the parsed `user` dict.

        Raises ValueError if the signature is invalid or the token is missing.
        """
        if not self.bot_token:
            raise ValueError('Telegram bot token is not configured')

        pairs = dict(parse_qsl(init_data, keep_blank_values=True))
        received_hash = pairs.pop('hash', None)
        if not received_hash:
            raise ValueError('initData has no hash')

        data_check_string = '\n'.join(f'{k}={pairs[k]}' for k in sorted(pairs))
        secret_key = hmac.new(b'WebAppData', self.bot_token.encode(), hashlib.sha256).digest()
        computed = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()
        if not hmac.compare_digest(computed, received_hash):
            raise ValueError('initData signature mismatch')

        auth_date = int(pairs.get('auth_date', '0'))
        if max_age_seconds and auth_date and (time.time() - auth_date) > max_age_seconds:
            raise ValueError('initData expired')

        user_raw = pairs.get('user')
        return json.loads(user_raw) if user_raw else {}

    # ---- Bot API ------------------------------------------------------------
    def send_message(self, chat_id: str | int, text: str, **kwargs) -> dict:
        if not self.api:
            return {'ok': False, 'error': 'bot token not configured'}
        resp = httpx.post(f'{self.api}/sendMessage', json={'chat_id': chat_id, 'text': text, **kwargs}, timeout=20)
        return resp.json()

    def answer_pre_checkout_query(self, pre_checkout_query_id: str, ok: bool = True, error_message: str | None = None) -> dict:
        if not self.api:
            return {'ok': False, 'error': 'bot token not configured'}
        payload: dict = {'pre_checkout_query_id': pre_checkout_query_id, 'ok': ok}
        if error_message:
            payload['error_message'] = error_message
        resp = httpx.post(f'{self.api}/answerPreCheckoutQuery', json=payload, timeout=20)
        return resp.json()

    def create_invoice_link(self, title: str, description: str, payload: str, currency: str, prices: list[dict]) -> str:
        if not self.api:
            raise ValueError('bot token not configured')
        body = {
            'title': title,
            'description': description,
            'payload': payload,
            'provider_token': settings.telegram_payment_provider_token,
            'currency': currency,
            'prices': prices,
        }
        resp = httpx.post(f'{self.api}/createInvoiceLink', json=body, timeout=20)
        data = resp.json()
        if not data.get('ok'):
            raise ValueError(f'createInvoiceLink failed: {data}')
        return data['result']
