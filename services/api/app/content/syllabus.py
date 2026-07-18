"""Comprehensive Spanish syllabus (A1–C2), ~150 topics.

Only the *list of topics* (grammar facts) is encoded here — not any copyrighted prose.
It mirrors a standard CEFR morphology/syntax progression and the topic outline seen in
common courses (articles → nouns → adjectives → pronouns → the verb system → syntax →
individual conjugation & prepositional government). The AI lesson generator turns each
entry into an original lesson (theory + exercises).

Each entry: (level, es, ru, focus).
"""

_A1 = [
    ('Partes de la oración', 'Части речи', 'обзор существительного, глагола, прилагательного, артикля'),
    ('El artículo: función', 'Артикль и его функция', 'зачем нужен артикль'),
    ('Artículo indeterminado (un/una/unos/unas)', 'Неопределённый артикль', 'формы и базовое употребление'),
    ('Artículo determinado (el/la/los/las)', 'Определённый артикль', 'формы и базовое употребление'),
    ('El artículo neutro lo', 'Артикль среднего рода lo', 'lo + прилагательное'),
    ('Género del sustantivo', 'Род существительных', 'мужской/женский, исключения'),
    ('Número del sustantivo', 'Число существительных', 'образование множественного числа'),
    ('Concordancia del adjetivo', 'Согласование прилагательного', 'род и число'),
    ('Adjetivos demostrativos', 'Указательные прилагательные', 'este/ese/aquel'),
    ('Adjetivos posesivos', 'Притяжательные прилагательные', 'mi/tu/su...'),
    ('Pronombres personales sujeto', 'Личные местоимения-подлежащие', 'yo/tú/él...'),
    ('El verbo ser', 'Глагол ser', 'формы и употребление'),
    ('El verbo estar', 'Глагол estar', 'формы и употребление'),
    ('Ser vs estar', 'Ser и estar', 'базовое различие'),
    ('Presente de indicativo: verbos regulares', 'Настоящее время: правильные глаголы', '-ar/-er/-ir'),
    ('Hay (haber impersonal)', 'Оборот hay', 'наличие/существование'),
    ('Números cardinales', 'Количественные числительные', '0–100 и далее'),
    ('La interrogación', 'Вопросительные предложения', 'qué, quién, dónde, cómo'),
    ('La negación', 'Отрицание', 'no, nunca, nada, nadie'),
    ('El verbo gustar', 'Глагол gustar', 'me gusta/gustan'),
    ('La hora y la fecha', 'Время и дата', 'который час, дни, месяцы'),
    ('Presente: verbos irregulares comunes', 'Настоящее: частые неправильные', 'tener, ir, hacer, poder'),
    ('Preposiciones a y de', 'Предлоги a и de', 'направление, принадлежность'),
    ('Preposiciones en, con, para', 'Предлоги en, con, para', 'место, совместность, цель'),
    ('Adverbios de lugar y tiempo', 'Наречия места и времени', 'aquí, allí, hoy, ayer'),
]

_A2 = [
    ('Verbos con cambio vocálico (e>ie, o>ue)', 'Глаголы с чередованием гласной', 'querer, poder, dormir'),
    ('Verbos reflexivos', 'Возвратные глаголы', 'levantarse, ducharse'),
    ('Pronombres de objeto directo', 'Прямые дополнения-местоимения', 'lo/la/los/las'),
    ('Pronombres de objeto indirecto', 'Косвенные дополнения-местоимения', 'me/te/le/nos/os/les'),
    ('Combinación de pronombres', 'Сочетание местоимений', 'se lo, me la'),
    ('Pretérito indefinido: regulares', 'Indefinido: правильные', 'завершённое прошлое'),
    ('Pretérito indefinido: irregulares', 'Indefinido: неправильные', 'ser/ir, tener, hacer, decir'),
    ('Pretérito imperfecto', 'Imperfecto', 'фон, привычки в прошлом'),
    ('Indefinido vs imperfecto', 'Indefinido и imperfecto', 'выбор времени'),
    ('Futuro simple', 'Будущее время', 'формы и употребление'),
    ('Comparativos', 'Сравнительная степень', 'más/menos que, tan como'),
    ('Superlativos', 'Превосходная степень', 'el más, -ísimo'),
    ('Adverbios en -mente', 'Наречия на -mente', 'образование от прилагательных'),
    ('Perfecto (pretérito perfecto compuesto)', 'Present perfect', 'he hablado'),
    ('Estar + gerundio', 'Estar + герундий', 'настоящее длительное'),
    ('Imperativo afirmativo', 'Повелительное наклонение (утв.)', 'habla, come, vive'),
    ('Por y para (introducción)', 'Por и para (введение)', 'причина vs цель'),
    ('Preposiciones de tiempo', 'Предлоги времени', 'a, en, de, desde, hasta'),
    ('Pronombres posesivos', 'Притяжательные местоимения', 'el mío, la tuya'),
    ('Verbos como gustar', 'Глаголы типа gustar', 'encantar, doler, interesar'),
]

_B1 = [
    ('Presente de subjuntivo: formación', 'Presente de subjuntivo: образование', 'от 1 лица настоящего'),
    ('Subjuntivo: deseos y emociones', 'Subjuntivo: желания и эмоции', 'espero que, me alegro de que'),
    ('Subjuntivo: duda y negación', 'Subjuntivo: сомнение и отрицание', 'no creo que, dudo que'),
    ('Imperativo negativo', 'Повелительное (отриц.)', 'no hables, no comas'),
    ('Condicional simple', 'Условное наклонение', 'формы и вежливость'),
    ('Pluscuamperfecto', 'Предпрошедшее (pluscuamperfecto)', 'había hablado'),
    ('Pronombres relativos', 'Относительные местоимения', 'que, quien, el que, cuyo'),
    ('Por y para (avanzado)', 'Por и para (углублённо)', 'все значения'),
    ('Ser y estar (avanzado)', 'Ser и estar (углублённо)', 'с прилагательными, изменение смысла'),
    ('Estilo indirecto (presente)', 'Косвенная речь (наст.)', 'dice que...'),
    ('Conectores del discurso', 'Коннекторы речи', 'sin embargo, por lo tanto, aunque'),
    ('Verbos de cambio', 'Глаголы становления', 'ponerse, hacerse, volverse'),
    ('Perífrasis verbales', 'Глагольные перифразы', 'ir a, acabar de, volver a'),
    ('La voz pasiva', 'Страдательный залог', 'ser + participio'),
    ('Se impersonal y pasiva refleja', 'Безличное se и пассив', 'se dice, se venden'),
    ('Preposiciones: régimen básico', 'Управление предлогами (базово)', 'soñar con, pensar en'),
    ('Contraste de pasados', 'Сопоставление прошедших', 'indefinido/imperfecto/perfecto'),
    ('Oraciones temporales', 'Временные придаточные', 'cuando + subj/indic'),
]

_B2 = [
    ('Imperfecto de subjuntivo', 'Imperfecto de subjuntivo', 'hablara/hablase'),
    ('Oraciones condicionales (tipos)', 'Условные предложения (типы)', 'реальные и нереальные'),
    ('Subjuntivo en oraciones adverbiales', 'Subjuntivo в обстоятельственных', 'para que, aunque, a menos que'),
    ('Correlación de tiempos', 'Согласование времён', 'sequence of tenses'),
    ('Estilo indirecto (pasado)', 'Косвенная речь (прош.)', 'dijo que...'),
    ('Conectores avanzados', 'Продвинутые коннекторы', 'no obstante, puesto que, así que'),
    ('Perífrasis con infinitivo/gerundio/participio', 'Перифразы (инф./гер./прич.)', 'llevar + gerundio'),
    ('Usos del gerundio y participio', 'Употребление герундия и причастия', 'ограничения'),
    ('Futuro y condicional de probabilidad', 'Будущее/условное вероятности', 'serán las tres'),
    ('Cambios ortográficos: -car/-gar/-zar', 'Орфография: -car/-gar/-zar', 'ataqué, pagué, empecé'),
    ('Cambios ortográficos: -cer/-cir/-ger/-gir', 'Орфография: -cer/-cir/-ger/-gir', 'venzo, protejo'),
    ('Acentuación y tilde diacrítica', 'Ударение и различительный акцент', 'tú/tu, sí/si'),
    ('Oraciones concesivas', 'Уступительные предложения', 'aunque, a pesar de que'),
    ('Oraciones finales y causales', 'Целевые и причинные', 'para que, porque, ya que'),
    ('Verbos pronominales de significado', 'Местоименные глаголы (смысл)', 'irse vs ir, quedarse'),
]

_C = [
    ('El verbo Ser: conjugación completa', 'Глагол Ser: полное спряжение', 'все времена'),
    ('El verbo Estar: conjugación completa', 'Глагол Estar: полное спряжение', 'все времена'),
    ('Estar para vs estar por', 'Estar para и estar por', 'близость vs склонность'),
]

# Individual-conjugation verbs (each becomes a lesson) — facts, not prose.
_INDIVIDUAL_VERBS = [
    ('Ir', 'Идти/Ехать'), ('Hacer', 'Делать'), ('Decir', 'Говорить'), ('Tener', 'Иметь'),
    ('Venir', 'Приходить'), ('Poder', 'Мочь'), ('Poner', 'Класть'), ('Salir', 'Выходить'),
    ('Traer', 'Приносить'), ('Caer', 'Падать'), ('Oír', 'Слышать'), ('Ver', 'Видеть'),
    ('Dar', 'Давать'), ('Saber', 'Знать'), ('Querer', 'Хотеть'), ('Conocer', 'Быть знакомым'),
    ('Conducir', 'Вести (машину)'), ('Dormir', 'Спать'), ('Pedir', 'Просить'), ('Servir', 'Служить/Подавать'),
    ('Sentir', 'Чувствовать'), ('Jugar', 'Играть'), ('Valer', 'Стоить/Годиться'), ('Caber', 'Вмещаться'),
    ('Andar', 'Ходить'), ('Producir', 'Производить'),
]

# Verb + preposition government (each a lesson).
_VERB_GOVERNMENT = [
    ('contar con', 'рассчитывать на'), ('soñar con', 'мечтать о'), ('pensar en', 'думать о'),
    ('tardar en', 'медлить с'), ('insistir en', 'настаивать на'), ('depender de', 'зависеть от'),
    ('acordarse de', 'помнить о'), ('quejarse de', 'жаловаться на'), ('confiar en', 'доверять'),
    ('tratar de', 'пытаться'), ('consistir en', 'состоять в'), ('renunciar a', 'отказываться от'),
    ('atreverse a', 'осмеливаться'), ('enterarse de', 'узнавать о'), ('fijarse en', 'обращать внимание'),
    ('alegrarse de', 'радоваться'), ('preocuparse por', 'беспокоиться о'), ('despedirse de', 'прощаться'),
    ('convertirse en', 'превращаться в'), ('empeñarse en', 'упорствовать в'),
]

# Thematic vocabulary lessons (A1–A2).
_VOCAB = [
    ('A1', 'Saludos y presentaciones', 'Приветствия и знакомство'),
    ('A1', 'La familia', 'Семья'),
    ('A1', 'Los colores', 'Цвета'),
    ('A1', 'Los números y precios', 'Числа и цены'),
    ('A1', 'La comida y bebida', 'Еда и напитки'),
    ('A1', 'La casa y los muebles', 'Дом и мебель'),
    ('A2', 'La ropa', 'Одежда'),
    ('A2', 'El cuerpo y la salud', 'Тело и здоровье'),
    ('A2', 'La ciudad y direcciones', 'Город и как спросить дорогу'),
    ('A2', 'Los viajes y el transporte', 'Путешествия и транспорт'),
    ('A2', 'El trabajo y las profesiones', 'Работа и профессии'),
    ('A2', 'El tiempo y las estaciones', 'Погода и времена года'),
    ('A2', 'Las rutinas diarias', 'Ежедневные дела'),
    ('B1', 'Las emociones y el carácter', 'Эмоции и характер'),
    ('B1', 'La tecnología e internet', 'Технологии и интернет'),
]

_EXTRA_SYNTAX = [
    ('B2', 'Oraciones de relativo especificativas y explicativas', 'Определительные придаточные', 'запятая и смысл'),
    ('B2', 'La nominalización', 'Номинализация', 'lo que, el hecho de que'),
    ('C1', 'Marcadores del discurso formales', 'Формальные маркеры дискурса', 'по сути, в итоге'),
    ('C1', 'Registro formal e informal', 'Формальный и неформальный регистр', 'tú/usted, стиль'),
    ('C2', 'Matices de subjuntivo vs indicativo', 'Оттенки subjuntivo/indicativo', 'тонкие случаи'),
]

_ADJ_GOVERNMENT = [
    ('Régimen del adjetivo', 'Управление прилагательных', 'lleno de, capaz de, difícil de'),
    ('Malo, mayor y menor', 'Malo, mayor и menor', 'особые формы сравнения'),
]


def _build() -> list[dict]:
    out: list[dict] = []
    n = 0

    def add(level, es, ru, focus=''):
        nonlocal n
        n += 1
        out.append({'n': n, 'level': level, 'es': es, 'ru': ru, 'focus': focus})

    for es, ru, f in _A1:
        add('A1', es, ru, f)
    for es, ru, f in _A2:
        add('A2', es, ru, f)
    for es, ru, f in _B1:
        add('B1', es, ru, f)
    for es, ru, f in _B2:
        add('B2', es, ru, f)
    for es, ru, f in _C:
        add('C1', es, ru, f)
    for v_es, v_ru in _INDIVIDUAL_VERBS:
        add('C1', f'Conjugación individual: {v_es}', f'Индивидуальное спряжение: {v_ru}',
            'уникальные формы и употребление')
    for g_es, g_ru in _VERB_GOVERNMENT:
        add('C2', f'Régimen preposicional: {g_es}', f'Управление предлогом: {g_es} ({g_ru})',
            'предлог и значение')
    for es, ru, f in _ADJ_GOVERNMENT:
        add('C2', es, ru, f)
    for level, es, ru in _VOCAB:
        add(level, es, ru, 'тематическая лексика с примерами')
    for level, es, ru, f in _EXTRA_SYNTAX:
        add(level, es, ru, f)
    return out


SYLLABUS = _build()
