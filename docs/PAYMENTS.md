# Payments — Spain & international

The platform never hardcodes a single PSP. Providers implement a common interface
(`app/services/payments/base.py`) and are exposed through a registry that annotates
methods by country. The frontend calls `GET /api/billing/providers?country=ES` and
renders only the relevant methods.

## What is available where

| Provider | Methods | Best for | Notes |
|---|---|---|---|
| **Stripe** | Card, **Bizum**, **SEPA Direct Debit**, PayPal | Spain + EU + intl cards | Stripe supports Bizum & SEPA natively for EUR merchants — covers most of Spain without a separate Redsys integration. |
| **PayPal** | PayPal balance/cards | International fallback | Subscriptions via PayPal REST. Requires a PayPal plan id stored in `plan.features_json.paypal_plan_id`. |
| **Telegram Payments** | Whatever the bound PSP supports | Inside the Telegram Mini App | Uses `createInvoiceLink`; confirmation via bot `pre_checkout_query` → `successful_payment`. |
| **Redsys / Bizum (native)** | Bizum, Spanish cards | Spain, if you use a Spanish acquiring bank directly | Config hooks are present (`REDSYS_*`). Implement only if you need native Redsys instead of Stripe. |

## Which are "permitted" in Spain
Card schemes (Visa/Mastercard), **Bizum**, and **SEPA Direct Debit** are the standard,
regulated methods for recurring subscriptions in Spain. All three are available through
Stripe here, so a single Stripe account satisfies the Spanish requirement while also
handling international cards. PayPal and Telegram Payments extend coverage to users who
prefer them or who subscribe from inside Telegram.

## Enabling providers
Set `PAYMENT_PROVIDERS=stripe,paypal,telegram` in `.env` and configure the keys for the
ones you enable. Unconfigured providers still appear in dev with a `dev_fallback` mode so
the flow is demoable without live keys.

## Endpoints
- `GET  /api/billing/plans` — plans (EUR).
- `GET  /api/billing/providers?country=ES` — providers + methods, `recommended` flag per country.
- `POST /api/billing/checkout` — `{provider, plan_code, billing_interval}` → checkout URL or Telegram invoice.
- `POST /api/billing/checkout-session` — Stripe-only convenience endpoint (kept for compatibility).
- `POST /api/billing/webhook/stripe` — Stripe webhook (source of truth for access).
- `POST /api/telegram/webhook` — Telegram payment handshake.

**Access is granted only after a verified webhook**, never on the success page.
