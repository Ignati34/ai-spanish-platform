"""Minimal object storage: local disk by default, S3/MinIO when configured.

Keeps the pipeline runnable with zero cloud setup (self-hosted/desktop) while
allowing a real S3/MinIO bucket in production via boto3.
"""
from __future__ import annotations

import os
import uuid

from app.core.config import get_settings

settings = get_settings()


class StorageService:
    async def health(self) -> dict:
        return {'service': 'storage_service', 'status': 'ok', 'backend': self._backend()}

    def _backend(self) -> str:
        return 's3' if self._s3_ready() else 'local'

    def _s3_ready(self) -> bool:
        try:
            import boto3  # noqa: F401
            return bool(settings.s3_endpoint and settings.s3_bucket_uploads)
        except Exception:
            return False

    def save(self, user_id, filename: str, data: bytes, content_type: str | None = None) -> str:
        """Persist bytes; return a storage URL/key recorded on UploadedFile."""
        safe = os.path.basename(filename).replace(' ', '_')
        key = f'uploads/{user_id}/{uuid.uuid4().hex}_{safe}'
        # Try S3/MinIO first if usable.
        if self._s3_ready():
            try:
                import boto3
                client = boto3.client(
                    's3', endpoint_url=settings.s3_endpoint,
                    aws_access_key_id=settings.s3_access_key, aws_secret_access_key=settings.s3_secret_key,
                    region_name=settings.s3_region,
                )
                client.put_object(Bucket=settings.s3_bucket_uploads, Key=key, Body=data, ContentType=content_type or 'application/octet-stream')
                return f's3://{settings.s3_bucket_uploads}/{key}'
            except Exception:
                pass  # fall through to local
        # Local disk fallback.
        path = os.path.join(settings.upload_dir, key)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as fh:
            fh.write(data)
        return f'file://{os.path.abspath(path)}'


storage_service = StorageService()
