from datetime import datetime
from pydantic import BaseModel


class AdminMetric(BaseModel):
    label: str
    value: str | int | float
    tone: str = 'slate'


class AdminDashboardOut(BaseModel):
    metrics: list[AdminMetric]
    failed_jobs: int
    failed_payments: int
    ai_cost_today: float
    system_status: str


class AdminUserOut(BaseModel):
    id: str
    email: str
    role: str
    status: str
    native_language: str
    plan_code: str | None = None
    created_at: datetime


class ManualAccessRequest(BaseModel):
    plan_code: str
    valid_days: int = 30
    reason: str | None = None


class JobOut(BaseModel):
    id: str
    job_type: str
    status: str
    attempts: int
    error_message: str | None = None
    created_at: datetime


class SystemHealthOut(BaseModel):
    api: str
    database: str
    redis: str
    object_storage: str
    workers: str
    stripe_webhook: str
