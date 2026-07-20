# -*- coding: utf-8 -*-
"""Short, localized explanations of Spanish tenses with examples.

Used to enrich text-analysis results: each detected tense gets a small popover with a
one-line explanation (in the learner's language) and a couple of Spanish examples. Static
data — no LLM call, instant in the UI. Explanations are original.
"""
from __future__ import annotations

import unicodedata

_LANGS = ('ru', 'uk', 'ar', 'fr', 'es', 'en')

# key -> {examples: [es...], explanation: {lang: str}}
TENSES: dict[str, dict] = {
    'presente': {
        'examples': ['Hablo español todos los días.', 'Ella vive en Madrid.'],
        'explanation': {
            'ru': 'Настоящее время: действия сейчас, привычные и общие истины.',
            'uk': 'Теперішній час: дії зараз, звичні та загальні істини.',
            'ar': 'المضارع: أفعال تحدث الآن، عادات وحقائق عامة.',
            'fr': 'Présent : actions actuelles, habitudes et vérités générales.',
            'es': 'Presente: acciones actuales, hábitos y verdades generales.',
            'en': 'Present: current actions, habits and general truths.',
        },
    },
    'preterito_perfecto': {
        'examples': ['Hoy he comido paella.', '¿Has visto la película?'],
        'explanation': {
            'ru': 'Pretérito perfecto: недавнее прошлое, связанное с настоящим (haber + причастие).',
            'uk': 'Pretérito perfecto: недавнє минуле, повʼязане з теперішнім (haber + дієприкметник).',
            'ar': 'الماضي القريب المرتبط بالحاضر (haber + اسم المفعول).',
            'fr': 'Passé composé espagnol : passé récent lié au présent (haber + participe).',
            'es': 'Pretérito perfecto: pasado reciente ligado al presente (haber + participio).',
            'en': 'Present perfect: recent past connected to now (haber + participle).',
        },
    },
    'preterito_indefinido': {
        'examples': ['Ayer comí en casa.', 'Viajaron a Perú en 2019.'],
        'explanation': {
            'ru': 'Pretérito indefinido: завершённые действия в конкретный момент прошлого.',
            'uk': 'Pretérito indefinido: завершені дії в конкретний момент минулого.',
            'ar': 'الماضي البسيط: أفعال منتهية في وقت محدد من الماضي.',
            'fr': 'Passé simple : actions achevées à un moment précis du passé.',
            'es': 'Pretérito indefinido: acciones terminadas en un momento concreto del pasado.',
            'en': 'Preterite: completed actions at a specific past moment.',
        },
    },
    'preterito_imperfecto': {
        'examples': ['De niño jugaba en la calle.', 'Llovía y hacía frío.'],
        'explanation': {
            'ru': 'Pretérito imperfecto: привычки, описания и фон в прошлом («что делал обычно»).',
            'uk': 'Pretérito imperfecto: звички, описи та тло в минулому.',
            'ar': 'الماضي الناقص: العادات والأوصاف والخلفية في الماضي.',
            'fr': 'Imparfait : habitudes, descriptions et arrière-plan au passé.',
            'es': 'Pretérito imperfecto: hábitos, descripciones y fondo en el pasado.',
            'en': 'Imperfect: past habits, descriptions and background.',
        },
    },
    'preterito_pluscuamperfecto': {
        'examples': ['Cuando llegué, ya habían cenado.', 'Nunca había visto algo así.'],
        'explanation': {
            'ru': 'Pluscuamperfecto: действие ДО другого прошлого (había + причастие).',
            'uk': 'Pluscuamperfecto: дія ДО іншої минулої (había + дієприкметник).',
            'ar': 'الماضي التام: فعل وقع قبل فعل ماضٍ آخر (había + اسم المفعول).',
            'fr': 'Plus-que-parfait : action antérieure à un autre passé (había + participe).',
            'es': 'Pluscuamperfecto: acción anterior a otro pasado (había + participio).',
            'en': 'Past perfect: an action before another past one (había + participle).',
        },
    },
    'futuro': {
        'examples': ['Mañana iré al médico.', '¿Vendrás a la fiesta?'],
        'explanation': {
            'ru': 'Futuro simple: будущие действия и предположения о настоящем.',
            'uk': 'Futuro simple: майбутні дії та припущення про теперішнє.',
            'ar': 'المستقبل البسيط: أفعال مستقبلية وتخمينات عن الحاضر.',
            'fr': 'Futur simple : actions futures et suppositions sur le présent.',
            'es': 'Futuro simple: acciones futuras y suposiciones sobre el presente.',
            'en': 'Simple future: future actions and guesses about the present.',
        },
    },
    'futuro_perfecto': {
        'examples': ['Para junio habré terminado el curso.'],
        'explanation': {
            'ru': 'Futuro perfecto: действие, которое завершится к моменту в будущем.',
            'uk': 'Futuro perfecto: дія, що завершиться до певного моменту в майбутньому.',
            'ar': 'المستقبل التام: فعل سيكتمل قبل لحظة في المستقبل.',
            'fr': 'Futur antérieur : action achevée avant un moment futur.',
            'es': 'Futuro perfecto: acción acabada antes de un momento futuro.',
            'en': 'Future perfect: an action completed before a future moment.',
        },
    },
    'condicional': {
        'examples': ['Me gustaría un café.', '¿Podrías ayudarme?'],
        'explanation': {
            'ru': 'Condicional: вежливость, гипотезы и «бы» (что было бы).',
            'uk': 'Condicional: ввічливість, гіпотези та «би».',
            'ar': 'الشرطي: التأدب والافتراضات و«لو».',
            'fr': 'Conditionnel : politesse, hypothèses et « je ferais ».',
            'es': 'Condicional: cortesía, hipótesis y lo que pasaría.',
            'en': 'Conditional: politeness, hypotheses and “would”.',
        },
    },
    'condicional_perfecto': {
        'examples': ['Yo habría ido, pero no pude.'],
        'explanation': {
            'ru': 'Condicional perfecto: что бы произошло в прошлом (habría + причастие).',
            'uk': 'Condicional perfecto: що сталося б у минулому (habría + дієприкметник).',
            'ar': 'الشرطي التام: ما كان سيحدث في الماضي (habría + اسم المفعول).',
            'fr': 'Conditionnel passé : ce qui serait arrivé (habría + participe).',
            'es': 'Condicional perfecto: lo que habría pasado (habría + participio).',
            'en': 'Conditional perfect: what would have happened (habría + participle).',
        },
    },
    'presente_subjuntivo': {
        'examples': ['Espero que tengas razón.', 'Quiero que vengas.'],
        'explanation': {
            'ru': 'Presente de subjuntivo: желания, сомнения, оценки после que.',
            'uk': 'Presente de subjuntivo: бажання, сумніви, оцінки після que.',
            'ar': 'مضارع الشرط: الرغبات والشكوك والتقييمات بعد que.',
            'fr': 'Subjonctif présent : souhaits, doutes, jugements après que.',
            'es': 'Presente de subjuntivo: deseos, dudas y valoraciones tras que.',
            'en': 'Present subjunctive: wishes, doubts and judgments after que.',
        },
    },
    'imperfecto_subjuntivo': {
        'examples': ['Si tuviera tiempo, viajaría.', 'Ojalá pudiera ir.'],
        'explanation': {
            'ru': 'Imperfecto de subjuntivo: нереальные условия и «если бы».',
            'uk': 'Imperfecto de subjuntivo: нереальні умови та «якби».',
            'ar': 'ماضي الشرط: الشروط غير الواقعية و«لو».',
            'fr': 'Subjonctif imparfait : conditions irréelles et « si ».',
            'es': 'Imperfecto de subjuntivo: condiciones irreales y “si tuviera”.',
            'en': 'Imperfect subjunctive: unreal conditions and “if I were”.',
        },
    },
    'imperativo': {
        'examples': ['¡Habla más despacio!', 'Ven aquí, por favor.'],
        'explanation': {
            'ru': 'Imperativo: приказы, просьбы и советы.',
            'uk': 'Imperativo: накази, прохання та поради.',
            'ar': 'الأمر: الأوامر والطلبات والنصائح.',
            'fr': 'Impératif : ordres, demandes et conseils.',
            'es': 'Imperativo: órdenes, peticiones y consejos.',
            'en': 'Imperative: orders, requests and advice.',
        },
    },
    'presente_continuo': {
        'examples': ['Estoy estudiando ahora.', 'Están comiendo.'],
        'explanation': {
            'ru': 'Presente continuo (estar + герундий): действие прямо сейчас, в процессе.',
            'uk': 'Presente continuo (estar + герундій): дія саме зараз, у процесі.',
            'ar': 'المضارع المستمر (estar + الحال): فعل يجري الآن.',
            'fr': 'Présent continu (estar + gérondif) : action en cours maintenant.',
            'es': 'Presente continuo (estar + gerundio): acción en curso ahora.',
            'en': 'Present continuous (estar + gerund): action in progress now.',
        },
    },
}


def _norm(s: str) -> str:
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode('ascii')
    return s.lower().strip()


def classify(tense: str) -> str | None:
    """Map a free-form Spanish tense name to a guide key (or None)."""
    s = _norm(tense)
    if not s:
        return None
    has = lambda *ws: all(w in s for w in ws)
    if 'subjuntivo' in s:
        if 'imperfecto' in s or 'pasado' in s or 'pretecrito' in s:
            return 'imperfecto_subjuntivo'
        return 'presente_subjuntivo'
    if 'continuo' in s or 'progresivo' in s or 'gerundio' in s:
        return 'presente_continuo'
    if 'imperativo' in s or 'mandato' in s:
        return 'imperativo'
    if 'pluscuamperfecto' in s:
        return 'preterito_pluscuamperfecto'
    if 'condicional' in s:
        return 'condicional_perfecto' if ('perfecto' in s or 'compuesto' in s) else 'condicional'
    if 'futuro' in s:
        return 'futuro_perfecto' if ('perfecto' in s or 'compuesto' in s) else 'futuro'
    if 'imperfecto' in s:
        return 'preterito_imperfecto'
    if 'indefinido' in s or has('preterito', 'simple') or 'perfecto simple' in s:
        return 'preterito_indefinido'
    if 'perfecto' in s or 'compuesto' in s:
        return 'preterito_perfecto'
    if 'presente' in s:
        return 'presente'
    return None


def tense_info(tenses: list[str], native_language: str = 'ru') -> list[dict]:
    """For each recognized tense name, return {name, key, explanation, examples}.
    Deduplicated by key; unrecognized tenses are skipped."""
    lang = (native_language or 'ru')[:2].lower()
    if lang not in _LANGS:
        lang = 'en'
    out: list[dict] = []
    seen: set[str] = set()
    for name in tenses or []:
        key = classify(name if isinstance(name, str) else str(name))
        if not key or key in seen:
            continue
        seen.add(key)
        entry = TENSES[key]
        out.append({
            'name': name,
            'key': key,
            'explanation': entry['explanation'].get(lang) or entry['explanation'].get('en'),
            'examples': entry['examples'],
        })
    return out
