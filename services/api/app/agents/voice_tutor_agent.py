class VoiceTutorAgent:
    """MVP stub. Implement provider-specific logic here."""

    name = 'voice_tutor_agent'

    async def run(self, payload: dict) -> dict:
        return {'agent': self.name, 'status': 'stub', 'payload': payload}
