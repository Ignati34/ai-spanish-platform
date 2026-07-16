from datetime import datetime, timedelta, timezone
from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.user import User
from app.models.subscription import Invoice, Plan, Subscription, UserEntitlement
from app.models.usage import AIUsageLog, AdminAuditLog, BackgroundJob, SystemEvent


class AdminService:
    def __init__(self, db: Session):
        self.db = db

    def dashboard(self) -> dict:
        users = self.db.query(func.count(User.id)).scalar() or 0
        active_subscriptions = self.db.query(func.count(Subscription.id)).filter(Subscription.status.in_(['active', 'trialing'])).scalar() or 0
        failed_payments = self.db.query(func.count(Invoice.id)).filter(Invoice.status.in_(['open', 'uncollectible', 'void'])).scalar() or 0
        failed_jobs = self.db.query(func.count(BackgroundJob.id)).filter(BackgroundJob.status == 'failed').scalar() or 0
        ai_cost_today = self._ai_cost_today()
        return {
            'metrics': [
                {'label': 'Users', 'value': users, 'tone': 'blue'},
                {'label': 'Active subscriptions', 'value': active_subscriptions, 'tone': 'green'},
                {'label': 'Failed payments', 'value': failed_payments, 'tone': 'rose'},
                {'label': 'Failed jobs', 'value': failed_jobs, 'tone': 'orange'},
                {'label': 'AI cost today', 'value': round(ai_cost_today, 4), 'tone': 'slate'},
            ],
            'failed_jobs': failed_jobs,
            'failed_payments': failed_payments,
            'ai_cost_today': round(ai_cost_today, 4),
            'system_status': 'operational',
        }

    def list_users(self) -> list[dict]:
        rows = self.db.query(User).order_by(User.created_at.desc()).limit(100).all()
        result = []
        for user in rows:
            entitlement = self.db.query(UserEntitlement).filter(UserEntitlement.user_id == user.id).first()
            result.append({
                'id': str(user.id),
                'email': user.email,
                'role': user.role,
                'status': user.status,
                'native_language': user.native_language,
                'plan_code': entitlement.plan_code if entitlement else 'free',
                'created_at': user.created_at,
            })
        return result

    def grant_manual_access(self, actor: User, target_user: User, plan: Plan, valid_days: int, reason: str | None = None) -> UserEntitlement:
        valid_until = datetime.now(timezone.utc) + timedelta(days=valid_days)
        entitlement = self.db.query(UserEntitlement).filter(UserEntitlement.user_id == target_user.id).first()
        if not entitlement:
            entitlement = UserEntitlement(user_id=target_user.id)
            self.db.add(entitlement)
        entitlement.plan_code = plan.code
        entitlement.source = 'manual_admin'
        entitlement.voice_tutor_enabled = plan.voice_tutor_enabled
        entitlement.podcast_enabled = plan.podcast_enabled
        entitlement.image_generation_enabled = plan.image_generation_enabled
        entitlement.video_upload_enabled = plan.video_enabled
        entitlement.max_ai_requests_month = plan.max_ai_requests_per_month
        entitlement.max_transcription_minutes_month = plan.max_transcription_minutes
        entitlement.max_generated_images_month = plan.max_generated_images
        entitlement.max_storage_mb = plan.max_storage_mb
        entitlement.valid_until = valid_until
        self.audit(actor, 'manual_access_granted', 'user', str(target_user.id), {'plan_code': plan.code, 'valid_days': valid_days, 'reason': reason})
        self.db.flush()
        return entitlement

    def audit(self, actor: User | None, action: str, target_type: str | None = None, target_id: str | None = None, metadata: dict | None = None) -> None:
        self.db.add(AdminAuditLog(actor_user_id=actor.id if actor else None, action=action, target_type=target_type, target_id=target_id, metadata_json=metadata))

    def _ai_cost_today(self) -> float:
        start = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
        return float(self.db.query(func.coalesce(func.sum(AIUsageLog.estimated_cost), 0)).filter(AIUsageLog.created_at >= start).scalar() or 0)
