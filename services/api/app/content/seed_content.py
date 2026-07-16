"""Original, license-clean seed content for the course.

IMPORTANT (copyright): This file contains ONLY original example material written
for the platform. It deliberately does NOT reproduce any copyrighted textbook
(e.g. Vinogradov's "Español" / задачник). To ship licensed textbook content,
import it through the content pipeline once you hold the rights — see
docs/CONTENT_LICENSING.md. CEFR "can-do" level descriptors below are short
original summaries, not quotations of the Council of Europe text.
"""

# CEFR levels A1..C2 with short original descriptions (localized).
CEFR_LEVELS = [
    {'code': 'A1', 'sort': 1, 'title': {'es': 'Principiante', 'ru': 'Начальный', 'uk': 'Початковий', 'ar': 'مبتدئ', 'fr': 'Débutant', 'en': 'Beginner'}},
    {'code': 'A2', 'sort': 2, 'title': {'es': 'Elemental', 'ru': 'Элементарный', 'uk': 'Елементарний', 'ar': 'أساسي', 'fr': 'Élémentaire', 'en': 'Elementary'}},
    {'code': 'B1', 'sort': 3, 'title': {'es': 'Intermedio', 'ru': 'Средний', 'uk': 'Середній', 'ar': 'متوسط', 'fr': 'Intermédiaire', 'en': 'Intermediate'}},
    {'code': 'B2', 'sort': 4, 'title': {'es': 'Intermedio alto', 'ru': 'Выше среднего', 'uk': 'Вище середнього', 'ar': 'فوق المتوسط', 'fr': 'Intermédiaire avancé', 'en': 'Upper-Intermediate'}},
    {'code': 'C1', 'sort': 5, 'title': {'es': 'Avanzado', 'ru': 'Продвинутый', 'uk': 'Просунутий', 'ar': 'متقدم', 'fr': 'Avancé', 'en': 'Advanced'}},
    {'code': 'C2', 'sort': 6, 'title': {'es': 'Maestría', 'ru': 'В совершенстве', 'uk': 'Досконалий', 'ar': 'إتقان', 'fr': 'Maîtrise', 'en': 'Proficiency'}},
]

# A few original A1 lessons. `explanations` are keyed by native language so the
# Grammar Agent can serve the learner's own language (RU/UK/AR/FR/ES/EN).
SAMPLE_LESSONS = [
    {
        'level': 'A1',
        'module': {'es': 'Primeros pasos', 'ru': 'Первые шаги', 'uk': 'Перші кроки', 'ar': 'الخطوات الأولى', 'fr': 'Premiers pas'},
        'title': 'Saludos y presentaciones',
        'topic': {'es': 'Saludar y presentarse', 'ru': 'Приветствие и знакомство', 'uk': 'Привітання та знайомство', 'ar': 'التحية والتعريف بالنفس', 'fr': 'Saluer et se présenter'},
        'vocabulary': [
            {'es': 'hola', 'ru': 'привет', 'uk': 'привіт', 'ar': 'مرحبا', 'fr': 'bonjour'},
            {'es': 'buenos días', 'ru': 'доброе утро', 'uk': 'доброго ранку', 'ar': 'صباح الخير', 'fr': 'bonjour (matin)'},
            {'es': 'me llamo', 'ru': 'меня зовут', 'uk': 'мене звати', 'ar': 'اسمي', 'fr': "je m'appelle"},
            {'es': 'gracias', 'ru': 'спасибо', 'uk': 'дякую', 'ar': 'شكرا', 'fr': 'merci'},
        ],
        'grammar_topic': 'verbo "llamarse" (presente)',
        'explanations': {
            'ru': 'Глагол llamarse — возвратный: me llamo (меня зовут), te llamas (тебя зовут), se llama (его/её зовут).',
            'uk': 'Дієслово llamarse — зворотне: me llamo (мене звати), te llamas (тебе звати), se llama (його/її звати).',
            'ar': 'الفعل llamarse فعل انعكاسي: me llamo (اسمي)، te llamas (اسمك)، se llama (اسمه/اسمها).',
            'fr': "Le verbe llamarse est pronominal : me llamo (je m'appelle), te llamas (tu t'appelles), se llama (il/elle s'appelle).",
            'es': 'El verbo llamarse es reflexivo: me llamo, te llamas, se llama.',
            'en': 'The verb llamarse is reflexive: me llamo (my name is), te llamas, se llama.',
        },
        'dialogue': ['— Hola, ¿cómo te llamas?', '— Me llamo Ana. ¿Y tú?', '— Me llamo Diego. Mucho gusto.'],
    },
    {
        'level': 'A1',
        'module': {'es': 'Primeros pasos', 'ru': 'Первые шаги', 'uk': 'Перші кроки', 'ar': 'الخطوات الأولى', 'fr': 'Premiers pas'},
        'title': 'Ser y estar',
        'topic': {'es': 'Los verbos ser y estar', 'ru': 'Глаголы ser и estar', 'uk': 'Дієслова ser та estar', 'ar': 'الفعلان ser و estar', 'fr': 'Les verbes ser et estar'},
        'vocabulary': [
            {'es': 'soy', 'ru': 'я есть (ser)', 'uk': 'я є (ser)', 'ar': 'أنا (ser)', 'fr': 'je suis (ser)'},
            {'es': 'estoy', 'ru': 'я нахожусь (estar)', 'uk': 'я перебуваю (estar)', 'ar': 'أنا (estar)', 'fr': 'je suis (estar)'},
            {'es': 'cansado', 'ru': 'усталый', 'uk': 'втомлений', 'ar': 'متعب', 'fr': 'fatigué'},
        ],
        'grammar_topic': 'ser vs estar',
        'explanations': {
            'ru': 'Ser — постоянные признаки (Soy médico). Estar — состояние/местоположение (Estoy cansado, Estoy en casa).',
            'uk': 'Ser — постійні ознаки (Soy médico). Estar — стан/місце (Estoy cansado, Estoy en casa).',
            'ar': 'ser للصفات الدائمة (Soy médico). estar للحالة/المكان (Estoy cansado، Estoy en casa).',
            'fr': "Ser pour l'essentiel/permanent (Soy médico). Estar pour l'état/le lieu (Estoy cansado, Estoy en casa).",
            'es': 'Ser: características permanentes. Estar: estado o lugar.',
            'en': 'Ser for permanent traits; estar for state/location.',
        },
        'dialogue': ['— ¿Cómo estás?', '— Estoy bien, gracias. ¿Y tú?', '— Estoy un poco cansado.'],
    },
]
