"""Original diagnostic items (license-clean). Answer keys stay server-side.

A short adaptive-ish set spanning A1->B2 so the multiple-choice part gives a rough
band; the writing (and optional speaking) sample is assessed by the AI gateway.
"""

# Each: id, level, skill, prompt (Spanish), options, answer (index), explanation key optional.
QUESTIONS = [
    {'id': 'q1', 'level': 'A1', 'skill': 'ser/estar', 'prompt': 'Yo ___ estudiante.', 'options': ['soy', 'estoy', 'es', 'está'], 'answer': 0},
    {'id': 'q2', 'level': 'A1', 'skill': 'artículos', 'prompt': '___ casa es grande.', 'options': ['El', 'La', 'Los', 'Un'], 'answer': 1},
    {'id': 'q3', 'level': 'A2', 'skill': 'pretérito', 'prompt': 'Ayer ___ al cine.', 'options': ['voy', 'fui', 'iba', 'iré'], 'answer': 1},
    {'id': 'q4', 'level': 'A2', 'skill': 'gustar', 'prompt': 'A mí me ___ los libros.', 'options': ['gusta', 'gustan', 'gusto', 'gustas'], 'answer': 1},
    {'id': 'q5', 'level': 'B1', 'skill': 'subjuntivo', 'prompt': 'Espero que ___ bien.', 'options': ['estás', 'estar', 'estés', 'estarás'], 'answer': 2},
    {'id': 'q6', 'level': 'B1', 'skill': 'por/para', 'prompt': 'Estudio español ___ mi trabajo.', 'options': ['por', 'para', 'de', 'en'], 'answer': 1},
    {'id': 'q7', 'level': 'B2', 'skill': 'condicional', 'prompt': 'Si tuviera tiempo, ___ más.', 'options': ['viajo', 'viajaré', 'viajaría', 'viajara'], 'answer': 2},
    {'id': 'q8', 'level': 'B2', 'skill': 'conectores', 'prompt': 'No vino, ___ estaba enfermo.', 'options': ['aunque', 'puesto que', 'para que', 'a menos que'], 'answer': 1},
]

WRITING_PROMPT = {
    'es': 'Escribe 3-5 frases sobre ti: quién eres, qué haces y por qué aprendes español.',
    'ru': 'Напишите 3-5 предложений по-испански о себе: кто вы, чем занимаетесь и зачем учите испанский.',
    'uk': 'Напишіть 3-5 речень іспанською про себе: хто ви, чим займаєтесь і навіщо вчите іспанську.',
    'ar': 'اكتب 3-5 جمل بالإسبانية عن نفسك: من أنت، وماذا تفعل، ولماذا تتعلم الإسبانية.',
    'fr': "Écris 3 à 5 phrases en espagnol sur toi : qui tu es, ce que tu fais et pourquoi tu apprends l'espagnol.",
    'en': 'Write 3-5 sentences in Spanish about yourself: who you are, what you do, and why you learn Spanish.',
}

SPEAKING_PROMPT = {
    'es': 'Habla 20-30 segundos: preséntate y describe tu día.',
    'ru': 'Говорите 20-30 секунд по-испански: представьтесь и опишите свой день.',
    'uk': 'Говоріть 20-30 секунд іспанською: представтесь і опишіть свій день.',
    'ar': 'تحدّث 20-30 ثانية بالإسبانية: عرّف بنفسك وصف يومك.',
    'fr': "Parle 20 à 30 secondes en espagnol : présente-toi et décris ta journée.",
    'en': 'Speak 20-30 seconds in Spanish: introduce yourself and describe your day.',
}

_ANSWER_KEY = {q['id']: q['answer'] for q in QUESTIONS}


def public_questions() -> list[dict]:
    """Questions without the answer key (safe to send to the client)."""
    return [{'id': q['id'], 'level': q['level'], 'skill': q['skill'], 'prompt': q['prompt'], 'options': q['options']} for q in QUESTIONS]


def score_answers(answers: list[dict]) -> dict:
    """answers: [{id, answer}] where answer is the chosen option index or text.
    Returns {correct, total, ratio, per_skill}."""
    correct = 0
    per_skill: dict[str, list[int]] = {}
    by_id = {q['id']: q for q in QUESTIONS}
    for a in answers or []:
        qid = a.get('id')
        q = by_id.get(qid)
        if not q:
            continue
        chosen = a.get('answer')
        ok = False
        if isinstance(chosen, int):
            ok = chosen == _ANSWER_KEY.get(qid)
        elif isinstance(chosen, str) and chosen.strip():
            # allow the literal option text
            try:
                ok = q['options'].index(chosen) == _ANSWER_KEY.get(qid)
            except ValueError:
                ok = False
        correct += 1 if ok else 0
        per_skill.setdefault(q['skill'], []).append(1 if ok else 0)
    total = len([a for a in (answers or []) if a.get('id') in by_id])
    return {
        'correct': correct,
        'total': total,
        'ratio': (correct / total) if total else 0.0,
        'per_skill': {k: sum(v) / len(v) for k, v in per_skill.items()},
    }
