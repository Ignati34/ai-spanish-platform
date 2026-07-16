from app.services.ai_gateway import AIGateway


class AgentOrchestrator:
    def __init__(self, ai_gateway: AIGateway | None = None):
        self.ai = ai_gateway or AIGateway()

    async def analyze_text(self, text: str, native_language: str = 'ru') -> dict:
        return await self.ai.analyze_text(text=text, native_language=native_language)

    async def generate_flashcards(self, text: str, native_language: str = 'ru', cefr_level: str = 'A1') -> dict:
        return await self.ai.generate_flashcards(text=text, native_language=native_language, cefr_level=cefr_level)

    async def generate_exercises(self, text: str, cefr_level: str = 'A1', native_language: str = 'ru') -> dict:
        return await self.ai.generate_exercises(text=text, cefr_level=cefr_level, native_language=native_language)

    async def check_answer(self, answer: str, correct_answer: str | None = None) -> dict:
        return await self.ai.check_answer(answer=answer, correct_answer=correct_answer)

    async def transcribe(self, data: bytes, filename: str, language: str = 'es') -> dict:
        return await self.ai.transcribe_audio(data=data, filename=filename, language=language)

    async def voice_reply(self, history, user_message, scenario='restaurant', cefr_level='A1', native_language='ru') -> dict:
        return await self.ai.voice_reply(history, user_message, scenario, cefr_level, native_language)

    async def synthesize(self, text: str, voice: str | None = None, language: str = 'es') -> bytes:
        return await self.ai.synthesize_speech(text=text, voice=voice, language=language)

    async def assess_level(self, writing_sample: str, speaking_sample: str, mc_summary: dict, native_language: str = 'ru') -> dict:
        return await self.ai.assess_level(writing_sample, speaking_sample, mc_summary, native_language)

    async def targeted_exercises(self, topics, cefr_level='A1', native_language='ru') -> dict:
        return await self.ai.targeted_exercises(topics, cefr_level, native_language)

    async def simulation_turn(self, history, user_message, role, goal_es, cefr_level='A1', native_language='ru') -> dict:
        return await self.ai.simulation_turn(history, user_message, role, goal_es, cefr_level, native_language)
