# Billing + Admin Console Runbook

## What was added

This patch adds a commercial SaaS control layer:

- Stripe Billing scaffold
- Checkout Session endpoint
- Customer Portal endpoint
- Stripe webhook endpoint
- Plans, subscriptions, invoices, payment events
- User entitlements
- Usage counters
- Admin / Developer Console endpoints
- Admin dashboard frontend page
- Billing frontend page
- Manual access grant endpoint
- Background jobs, system events and admin audit logs models

## Backend endpoints

### Billing

```text
GET  /api/billing/plans
POST /api/billing/checkout-session
POST /api/billing/customer-portal
POST /api/billing/webhook/stripe
GET  /api/billing/subscription
GET  /api/billing/usage
GET  /api/billing/invoices
```

### Admin

```text
GET   /api/admin/dashboard
GET   /api/admin/users
GET   /api/admin/users/{id}
PATCH /api/admin/users/{id}/access
GET   /api/admin/subscriptions
GET   /api/admin/payments
GET   /api/admin/usage
GET   /api/admin/jobs
POST  /api/admin/jobs/{id}/retry
GET   /api/admin/logs
GET   /api/admin/system-health
GET   /api/admin/licenses
```

## Environment variables

```env
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
STRIPE_SUCCESS_URL=http://localhost:3000/billing?checkout=success
STRIPE_CANCEL_URL=http://localhost:3000/billing?checkout=cancelled
STRIPE_PRICE_BASIC_MONTHLY=
STRIPE_PRICE_PRO_MONTHLY=
STRIPE_PRICE_PREMIUM_MONTHLY=

ADMIN_BOOTSTRAP_EMAIL=admin@example.com
ADMIN_BOOTSTRAP_PASSWORD=change_me_admin_password
```

## Local run

```bash
cp .env.example .env
cp apps/web/.env.example apps/web/.env
docker compose up -d --build
docker compose exec api python scripts/create_tables.py
docker compose exec api python scripts/seed_demo_data.py
```

Open:

```text
Frontend: http://localhost:3000
API docs: http://localhost:8000/docs
Admin page: http://localhost:3000/admin
Billing page: http://localhost:3000/billing
```

## Stripe setup

1. Create Stripe products: Basic, Pro, Premium.
2. Create recurring monthly prices.
3. Copy price IDs into `.env`:

```env
STRIPE_PRICE_BASIC_MONTHLY=price_xxx
STRIPE_PRICE_PRO_MONTHLY=price_xxx
STRIPE_PRICE_PREMIUM_MONTHLY=price_xxx
```

4. Set webhook endpoint:

```text
https://your-api-domain.com/api/billing/webhook/stripe
```

5. Subscribe webhook to:

```text
checkout.session.completed
customer.subscription.created
customer.subscription.updated
customer.subscription.deleted
invoice.paid
invoice.payment_failed
```

## Access control rule

Paid access must be controlled by `user_entitlements`, not by frontend state.

Correct flow:

```text
Stripe webhook → Subscription update → UserEntitlement update → API feature check
```

## AWS deployment notes

Recommended first SaaS deployment:

```text
ECS Fargate services: frontend, api, workers, scheduler
RDS PostgreSQL
ElastiCache Redis
S3
ECR
Secrets Manager
CloudWatch Logs/Metrics/Alarms
CloudTrail
```
