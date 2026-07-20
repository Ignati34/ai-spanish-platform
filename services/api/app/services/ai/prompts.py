"""Localized prompt builders. Explanations are produced in the learner's own
native language (RU/UK/AR/FR/ES/EN), which is the platform's differentiator."""
from __future__ import annotations

LANG_NAMES = {
    'ru': 'Russian', 'uk': 'Ukrainian', 'ar': 'Arabic',
    'fr': 'French', 'es': 'Spanish', 'en': 'English',
}


from app.content.vocab_bank import enrichment_block


def lang_name(code: str) -> str:
    return LANG_NAMES.get((code or 'ru')[:2], 'Russian')


def _system(native_language: str) -> str:
    lang = lang_name(native_language)
    return (
        f'You are an expert teacher of Spanish (español) and a careful linguist. '
        f'Your student\'s native language is {lang}; write all translations and explanations in {lang}. '
        f'Be accurate about Spanish grammar. '
        f'Respond with ONE valid minified JSON object and nothing else — no prose, no markdown fences.'
    )


def analyze(text: str, native_language: str) -> tuple[str, str]:
    lang = lang_name(native_language)
    user = (
        'Analyze the Spanish text below. Return JSON with exactly these keys: '
        'cefr_estimate (one of "A1","A2","B1","B2","C1","C2"), '
        f'translation (a faithful, natural translation of the WHOLE text into {lang}), '
        'verbs (array of objects {"word","tense","translation"} where tense is the Spanish '
        f'tense name and translation is the infinitive meaning in {lang}), '
        'tenses (array of Spanish tense names actually used, e.g. "presente de indicativo", '
        '"pretérito indefinido"), '
        f'nouns (array of objects {{"word","translation"}} translated to {lang}), '
        f'adjectives (array of objects {{"word","translation"}} translated to {lang}), '
        f'adverbs (array of objects {{"word","translation"}} translated to {lang}), '
        'conjunctions (array of strings), '
        f'vocabulary (array of objects {{"word","translation","cefr"}} where translation is in {lang}), '
        'grammar_topics (array of strings), '
        f'summary (one short paragraph in {lang}). '
        'Keep the "word" fields exactly as they appear in Spanish (lemmatize verbs to the '
        'infinitive). '
        f'Text:\n"""{text}"""'
    )
    return _system(native_language), user


def flashcards(text: str, native_language: str, cefr_level: str, max_cards: int = 12,
               source_language: str = 'es') -> tuple[str, str]:
    lang = lang_name(native_language)
    if source_language and source_language != 'es':
        src = lang_name(source_language)
        origin = (
            f'The input is in {src} (NOT Spanish). First translate each word/phrase into natural '
            f'Spanish, then build the card. '
        )
    else:
        origin = 'The input is Spanish. '
    user = (
        f'Create up to {max_cards} study flashcards for a {cefr_level} learner. {origin}'
        'Return JSON {"deck_title", "cards": [{"front","back","card_type","example_sentence"}]}. '
        f'front = Spanish; back = translation/explanation in {lang}; '
        'card_type one of "word_translation","phrase","verb_conjugation"; '
        'example_sentence = a short Spanish sentence using the word. '
        f'Input:\n"""{text}"""'
    )
    return _system(native_language), user


def exercises(text: str, native_language: str, cefr_level: str) -> tuple[str, str]:
    lang = lang_name(native_language)
    user = (
        f'Create 4-6 exercises for a {cefr_level} learner based on the Spanish text. '
        'Return JSON {"exercises": [{"exercise_type","prompt","options","correct_answer","explanation"}]}. '
        'exercise_type one of "multiple_choice","fill_blank","translation"; '
        'options = array of strings (or null for translation); '
        f'explanation in {lang}. '
        f'Text:\n"""{text}"""'
    )
    return _system(native_language), user


def check(answer: str, correct_answer: str | None, native_language: str) -> tuple[str, str]:
    lang = lang_name(native_language)
    user = (
        'A learner answered a Spanish exercise. '
        f'Correct answer: "{correct_answer}". Learner answer: "{answer}". '
        'Return JSON {"is_correct": bool, "score": number between 0 and 1, "feedback"}. '
        f'feedback in {lang}, concise, explaining the mistake if any.'
    )
    return _system(native_language), user


def voice_reply(history: list[dict], user_message: str, scenario: str, cefr_level: str, native_language: str) -> tuple[str, str]:
    lang = lang_name(native_language)
    system = (
        f'You are a friendly Spanish conversation tutor roleplaying the scenario "{scenario}". '
        f'The student\'s level is {cefr_level} and their native language is {lang}. '
        f'Speak natural Spanish appropriate to {cefr_level}; keep your reply short (1-3 sentences). '
        f'Gently correct the student\'s last message only if it has real errors, and write that '
        f'correction in {lang}. Respond with ONE valid minified JSON object and nothing else.'
            + enrichment_block(n_verbs=5, n_phrases=6, n_examples=2)
    )
    convo = '\n'.join(f'{m.get("role")}: {m.get("text")}' for m in (history or [])[-8:])
    user = (
        'Conversation so far:\n' + (convo or '(empty)') + '\n\n'
        f'Student just said: "{user_message}"\n\n'
        'Return JSON {"reply_es": "<your Spanish reply>", '
        f'"correction": "<short correction in {lang}, empty string if none>", '
        '"score": <number 0..1 rating the student\'s last message>}.'
    )
    return system, user


def assess_level(writing_sample: str, speaking_sample: str, mc_summary: dict, native_language: str) -> tuple[str, str]:
    lang = lang_name(native_language)
    system = (
        'You are a CEFR examiner for Spanish. Estimate the learner\'s level from their '
        'multiple-choice performance and their free production (writing / speaking sample). '
        f'Write strengths, gaps, summary and the study plan in {lang}. '
        'Respond with ONE valid minified JSON object and nothing else.'
    )
    user = (
        f'Multiple-choice result: {mc_summary}\n\n'
        f'Writing sample (Spanish): """{writing_sample or "(none)"}"""\n\n'
        f'Speaking sample transcript (Spanish): """{speaking_sample or "(none)"}"""\n\n'
        'Return JSON {"cefr_estimate": one of "A1".."C2", "recommended_level": one of "A1".."C2", '
        f'"strengths": [up to 4 strings in {lang}], "gaps": [up to 4 strings in {lang}], '
        f'"summary": "2-3 sentences in {lang}", '
        f'"study_plan": [3-5 short next-step strings in {lang}]}}.'
    )
    return system, user


def targeted_exercises(topics: list[str], cefr_level: str, native_language: str) -> tuple[str, str]:
    lang = lang_name(native_language)
    topic_str = ', '.join(topics) if topics else 'general Spanish grammar'
    system = (
        'You are a Spanish teacher creating focused remedial practice. '
        f'Target the student\'s weak areas. Explanations in {lang}. '
        'Respond with ONE valid minified JSON object and nothing else.'
            + enrichment_block(n_verbs=6, n_phrases=3, n_examples=2)
    )
    user = (
        f'Create focused remedial practice for a {cefr_level} learner on: {topic_str}. '
        'Return ONE JSON object with two keys: '
        '"vocabulary": [6-8 useful Spanish words/phrases for these topics, each '
        '{"word": "<Spanish>", "translation": "<in %s>", "example": "<a natural Spanish '
        'sentence using the word>"}], and '
        '"exercises": [5 items {"exercise_type","prompt","options","correct_answer","explanation"}]. '
        'exercise_type one of "multiple_choice","fill_blank","translation"; options = array or null; '
        'explanation in %s and concrete (say WHY, with a short example).'
    ) % (lang, lang)
    return system, user


def simulation_turn(history: list[dict], user_message: str, role: str, goal_es: str,
                    cefr_level: str, native_language: str) -> tuple[str, str]:
    lang = lang_name(native_language)
    system = (
        f'You are role-playing as "{role}" in a Spanish practice simulation. '
        f'Stay in character and speak natural Spanish for a {cefr_level} learner (short turns). '
        f'The learner\'s native language is {lang}. Goal of the simulation: {goal_es} '
        f'Judge whether that goal has now been achieved in the conversation. '
        f'Correct only real errors, in {lang}. Respond with ONE valid minified JSON object and nothing else.'
        + enrichment_block(n_verbs=6, n_phrases=6, n_examples=2)
    )
    convo = '\n'.join(f'{m.get("role")}: {m.get("text")}' for m in (history or [])[-10:])
    user = (
        'Conversation so far:\n' + (convo or '(empty)') + '\n\n'
        f'Student just said: "{user_message}"\n\n'
        'Return JSON {"reply_es": "<in-character Spanish reply>", '
        f'"correction": "<short correction in {lang}, empty if none>", '
        '"score": <0..1 for the student\'s last message>, '
        '"goal_met": <true|false>, '
        '"hint": "<a short Spanish phrase the student could try next, empty if none>"}.'
    )
    return system, user


def image_ocr_instruction() -> str:
    return ('Extract ALL text visible in this image exactly as written (any language). '
            'Return only the extracted text, no commentary.')


def generate_lesson(topic_es: str, topic_native: str, cefr_level: str, native_language: str,
                    focus: str = '') -> tuple[str, str]:
    lang = lang_name(native_language)
    system = (
        f'You are an expert Spanish curriculum author writing for {cefr_level} learners whose '
        f'native language is {lang}. Write clear, original teaching content in {lang} with Spanish '
        f'examples. Do NOT copy any textbook; explain the grammar facts in your own words. '
        f'Respond with ONE valid minified JSON object and nothing else.'
            + enrichment_block(n_verbs=8, n_phrases=4, n_examples=3)
    )
    user = (
        f'Write a complete lesson on: "{topic_es}" ({topic_native}). {("Focus: " + focus + ". ") if focus else ""}'
        f'Return JSON {{"title": "<concise title>", '
        f'"theory": "<250-500 words of clear explanation in {lang} with Spanish examples; use \\n for line breaks>", '
        '"exercises": [at least 4 items {"exercise_type","prompt","options","correct_answer","explanation"}]}. '
        'exercise_type one of "multiple_choice","fill_blank","translation"; options = array of strings '
        '(or null for translation); correct_answer MUST exactly equal one option when options are given; '
        f'explanation in {lang}. Make exercises concrete and varied.'
    )
    return system, user


def translate_theory(text: str, target_language: str, source_language: str = 'ru') -> tuple[str, str]:
    """Translate a lesson's grammar theory into the target language while keeping
    the Spanish examples intact and the layout unchanged."""
    src = lang_name(source_language)
    tgt = lang_name(target_language)
    system = (
        f'You are a professional translator specializing in Spanish-language teaching materials. '
        f'You translate explanatory text from {src} into {tgt} for adult Spanish learners.'
    )
    user = (
        f'Translate the following Spanish grammar lesson from {src} into {tgt}.\n'
        f'Strict rules:\n'
        f'1) Keep every Spanish example EXACTLY as written (words, accents, punctuation) — do NOT translate the Spanish.\n'
        f'2) Translate the {src} explanations and the parenthetical glosses that explain the Spanish.\n'
        f'3) Preserve the structure verbatim: numbered points, bullet symbols, line breaks, the "МИНИ-ДИАЛОГ"/dialogue section and its dashes.\n'
        f'4) Keep grammar terms accurate and natural in {tgt}.\n'
        f'5) Output ONLY the translated text — no preamble, no notes, no markdown fences.\n\n'
        f'TEXT:\n{text}'
    )
    return system, user


def dialogue(topic: str, cefr_level: str, native_language: str) -> tuple[str, str]:
    """Generate a short, level-appropriate two-speaker dialogue on a topic.
    Total Spanish is capped (~500 characters) so it stays a quick read."""
    lang = lang_name(native_language)
    system = (
        f'You are a Spanish teacher creating a short practice dialogue for a {cefr_level} learner '
        f'whose native language is {lang}. Use vocabulary and grammar appropriate to {cefr_level} '
        f'(simple at A1, richer and more idiomatic toward C2). Respond with ONE valid minified JSON '
        f'object and nothing else.'
    )
    user = (
        f'Write a natural dialogue between two speakers about: "{topic}". '
        f'Return JSON {{"title": "<short Spanish title>", '
        f'"lines": [{{"speaker": "<name>", "es": "<Spanish line>", "translation": "<in {lang}>"}}]}}. '
        f'Rules: 5-8 turns; keep it {cefr_level}-appropriate; the TOTAL Spanish across all lines must '
        f'not exceed 500 characters; each line one short sentence; alternate the two speakers.'
    )
    return system, user
