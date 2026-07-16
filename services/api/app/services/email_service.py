class EmailService:
    """Service stub for email_service."""

    async def health(self) -> dict:
        return {'service': 'email_service', 'status': 'ok'}
