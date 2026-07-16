class VocabularyAgent:
    """MVP stub. Implement provider-specific logic here."""

    name = 'vocabulary_agent'

    async def run(self, payload: dict) -> dict:
        return {'agent': self.name, 'status': 'stub', 'payload': payload}
