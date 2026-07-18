"""One call the upload routes make right after reading file bytes:
scan for malware and reject infected files."""
from __future__ import annotations

import logging

from fastapi import HTTPException, status

from app.core.config import get_settings
from app.services.security.clamav_service import ScannerUnavailable, scan_bytes

logger = logging.getLogger(__name__)
settings = get_settings()


def scan_upload_or_raise(data: bytes, filename: str = 'upload') -> None:
    """No-op when scanning is disabled. Raises 422 if a threat is found; on scanner
    outage, raises 503 when fail-closed, otherwise logs and allows."""
    if not settings.malware_scan_enabled or not data:
        return
    try:
        result = scan_bytes(data)
    except ScannerUnavailable as exc:
        logger.warning('Malware scanner unavailable for %s: %s', filename, exc)
        if settings.malware_scan_fail_closed:
            raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                                detail='Security scanner unavailable; upload rejected.') from exc
        return
    if not result.clean:
        logger.warning('Malware detected in upload %s: %s', filename, result.signature)
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail=f'File rejected: security scan flagged it ({result.signature}).')
