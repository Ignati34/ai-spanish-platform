class VideoService:
    """Service stub for video_service."""

    async def health(self) -> dict:
        return {'service': 'video_service', 'status': 'ok'}
