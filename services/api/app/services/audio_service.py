class AudioService:
    """Service stub for audio_service."""

    async def health(self) -> dict:
        return {'service': 'audio_service', 'status': 'ok'}
