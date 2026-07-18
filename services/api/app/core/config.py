from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    app_env: str = Field(default='development', alias='APP_ENV')
    app_name: str = Field(default='AI Spanish Learning Platform', alias='APP_NAME')
    app_url: str = Field(default='http://localhost:3000', alias='APP_URL')
    api_url: str = Field(default='http://localhost:8000', alias='API_URL')

    database_url: str = Field(alias='DATABASE_URL')
    redis_url: str = Field(default='redis://redis:6379/0', alias='REDIS_URL')

    jwt_secret: str = Field(alias='JWT_SECRET')
    jwt_algorithm: str = Field(default='HS256', alias='JWT_ALGORITHM')
    jwt_expires_minutes: int = Field(default=1440, alias='JWT_EXPIRES_MINUTES')
    refresh_token_expires_days: int = Field(default=30, alias='REFRESH_TOKEN_EXPIRES_DAYS')

    s3_endpoint: str = Field(default='http://minio:9000', alias='S3_ENDPOINT')
    s3_access_key: str = Field(default='minio', alias='S3_ACCESS_KEY')
    s3_secret_key: str = Field(default='minio_password', alias='S3_SECRET_KEY')
    s3_bucket_uploads: str = Field(default='uploads', alias='S3_BUCKET_UPLOADS')
    s3_bucket_generated: str = Field(default='generated', alias='S3_BUCKET_GENERATED')
    s3_region: str = Field(default='us-east-1', alias='S3_REGION')

    ai_provider: str = Field(default='stub', alias='AI_PROVIDER')  # stub | openai
    ai_api_key: str | None = Field(default=None, alias='AI_API_KEY')
    # Chat LLM (OpenAI-compatible: works with OpenAI or any compatible base_url).
    ai_base_url: str = Field(default='https://api.openai.com/v1', alias='AI_BASE_URL')
    ai_model: str = Field(default='gpt-4o-mini', alias='AI_MODEL')
    ai_temperature: float = Field(default=0.2, alias='AI_TEMPERATURE')
    ai_max_tokens: int = Field(default=1400, alias='AI_MAX_TOKENS')
    ai_timeout_seconds: int = Field(default=45, alias='AI_TIMEOUT_SECONDS')
    ai_cache_ttl_seconds: int = Field(default=86400, alias='AI_CACHE_TTL_SECONDS')
    ai_cache_enabled: bool = Field(default=True, alias='AI_CACHE_ENABLED')
    stt_model: str = Field(default='gpt-4o-mini-transcribe', alias='STT_MODEL')
    tts_model: str = Field(default='gpt-4o-mini-tts', alias='TTS_MODEL')
    tts_voice: str = Field(default='alloy', alias='TTS_VOICE')
    tts_format: str = Field(default='mp3', alias='TTS_FORMAT')
    image_model: str = Field(default='image_model_name', alias='IMAGE_MODEL')
    embedding_model: str = Field(default='embedding_model_name', alias='EMBEDDING_MODEL')

    # ---- Localization -------------------------------------------------------
    default_interface_language: str = Field(default='ru', alias='DEFAULT_INTERFACE_LANGUAGE')
    supported_locales: str = Field(default='ru,uk,ar,fr,es,en', alias='SUPPORTED_LOCALES')
    rtl_locales: str = Field(default='ar', alias='RTL_LOCALES')
    default_currency: str = Field(default='eur', alias='DEFAULT_CURRENCY')

    # ---- Payments: providers ------------------------------------------------
    # Comma-separated list of enabled providers, e.g. "stripe,paypal,telegram"
    payment_providers: str = Field(default='stripe', alias='PAYMENT_PROVIDERS')

    # Stripe (cards + SEPA + Bizum for Spain, international cards, etc.)
    stripe_secret_key: str | None = Field(default=None, alias='STRIPE_SECRET_KEY')
    stripe_webhook_secret: str | None = Field(default=None, alias='STRIPE_WEBHOOK_SECRET')
    stripe_success_url: str = Field(default='http://localhost:3000/billing?checkout=success', alias='STRIPE_SUCCESS_URL')
    stripe_cancel_url: str = Field(default='http://localhost:3000/billing?checkout=cancelled', alias='STRIPE_CANCEL_URL')
    # Payment methods offered at Stripe Checkout. Spain-friendly defaults.
    stripe_payment_method_types: str = Field(default='card,sepa_debit,bizum,paypal', alias='STRIPE_PAYMENT_METHOD_TYPES')
    stripe_price_basic_monthly: str | None = Field(default=None, alias='STRIPE_PRICE_BASIC_MONTHLY')
    stripe_price_pro_monthly: str | None = Field(default=None, alias='STRIPE_PRICE_PRO_MONTHLY')
    stripe_price_premium_monthly: str | None = Field(default=None, alias='STRIPE_PRICE_PREMIUM_MONTHLY')

    # PayPal (international subscriptions where card/SEPA is not preferred)
    paypal_client_id: str | None = Field(default=None, alias='PAYPAL_CLIENT_ID')
    paypal_client_secret: str | None = Field(default=None, alias='PAYPAL_CLIENT_SECRET')
    paypal_webhook_id: str | None = Field(default=None, alias='PAYPAL_WEBHOOK_ID')
    paypal_env: str = Field(default='sandbox', alias='PAYPAL_ENV')  # sandbox | live

    # Telegram Payments (used inside the Telegram Mini App / bot)
    # Provider token issued by @BotFather via a PSP (e.g. Stripe TEST, YooKassa, etc.)
    telegram_payment_provider_token: str | None = Field(default=None, alias='TELEGRAM_PAYMENT_PROVIDER_TOKEN')
    telegram_payment_currency: str = Field(default='EUR', alias='TELEGRAM_PAYMENT_CURRENCY')

    # Redsys / Bizum (Spanish acquiring banks) — optional native integration.
    # Left as configuration hooks; Stripe already covers Bizum for most cases.
    redsys_merchant_code: str | None = Field(default=None, alias='REDSYS_MERCHANT_CODE')
    redsys_secret_key: str | None = Field(default=None, alias='REDSYS_SECRET_KEY')
    redsys_terminal: str = Field(default='1', alias='REDSYS_TERMINAL')
    redsys_env: str = Field(default='test', alias='REDSYS_ENV')  # test | live

    admin_bootstrap_email: str | None = Field(default=None, alias='ADMIN_BOOTSTRAP_EMAIL')
    admin_bootstrap_password: str | None = Field(default=None, alias='ADMIN_BOOTSTRAP_PASSWORD')

    cloudwatch_log_group: str | None = Field(default=None, alias='CLOUDWATCH_LOG_GROUP')

    telegram_bot_token: str | None = Field(default=None, alias='TELEGRAM_BOT_TOKEN')
    telegram_webapp_url: str | None = Field(default=None, alias='TELEGRAM_WEBAPP_URL')

    license_server_url: str | None = Field(default=None, alias='LICENSE_SERVER_URL')
    license_public_key: str | None = Field(default=None, alias='LICENSE_PUBLIC_KEY')
    self_hosted_mode: bool = Field(default=False, alias='SELF_HOSTED_MODE')

    # ---- Uploads / extraction ----
    upload_dir: str = Field(default='./var/uploads', alias='UPLOAD_DIR')
    max_upload_mb: int = Field(default=25, alias='MAX_UPLOAD_MB')

    # --- Security: upload malware scanning (ClamAV) ---
    malware_scan_enabled: bool = Field(default=False, alias='MALWARE_SCAN_ENABLED')
    clamav_host: str = Field(default='clamav', alias='CLAMAV_HOST')
    clamav_port: int = Field(default=3310, alias='CLAMAV_PORT')
    clamav_timeout_seconds: int = Field(default=30, alias='CLAMAV_TIMEOUT_SECONDS')
    # If the scanner is unreachable: True = reject uploads (fail closed), False = allow with a warning.
    malware_scan_fail_closed: bool = Field(default=False, alias='MALWARE_SCAN_FAIL_CLOSED')
    max_lesson_input_chars: int = Field(default=12000, alias='MAX_LESSON_INPUT_CHARS')

    cors_origins: str = Field(default='http://localhost:3000', alias='CORS_ORIGINS')

    @property
    def cors_origin_list(self) -> list[str]:
        return [origin.strip() for origin in self.cors_origins.split(',') if origin.strip()]

    @property
    def supported_locale_list(self) -> list[str]:
        return [x.strip() for x in self.supported_locales.split(',') if x.strip()]

    @property
    def rtl_locale_list(self) -> list[str]:
        return [x.strip() for x in self.rtl_locales.split(',') if x.strip()]

    @property
    def payment_provider_list(self) -> list[str]:
        return [x.strip() for x in self.payment_providers.split(',') if x.strip()]

    @property
    def stripe_payment_method_type_list(self) -> list[str]:
        return [x.strip() for x in self.stripe_payment_method_types.split(',') if x.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
