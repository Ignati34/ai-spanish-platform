FREE_LIMITS = {
    'ai_requests_per_day': 5,
    'transcription_minutes_per_month': 0,
    'generated_images_per_month': 3,
    'storage_mb': 100,
}

PRO_LIMITS = {
    'ai_requests_per_day': 200,
    'transcription_minutes_per_month': 300,
    'generated_images_per_month': 200,
    'storage_mb': 5000,
}


def get_plan_limits(plan_code: str) -> dict:
    if plan_code.lower() == 'pro':
        return PRO_LIMITS
    return FREE_LIMITS
