class TranscriptCleanerAgent:
    """MVP stub. Implement provider-specific logic here."""

    name = 'transcript_cleaner_agent'

    async def run(self, payload: dict) -> dict:
        return {'agent': self.name, 'status': 'stub', 'payload': payload}
