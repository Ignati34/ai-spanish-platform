from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.api.deps import require_admin, require_billing_admin
from app.db.session import get_db
from app.models.license import License
from app.models.subscription import Invoice, PaymentEvent, Plan, Subscription
from app.models.usage import AdminAuditLog, BackgroundJob, SystemEvent
from app.models.user import User
from app.schemas.admin import ManualAccessRequest
from app.services.admin_service import AdminService
from app.content.syllabus import SYLLABUS
from app.services import lesson_generator

router = APIRouter(prefix='/admin', tags=['admin'])


@router.get('/dashboard')
def dashboard(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    return AdminService(db).dashboard()


@router.get('/users')
def users(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    return AdminService(db).list_users()


@router.get('/users/{user_id}')
def user_detail(user_id: str, admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    subscriptions = db.query(Subscription).filter(Subscription.user_id == user.id).order_by(Subscription.created_at.desc()).all()
    return {
        'id': str(user.id),
        'email': user.email,
        'role': user.role,
        'status': user.status,
        'native_language': user.native_language,
        'subscriptions': [{'status': s.status, 'provider_subscription_id': s.provider_subscription_id, 'created_at': s.created_at} for s in subscriptions],
    }


@router.patch('/users/{user_id}/access')
def grant_access(user_id: str, payload: ManualAccessRequest, admin: User = Depends(require_billing_admin), db: Session = Depends(get_db)):
    target = db.get(User, user_id)
    if not target:
        raise HTTPException(status_code=404, detail='User not found')
    plan = db.query(Plan).filter(Plan.code == payload.plan_code).first()
    if not plan:
        raise HTTPException(status_code=404, detail='Plan not found')
    entitlement = AdminService(db).grant_manual_access(admin, target, plan, payload.valid_days, payload.reason)
    db.commit()
    return {'user_id': str(target.id), 'plan_code': entitlement.plan_code, 'valid_until': entitlement.valid_until}


@router.get('/subscriptions')
def subscriptions(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    rows = db.query(Subscription).order_by(Subscription.created_at.desc()).limit(100).all()
    return [{'id': str(s.id), 'user_id': str(s.user_id), 'status': s.status, 'provider': s.provider, 'provider_subscription_id': s.provider_subscription_id, 'created_at': s.created_at} for s in rows]


@router.get('/payments')
def payments(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    invoices = db.query(Invoice).order_by(Invoice.created_at.desc()).limit(100).all()
    events = db.query(PaymentEvent).order_by(PaymentEvent.created_at.desc()).limit(50).all()
    return {
        'invoices': [{'id': str(i.id), 'status': i.status, 'amount_paid': i.amount_paid, 'currency': i.currency, 'created_at': i.created_at} for i in invoices],
        'events': [{'event_id': e.event_id, 'event_type': e.event_type, 'processing_status': e.processing_status, 'created_at': e.created_at} for e in events],
    }


@router.get('/usage')
def usage(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    # Compact MVP aggregation. Extend with charts later.
    return AdminService(db).dashboard()


@router.get('/jobs')
def jobs(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    rows = db.query(BackgroundJob).order_by(BackgroundJob.created_at.desc()).limit(100).all()
    return [{'id': str(j.id), 'job_type': j.job_type, 'status': j.status, 'attempts': j.attempts, 'error_message': j.error_message, 'created_at': j.created_at} for j in rows]


@router.post('/jobs/{job_id}/retry')
def retry_job(job_id: str, admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    job = db.get(BackgroundJob, job_id)
    if not job:
        raise HTTPException(status_code=404, detail='Job not found')
    job.status = 'queued'
    job.error_message = None
    job.attempts = 0
    AdminService(db).audit(admin, 'job_retry_requested', 'background_job', str(job.id), {'job_type': job.job_type})
    db.commit()
    return {'id': str(job.id), 'status': job.status}


@router.get('/logs')
def logs(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    system_events = db.query(SystemEvent).order_by(SystemEvent.created_at.desc()).limit(100).all()
    audit_logs = db.query(AdminAuditLog).order_by(AdminAuditLog.created_at.desc()).limit(100).all()
    return {
        'system_events': [{'severity': e.severity, 'source': e.source, 'event_type': e.event_type, 'message': e.message, 'created_at': e.created_at} for e in system_events],
        'admin_audit_logs': [{'actor_user_id': str(a.actor_user_id) if a.actor_user_id else None, 'action': a.action, 'target_type': a.target_type, 'target_id': a.target_id, 'created_at': a.created_at} for a in audit_logs],
    }


@router.get('/system-health')
def system_health(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    db.execute(text('SELECT 1'))
    return {
        'api': 'ok',
        'database': 'ok',
        'redis': 'not_checked_in_mvp',
        'object_storage': 'not_checked_in_mvp',
        'workers': 'not_checked_in_mvp',
        'stripe_webhook': 'configured_check_env',
    }


@router.get('/licenses')
def licenses(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    rows = db.query(License).order_by(License.created_at.desc()).limit(100).all()
    return [{'id': str(l.id), 'edition': l.edition, 'max_users': l.max_users, 'valid_until': l.valid_until, 'status': l.status, 'created_at': l.created_at} for l in rows]


@router.get('/curriculum/status')
def curriculum_status(admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    done = lesson_generator.existing_numbers(db)
    return {'total': len(SYLLABUS), 'generated': len(done), 'remaining': len(SYLLABUS) - len(done)}


@router.post('/curriculum/generate')
async def curriculum_generate(count: int = 5, native: str = 'ru', admin: User = Depends(require_admin), db: Session = Depends(get_db)):
    """Generate the next N missing curriculum lessons via AI (capped at 20 per call)."""
    count = max(1, min(20, count))
    done = lesson_generator.existing_numbers(db)
    todo = [e for e in SYLLABUS if e['n'] not in done][:count]
    created = 0
    for e in todo:
        try:
            await lesson_generator.generate_and_store(db, e, native)
            created += 1
        except Exception:
            continue
    return {'created': created, 'generated_total': len(done) + created, 'total': len(SYLLABUS)}
