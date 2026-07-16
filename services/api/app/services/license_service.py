class LicenseService:
    """Service stub for license_service."""

    async def health(self) -> dict:
        return {'service': 'license_service', 'status': 'ok'}
