class DiagnosticAgent:
    """MVP stub. Implement provider-specific logic here."""

    name = 'diagnostic_agent'

    async def run(self, payload: dict) -> dict:
        return {'agent': self.name, 'status': 'stub', 'payload': payload}
