# Telegram Mini App

The same web build runs as a Telegram Mini App — no separate frontend.

## How it works
1. `index.html` loads `telegram-web-app.js`. `initTelegram()` calls `ready()` + `expand()`.
2. Inside Telegram, `LoginPage` detects `WebApp.initData` and calls
   `POST /api/telegram/auth` with the raw `initData`.
3. The backend validates the `initData` HMAC signature against the bot token
   (`TelegramService.validate_init_data`), finds/creates the user by `telegram_id`,
   and returns a JWT — same session model as the web app.

## Payments in Telegram
- `BillingPage` uses the `telegram` provider when running inside Telegram.
- `POST /api/billing/checkout` returns a Telegram **invoice link**; the app opens it with
  `WebApp.openInvoice(...)`.
- Telegram sends bot updates to `POST /api/telegram/webhook`:
  `pre_checkout_query` → auto-approve, then `successful_payment` → grant entitlement.

## Setup
1. Create a bot with @BotFather, set `TELEGRAM_BOT_TOKEN`.
2. Set the Mini App URL (`/setmenubutton` or a Web App button) to your `TELEGRAM_WEBAPP_URL`.
3. For payments, connect a PSP in @BotFather and set `TELEGRAM_PAYMENT_PROVIDER_TOKEN`.
4. Register the webhook: `https://api.telegram.org/bot<token>/setWebhook?url=<API_URL>/api/telegram/webhook`.
