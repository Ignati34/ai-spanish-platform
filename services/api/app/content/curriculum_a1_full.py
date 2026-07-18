# -*- coding: utf-8 -*-
"""Upgraded A1 lessons (full theory ~1 page + 3 exercise blocks of 10+ items with translations).

Original wording and examples; grammar facts follow the standard normative description
(coverage cross-checked against classic reference grammars). Replaces the short versions by n.
"""

A1_FULL = [
    {
        'n': 1, 'level': 'A1', 'title': 'Алфавит и произношение',
        'theory': (
            'В испанском алфавите 27 букв: 26 латинских плюс особая буква ñ. Испанская орфография '
            'почти фонетична: слово читается так, как пишется, по небольшому набору правил.\n\n'
            '1. Гласные. Их пять: a, e, i, o, u. Они произносятся чётко и кратко, без редукции: '
            'безударное o никогда не превращается в «а» (как в русском «молоко»). Гласные делятся на '
            'сильные (a, e, o) и слабые (i, u). Сочетание сильного и слабого гласного образует дифтонг '
            'и читается как один слог: bien (хорошо), aire (воздух), ciudad (город).\n\n'
            '2. Согласные и особые сочетания:\n'
            '• ñ — мягкое «нь»: niño (ребёнок), España (Испания), mañana (утро/завтра).\n'
            '• ll — в современном языке звучит как «й»: llave (ключ), calle (улица), lluvia (дождь).\n'
            '• ch — «ч»: chico (мальчик), coche (машина), noche (ночь).\n'
            '• h — никогда не читается: hola (привет) → «ола», hotel → «отель», ahora (сейчас) → «аора».\n'
            '• j — твёрдое гортанное «х»: jardín (сад), joven (молодой), trabajo (работа).\n'
            '• g перед e, i — тоже «х»: gente (люди), página (страница); перед a, o, u — «г»: gato (кот). '
            'Чтобы получить «ге/ги», пишут немую u: guerra (война), guitarra (гитара).\n'
            '• c перед e, i — межзубное «с» в Испании (в Латинской Америке обычное «с»): cine (кино), '
            'cielo (небо); в остальных позициях — «к»: casa (дом), cosa (вещь). Сочетание qu перед e, i '
            'даёт «к»: queso (сыр), aquí (здесь).\n'
            '• z — тот же звук, что c перед e/i: zapato (ботинок), plaza (площадь).\n'
            '• v произносится как b: vino (вино) звучит «бино»; разницы между b и v в речи нет.\n'
            '• r в начале слова и rr — раскатистое: rosa (роза), perro (собака); одиночная r внутри '
            'слова — одноударная: pero (но).\n\n'
            '3. Ударение. Два простых правила:\n'
            '• слово оканчивается на гласную, -n или -s → ударение на ПРЕДПОСЛЕДНЕМ слоге: '
            'CA-sa, HA-blan, LU-nes;\n'
            '• слово оканчивается на любую другую согласную → ударение на ПОСЛЕДНЕМ слоге: '
            'ha-BLAR, ciu-DAD, es-pa-ÑOL.\n'
            'Все исключения обозначаются графическим ударением (tilde): café (кофе), árbol (дерево), '
            'canción (песня), teléfono (телефон). Тильда также различает одинаково пишущиеся слова: '
            'tú (ты) — tu (твой), sí (да) — si (если), qué (что?) — que (что/который).'
        ),
        'exercises': [
            # --- Упражнение 1 ---
            {'section': 'Упражнение 1. Выберите правильное чтение буквы или сочетания', 'exercise_type': 'multiple_choice',
             'prompt': 'ñ в слове «mañana»', 'options': ['н', 'нь', 'й'], 'correct_answer': 'нь',
             'translation': 'mañana — утро; завтра', 'explanation': 'ñ всегда читается «нь».'},
            {'section': 'Упражнение 1. Выберите правильное чтение буквы или сочетания', 'exercise_type': 'multiple_choice',
             'prompt': 'll в слове «calle»', 'options': ['ль', 'й', 'лл'], 'correct_answer': 'й',
             'translation': 'calle — улица', 'explanation': 'Современное ll = «й».'},
            {'section': 'Упражнение 1. Выберите правильное чтение буквы или сочетания', 'exercise_type': 'multiple_choice',
             'prompt': 'h в слове «hotel»', 'options': ['х', 'г', 'не читается'], 'correct_answer': 'не читается',
             'translation': 'hotel — отель', 'explanation': 'h всегда немая.'},
            {'section': 'Упражнение 1. Выберите правильное чтение буквы или сочетания', 'exercise_type': 'multiple_choice',
             'prompt': 'j в слове «trabajo»', 'options': ['ж', 'х', 'дж'], 'correct_answer': 'х',
             'translation': 'trabajo — работа', 'explanation': 'j — твёрдое «х».'},
            {'section': 'Упражнение 1. Выберите правильное чтение буквы или сочетания', 'exercise_type': 'multiple_choice',
             'prompt': 'g в слове «gente»', 'options': ['г', 'х', 'ж'], 'correct_answer': 'х',
             'translation': 'gente — люди', 'explanation': 'g перед e/i = «х».'},
            {'section': 'Упражнение 1. Выберите правильное чтение буквы или сочетания', 'exercise_type': 'multiple_choice',
             'prompt': 'g в слове «gato»', 'options': ['г', 'х', 'к'], 'correct_answer': 'г',
             'translation': 'gato — кот', 'explanation': 'g перед a/o/u = «г».'},
            {'section': 'Упражнение 1. Выберите правильное чтение буквы или сочетания', 'exercise_type': 'multiple_choice',
             'prompt': 'c в слове «cine»', 'options': ['к', 'с/θ', 'ч'], 'correct_answer': 'с/θ',
             'translation': 'cine — кино', 'explanation': 'c перед e/i = «с» (в Испании «θ»).'},
            {'section': 'Упражнение 1. Выберите правильное чтение буквы или сочетания', 'exercise_type': 'multiple_choice',
             'prompt': 'qu в слове «queso»', 'options': ['ку', 'к', 'кв'], 'correct_answer': 'к',
             'translation': 'queso — сыр', 'explanation': 'qu перед e/i = «к», u немая.'},
            {'section': 'Упражнение 1. Выберите правильное чтение буквы или сочетания', 'exercise_type': 'multiple_choice',
             'prompt': 'v в слове «vino»', 'options': ['в', 'б', 'ф'], 'correct_answer': 'б',
             'translation': 'vino — вино', 'explanation': 'v = b по звучанию.'},
            {'section': 'Упражнение 1. Выберите правильное чтение буквы или сочетания', 'exercise_type': 'multiple_choice',
             'prompt': 'ch в слове «noche»', 'options': ['ш', 'ч', 'к'], 'correct_answer': 'ч',
             'translation': 'noche — ночь', 'explanation': 'ch = «ч».'},
            # --- Упражнение 2 ---
            {'section': 'Упражнение 2. На какой слог падает ударение?', 'exercise_type': 'multiple_choice',
             'prompt': 'casa', 'options': ['CA-sa', 'ca-SA'], 'correct_answer': 'CA-sa',
             'translation': 'casa — дом', 'explanation': 'На гласную → предпоследний слог.'},
            {'section': 'Упражнение 2. На какой слог падает ударение?', 'exercise_type': 'multiple_choice',
             'prompt': 'hablar', 'options': ['HA-blar', 'ha-BLAR'], 'correct_answer': 'ha-BLAR',
             'translation': 'hablar — говорить', 'explanation': 'На согласную (не n/s) → последний.'},
            {'section': 'Упражнение 2. На какой слог падает ударение?', 'exercise_type': 'multiple_choice',
             'prompt': 'lunes', 'options': ['LU-nes', 'lu-NES'], 'correct_answer': 'LU-nes',
             'translation': 'lunes — понедельник', 'explanation': 'На -s → предпоследний.'},
            {'section': 'Упражнение 2. На какой слог падает ударение?', 'exercise_type': 'multiple_choice',
             'prompt': 'ciudad', 'options': ['CIU-dad', 'ciu-DAD'], 'correct_answer': 'ciu-DAD',
             'translation': 'ciudad — город', 'explanation': 'На -d → последний.'},
            {'section': 'Упражнение 2. На какой слог падает ударение?', 'exercise_type': 'multiple_choice',
             'prompt': 'hablan', 'options': ['HA-blan', 'ha-BLAN'], 'correct_answer': 'HA-blan',
             'translation': 'hablan — (они) говорят', 'explanation': 'На -n → предпоследний.'},
            {'section': 'Упражнение 2. На какой слог падает ударение?', 'exercise_type': 'multiple_choice',
             'prompt': 'español', 'options': ['es-PA-ñol', 'es-pa-ÑOL'], 'correct_answer': 'es-pa-ÑOL',
             'translation': 'español — испанский', 'explanation': 'На -l → последний.'},
            {'section': 'Упражнение 2. На какой слог падает ударение?', 'exercise_type': 'multiple_choice',
             'prompt': 'café', 'options': ['CA-fe', 'ca-FÉ'], 'correct_answer': 'ca-FÉ',
             'translation': 'café — кофе', 'explanation': 'Тильда показывает исключение.'},
            {'section': 'Упражнение 2. На какой слог падает ударение?', 'exercise_type': 'multiple_choice',
             'prompt': 'árbol', 'options': ['ÁR-bol', 'ar-BOL'], 'correct_answer': 'ÁR-bol',
             'translation': 'árbol — дерево', 'explanation': 'Тильда: ударение на á.'},
            {'section': 'Упражнение 2. На какой слог падает ударение?', 'exercise_type': 'multiple_choice',
             'prompt': 'canción', 'options': ['CAN-ción', 'can-CIÓN'], 'correct_answer': 'can-CIÓN',
             'translation': 'canción — песня', 'explanation': 'Тильда на ó.'},
            {'section': 'Упражнение 2. На какой слог падает ударение?', 'exercise_type': 'multiple_choice',
             'prompt': 'teléfono', 'options': ['te-LÉ-fo-no', 'te-le-FO-no'], 'correct_answer': 'te-LÉ-fo-no',
             'translation': 'teléfono — телефон', 'explanation': 'Тильда на é.'},
            # --- Упражнение 3 ---
            {'section': 'Упражнение 3. Выберите слово с правильным написанием', 'exercise_type': 'multiple_choice',
             'prompt': '«ты» (местоимение)', 'options': ['tu', 'tú'], 'correct_answer': 'tú',
             'translation': 'tú — ты; tu — твой', 'explanation': 'tú (ты) — с тильдой.'},
            {'section': 'Упражнение 3. Выберите слово с правильным написанием', 'exercise_type': 'multiple_choice',
             'prompt': '«да»', 'options': ['si', 'sí'], 'correct_answer': 'sí',
             'translation': 'sí — да; si — если', 'explanation': 'sí (да) — с тильдой.'},
            {'section': 'Упражнение 3. Выберите слово с правильным написанием', 'exercise_type': 'multiple_choice',
             'prompt': '«что?» (вопрос)', 'options': ['que', 'qué'], 'correct_answer': 'qué',
             'translation': 'qué — что?; que — что/который', 'explanation': 'Вопросительное — с тильдой.'},
            {'section': 'Упражнение 3. Выберите слово с правильным написанием', 'exercise_type': 'multiple_choice',
             'prompt': '«война»', 'options': ['gerra', 'guerra'], 'correct_answer': 'guerra',
             'translation': 'guerra — война', 'explanation': 'Немая u сохраняет звук «г».'},
            {'section': 'Упражнение 3. Выберите слово с правильным написанием', 'exercise_type': 'multiple_choice',
             'prompt': '«здесь»', 'options': ['aquí', 'akí'], 'correct_answer': 'aquí',
             'translation': 'aquí — здесь', 'explanation': 'Звук «ки» пишется qui.'},
            {'section': 'Упражнение 3. Выберите слово с правильным написанием', 'exercise_type': 'multiple_choice',
             'prompt': '«привет»', 'options': ['ola', 'hola'], 'correct_answer': 'hola',
             'translation': 'hola — привет', 'explanation': 'Немая h пишется, но не читается.'},
            {'section': 'Упражнение 3. Выберите слово с правильным написанием', 'exercise_type': 'multiple_choice',
             'prompt': '«гитара»', 'options': ['guitarra', 'gitarra'], 'correct_answer': 'guitarra',
             'translation': 'guitarra — гитара', 'explanation': 'gui = «ги» (u немая).'},
            {'section': 'Упражнение 3. Выберите слово с правильным написанием', 'exercise_type': 'multiple_choice',
             'prompt': '«площадь»', 'options': ['plaza', 'plasa'], 'correct_answer': 'plaza',
             'translation': 'plaza — площадь', 'explanation': 'Звук «с/θ» перед a — буква z.'},
            {'section': 'Упражнение 3. Выберите слово с правильным написанием', 'exercise_type': 'multiple_choice',
             'prompt': '«собака»', 'options': ['pero', 'perro'], 'correct_answer': 'perro',
             'translation': 'perro — собака; pero — но', 'explanation': 'rr — раскатистый звук, меняет смысл.'},
            {'section': 'Упражнение 3. Выберите слово с правильным написанием', 'exercise_type': 'multiple_choice',
             'prompt': '«песня»', 'options': ['cancion', 'canción'], 'correct_answer': 'canción',
             'translation': 'canción — песня', 'explanation': 'Ударное -ción всегда с тильдой.'},
        ],
    },
    {
        'n': 2, 'level': 'A1', 'title': 'Род существительных и неопределённый артикль',
        'theory': (
            'В испанском языке существительные имеют только два рода — мужской и женский; среднего '
            'рода у существительных нет. Род — постоянный признак слова, и от него зависит форма '
            'артикля, прилагательного и местоимений, поэтому существительные надо запоминать вместе '
            'с артиклем.\n\n'
            '1. Основные признаки рода по окончанию:\n'
            '• -o → как правило, мужской род: el libro (книга), el vaso (стакан), el año (год);\n'
            '• -a → как правило, женский род: la mesa (стол), la casa (дом), la ventana (окно);\n'
            '• -ción, -sión, -dad, -tad, -umbre → всегда женский: la canción (песня), la ciudad (город), '
            'la libertad (свобода), la costumbre (обычай);\n'
            '• -or, -aje → обычно мужской: el amor (любовь), el viaje (путешествие).\n\n'
            '2. Важные исключения, которые надо выучить: el día (день), el mapa (карта), el sofá (диван) — '
            'мужской род при окончании -a; la mano (рука), la foto (фото), la moto (мотоцикл) — женский '
            'при окончании -o. Слова греческого происхождения на -ma — мужского рода: el problema '
            '(проблема), el idioma (язык), el tema (тема), el sistema (система).\n\n'
            '3. Одушевлённые существительные часто образуют пары: el chico — la chica (мальчик — девочка), '
            'el profesor — la profesora, el señor — la señora. У некоторых форма одна, меняется только '
            'артикль: el estudiante — la estudiante, el periodista — la periodista.\n\n'
            '4. Неопределённый артикль указывает на предмет как один из многих, впервые упоминаемый '
            'или неконкретный: un (м. р.) и una (ж. р.): un libro (какая-то/одна книга), una mesa. '
            'Во множественном числе unos/unas означают «несколько, какие-то»: unos amigos (несколько '
            'друзей), unas casas.\n\n'
            '5. Указательные слова esto (это) и eso (то) употребляются, когда предмет ещё не назван, '
            'и не меняются по родам: ¿Qué es esto? — Esto es un lápiz. (Что это? — Это карандаш.) '
            'Связка es («есть, является») — форма глагола ser для 3 лица: Esto es una ventana. '
            'Во множественном числе — son: Esos son unos libros.'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Определите род существительного', 'exercise_type': 'multiple_choice',
             'prompt': 'libro', 'options': ['мужской', 'женский'], 'correct_answer': 'мужской',
             'translation': 'libro — книга', 'explanation': '-o → м. р.: el libro.'},
            {'section': 'Упражнение 1. Определите род существительного', 'exercise_type': 'multiple_choice',
             'prompt': 'mesa', 'options': ['мужской', 'женский'], 'correct_answer': 'женский',
             'translation': 'mesa — стол', 'explanation': '-a → ж. р.: la mesa.'},
            {'section': 'Упражнение 1. Определите род существительного', 'exercise_type': 'multiple_choice',
             'prompt': 'día', 'options': ['мужской', 'женский'], 'correct_answer': 'мужской',
             'translation': 'día — день', 'explanation': 'Исключение: el día.'},
            {'section': 'Упражнение 1. Определите род существительного', 'exercise_type': 'multiple_choice',
             'prompt': 'mano', 'options': ['мужской', 'женский'], 'correct_answer': 'женский',
             'translation': 'mano — рука', 'explanation': 'Исключение: la mano.'},
            {'section': 'Упражнение 1. Определите род существительного', 'exercise_type': 'multiple_choice',
             'prompt': 'problema', 'options': ['мужской', 'женский'], 'correct_answer': 'мужской',
             'translation': 'problema — проблема', 'explanation': 'Греческое -ma → el problema.'},
            {'section': 'Упражнение 1. Определите род существительного', 'exercise_type': 'multiple_choice',
             'prompt': 'canción', 'options': ['мужской', 'женский'], 'correct_answer': 'женский',
             'translation': 'canción — песня', 'explanation': '-ción → ж. р.'},
            {'section': 'Упражнение 1. Определите род существительного', 'exercise_type': 'multiple_choice',
             'prompt': 'ciudad', 'options': ['мужской', 'женский'], 'correct_answer': 'женский',
             'translation': 'ciudad — город', 'explanation': '-dad → ж. р.'},
            {'section': 'Упражнение 1. Определите род существительного', 'exercise_type': 'multiple_choice',
             'prompt': 'idioma', 'options': ['мужской', 'женский'], 'correct_answer': 'мужской',
             'translation': 'idioma — язык', 'explanation': '-ma → el idioma.'},
            {'section': 'Упражнение 1. Определите род существительного', 'exercise_type': 'multiple_choice',
             'prompt': 'foto', 'options': ['мужской', 'женский'], 'correct_answer': 'женский',
             'translation': 'foto — фотография', 'explanation': 'Исключение: la foto.'},
            {'section': 'Упражнение 1. Определите род существительного', 'exercise_type': 'multiple_choice',
             'prompt': 'viaje', 'options': ['мужской', 'женский'], 'correct_answer': 'мужской',
             'translation': 'viaje — путешествие', 'explanation': '-aje → м. р.: el viaje.'},
            # --- 2 ---
            {'section': 'Упражнение 2. Вставьте un или una', 'exercise_type': 'fill_blank',
             'prompt': 'Esto es ___ libro.', 'options': ['un', 'una'], 'correct_answer': 'un',
             'translation': 'Это книга.', 'explanation': 'libro — м. р.'},
            {'section': 'Упражнение 2. Вставьте un или una', 'exercise_type': 'fill_blank',
             'prompt': 'Esto es ___ mesa.', 'options': ['un', 'una'], 'correct_answer': 'una',
             'translation': 'Это стол.', 'explanation': 'mesa — ж. р.'},
            {'section': 'Упражнение 2. Вставьте un или una', 'exercise_type': 'fill_blank',
             'prompt': 'Es ___ problema difícil.', 'options': ['un', 'una'], 'correct_answer': 'un',
             'translation': 'Это трудная проблема.', 'explanation': 'el problema — м. р.'},
            {'section': 'Упражнение 2. Вставьте un или una', 'exercise_type': 'fill_blank',
             'prompt': 'Es ___ ciudad bonita.', 'options': ['un', 'una'], 'correct_answer': 'una',
             'translation': 'Это красивый город.', 'explanation': 'ciudad — ж. р.'},
            {'section': 'Упражнение 2. Вставьте un или una', 'exercise_type': 'fill_blank',
             'prompt': 'Tengo ___ mapa de España.', 'options': ['un', 'una'], 'correct_answer': 'un',
             'translation': 'У меня есть карта Испании.', 'explanation': 'Исключение: el mapa.'},
            {'section': 'Упражнение 2. Вставьте un или una', 'exercise_type': 'fill_blank',
             'prompt': 'Es ___ día bonito.', 'options': ['un', 'una'], 'correct_answer': 'un',
             'translation': 'Прекрасный день.', 'explanation': 'el día — м. р.'},
            {'section': 'Упражнение 2. Вставьте un или una', 'exercise_type': 'fill_blank',
             'prompt': 'Veo ___ foto en la mesa.', 'options': ['un', 'una'], 'correct_answer': 'una',
             'translation': 'Я вижу фотографию на столе.', 'explanation': 'la foto — ж. р.'},
            {'section': 'Упражнение 2. Вставьте un или una', 'exercise_type': 'fill_blank',
             'prompt': 'Es ___ canción popular.', 'options': ['un', 'una'], 'correct_answer': 'una',
             'translation': 'Это популярная песня.', 'explanation': '-ción → ж. р.'},
            {'section': 'Упражнение 2. Вставьте un или una', 'exercise_type': 'fill_blank',
             'prompt': 'Compro ___ sofá nuevo.', 'options': ['un', 'una'], 'correct_answer': 'un',
             'translation': 'Я покупаю новый диван.', 'explanation': 'el sofá — м. р.'},
            {'section': 'Упражнение 2. Вставьте un или una', 'exercise_type': 'fill_blank',
             'prompt': 'Es ___ idioma bonito.', 'options': ['un', 'una'], 'correct_answer': 'un',
             'translation': 'Это красивый язык.', 'explanation': 'el idioma — м. р.'},
            # --- 3 ---
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это книга.»',
             'options': ['Esto es un libro.', 'Esto es una libro.', 'Este es libro.'],
             'correct_answer': 'Esto es un libro.', 'explanation': 'esto + es + un (м. р.).'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это стол.»',
             'options': ['Esto es un mesa.', 'Esto es una mesa.', 'Eso son una mesa.'],
             'correct_answer': 'Esto es una mesa.', 'explanation': 'mesa — ж. р. → una.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Что это?»',
             'options': ['¿Qué es esto?', '¿Que es esto?', '¿Qué esto es?'],
             'correct_answer': '¿Qué es esto?', 'explanation': 'Вопросительное qué — с тильдой.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это проблема.»',
             'options': ['Esto es una problema.', 'Esto es un problema.', 'Esto son un problema.'],
             'correct_answer': 'Esto es un problema.', 'explanation': 'el problema — м. р.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «У меня есть карта.»',
             'options': ['Tengo un mapa.', 'Tengo una mapa.', 'Tengo mapa un.'],
             'correct_answer': 'Tengo un mapa.', 'explanation': 'el mapa — м. р.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это рука.»',
             'options': ['Esto es un mano.', 'Esto es una mano.', 'Esto es el mano.'],
             'correct_answer': 'Esto es una mano.', 'explanation': 'la mano — ж. р. (исключение).'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это песня.»',
             'options': ['Esto es un canción.', 'Esto es una canción.', 'Esto es unas canción.'],
             'correct_answer': 'Esto es una canción.', 'explanation': '-ción → ж. р.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «несколько друзей»',
             'options': ['unos amigos', 'unas amigos', 'un amigos'],
             'correct_answer': 'unos amigos', 'explanation': 'unos + м. р. мн. ч.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это день.»',
             'options': ['Esto es una día.', 'Esto es un día.', 'Esto es día.'],
             'correct_answer': 'Esto es un día.', 'explanation': 'el día — м. р. (исключение).'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это фотография.»',
             'options': ['Esto es un foto.', 'Esto es una foto.', 'Esto es unos foto.'],
             'correct_answer': 'Esto es una foto.', 'explanation': 'la foto — ж. р. (исключение).'},
        ],
    },
    {
        'n': 3, 'level': 'A1', 'title': 'Определённый артикль и прилагательное',
        'theory': (
            'Определённый артикль указывает, что предмет известен собеседникам, единственный в своём '
            'роде или уже упоминался. Формы: el (м. р. ед.), la (ж. р. ед.), los (м. р. мн.), '
            'las (ж. р. мн.): el libro — los libros, la casa — las casas.\n\n'
            '1. Особый случай: перед существительными женского рода, начинающимися с УДАРНОГО a- или '
            'ha-, в единственном числе используется el: el agua (вода), el aula (аудитория), '
            'el hambre (голод). Род при этом остаётся женским: el agua fría (холодная вода), '
            'во множественном — las aguas.\n\n'
            '2. Слияния с предлогами (обязательные): a + el = al (Voy al parque — иду в парк), '
            'de + el = del (el libro del profesor — книга преподавателя). С la, los, las слияния нет.\n\n'
            '3. Прилагательное согласуется с существительным в роде и числе:\n'
            '• на -o меняют род: alto/alta (высокий/-ая), rojo/roja (красный/-ая): '
            'el coche rojo, la casa roja;\n'
            '• на -e и на большинство согласных по роду НЕ меняются: grande (большой), verde (зелёный), '
            'azul (синий), fácil (лёгкий): un libro verde, una mesa verde;\n'
            '• прилагательные национальности на согласную образуют женский род добавлением -a: '
            'español → española, francés → francesa.\n\n'
            '4. Место прилагательного. Обычное положение — ПОСЛЕ существительного: описательные '
            'прилагательные, цвета, форма, национальность: la mesa redonda (круглый стол), '
            'un escritor español. Перед существительным ставятся указания количества и порядка, '
            'а также несколько кратких оценочных прилагательных.\n\n'
            '5. Усечение (apócope). Перед существительным мужского рода ЕДИНСТВЕННОГО числа '
            'некоторые прилагательные теряют конечный слог: bueno → buen (un buen amigo — хороший '
            'друг), malo → mal (un mal día — плохой день), grande → gran перед существительным '
            'ЛЮБОГО рода в ед. ч. (un gran hombre — великий человек, una gran ciudad — большой/великий '
            'город). Обратите внимание: grande после существительного значит «большой по размеру» '
            '(una ciudad grande), gran перед ним — «великий, выдающийся».'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Вставьте el, la, los или las', 'exercise_type': 'fill_blank',
             'prompt': '___ libro está aquí.', 'options': ['El', 'La', 'Los'], 'correct_answer': 'El',
             'translation': 'Книга здесь.', 'explanation': 'libro — м. р. ед.'},
            {'section': 'Упражнение 1. Вставьте el, la, los или las', 'exercise_type': 'fill_blank',
             'prompt': '___ casas son blancas.', 'options': ['La', 'Los', 'Las'], 'correct_answer': 'Las',
             'translation': 'Дома белые.', 'explanation': 'casas — ж. р. мн.'},
            {'section': 'Упражнение 1. Вставьте el, la, los или las', 'exercise_type': 'fill_blank',
             'prompt': '___ agua está fría.', 'options': ['La', 'El', 'Las'], 'correct_answer': 'El',
             'translation': 'Вода холодная.', 'explanation': 'Ударное a- → el agua (род женский).'},
            {'section': 'Упражнение 1. Вставьте el, la, los или las', 'exercise_type': 'fill_blank',
             'prompt': '___ problemas son difíciles.', 'options': ['Las', 'Los', 'La'], 'correct_answer': 'Los',
             'translation': 'Проблемы трудные.', 'explanation': 'el problema → los problemas.'},
            {'section': 'Упражнение 1. Вставьте el, la, los или las', 'exercise_type': 'fill_blank',
             'prompt': '___ mano derecha.', 'options': ['El', 'La', 'Lo'], 'correct_answer': 'La',
             'translation': 'Правая рука.', 'explanation': 'la mano — ж. р.'},
            {'section': 'Упражнение 1. Вставьте el, la, los или las', 'exercise_type': 'fill_blank',
             'prompt': 'Voy ___ parque. (a + артикль)', 'options': ['al', 'a la', 'a el'], 'correct_answer': 'al',
             'translation': 'Я иду в парк.', 'explanation': 'a + el = al.'},
            {'section': 'Упражнение 1. Вставьте el, la, los или las', 'exercise_type': 'fill_blank',
             'prompt': 'El libro ___ profesor. (de + артикль)', 'options': ['del', 'de la', 'de el'], 'correct_answer': 'del',
             'translation': 'Книга преподавателя.', 'explanation': 'de + el = del.'},
            {'section': 'Упражнение 1. Вставьте el, la, los или las', 'exercise_type': 'fill_blank',
             'prompt': 'Vengo ___ escuela.', 'options': ['del', 'de la', 'al'], 'correct_answer': 'de la',
             'translation': 'Я иду из школы.', 'explanation': 'С la слияния нет: de la.'},
            {'section': 'Упражнение 1. Вставьте el, la, los или las', 'exercise_type': 'fill_blank',
             'prompt': '___ días son largos.', 'options': ['Las', 'Los', 'El'], 'correct_answer': 'Los',
             'translation': 'Дни длинные.', 'explanation': 'el día → los días.'},
            {'section': 'Упражнение 1. Вставьте el, la, los или las', 'exercise_type': 'fill_blank',
             'prompt': '___ aula está abierta.', 'options': ['La', 'El', 'Los'], 'correct_answer': 'El',
             'translation': 'Аудитория открыта.', 'explanation': 'Ударное a- → el aula.'},
            # --- 2 ---
            {'section': 'Упражнение 2. Согласуйте прилагательное', 'exercise_type': 'fill_blank',
             'prompt': 'El coche ___ (rojo).', 'options': ['rojo', 'roja', 'rojos'], 'correct_answer': 'rojo',
             'translation': 'Красная машина.', 'explanation': 'coche — м. р. ед.'},
            {'section': 'Упражнение 2. Согласуйте прилагательное', 'exercise_type': 'fill_blank',
             'prompt': 'La casa ___ (blanco).', 'options': ['blanco', 'blanca', 'blancas'], 'correct_answer': 'blanca',
             'translation': 'Белый дом.', 'explanation': 'casa — ж. р.'},
            {'section': 'Упражнение 2. Согласуйте прилагательное', 'exercise_type': 'fill_blank',
             'prompt': 'Las mesas ___ (verde).', 'options': ['verde', 'verdes', 'verdas'], 'correct_answer': 'verdes',
             'translation': 'Зелёные столы.', 'explanation': '-e: по роду не меняется, по числу — да.'},
            {'section': 'Упражнение 2. Согласуйте прилагательное', 'exercise_type': 'fill_blank',
             'prompt': 'Los libros ___ (interesante).', 'options': ['interesante', 'interesantes', 'interesantos'],
             'correct_answer': 'interesantes', 'translation': 'Интересные книги.', 'explanation': 'Мн. ч.: -s.'},
            {'section': 'Упражнение 2. Согласуйте прилагательное', 'exercise_type': 'fill_blank',
             'prompt': 'Una escritora ___ (español).', 'options': ['español', 'española', 'españolas'],
             'correct_answer': 'española', 'translation': 'Испанская писательница.', 'explanation': 'Национальность: +a.'},
            {'section': 'Упражнение 2. Согласуйте прилагательное', 'exercise_type': 'fill_blank',
             'prompt': 'El cielo ___ (azul).', 'options': ['azul', 'azula', 'azules'], 'correct_answer': 'azul',
             'translation': 'Синее небо.', 'explanation': 'На согласную: род не меняется.'},
            {'section': 'Упражнение 2. Согласуйте прилагательное', 'exercise_type': 'fill_blank',
             'prompt': 'Las ciudades ___ (grande).', 'options': ['grande', 'grandes', 'grandas'], 'correct_answer': 'grandes',
             'translation': 'Большие города.', 'explanation': 'Мн. ч.: grandes.'},
            {'section': 'Упражнение 2. Согласуйте прилагательное', 'exercise_type': 'fill_blank',
             'prompt': 'Un ___ amigo. (bueno, перед сущ.)', 'options': ['bueno', 'buen', 'buena'], 'correct_answer': 'buen',
             'translation': 'Хороший друг.', 'explanation': 'Усечение перед м. р. ед.: buen.'},
            {'section': 'Упражнение 2. Согласуйте прилагательное', 'exercise_type': 'fill_blank',
             'prompt': 'Un ___ día. (malo, перед сущ.)', 'options': ['malo', 'mal', 'mala'], 'correct_answer': 'mal',
             'translation': 'Плохой день.', 'explanation': 'malo → mal перед м. р. ед.'},
            {'section': 'Упражнение 2. Согласуйте прилагательное', 'exercise_type': 'fill_blank',
             'prompt': 'Una ___ ciudad. (grande, «великий»)', 'options': ['grande', 'gran', 'granda'], 'correct_answer': 'gran',
             'translation': 'Великий город.', 'explanation': 'grande → gran перед ед. ч. любого рода.'},
            # --- 3 ---
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «красная машина»',
             'options': ['el rojo coche', 'el coche rojo', 'la coche roja'],
             'correct_answer': 'el coche rojo', 'explanation': 'Цвет — после существительного.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «белый дом»',
             'options': ['la casa blanca', 'la blanca casa', 'el casa blanco'],
             'correct_answer': 'la casa blanca', 'explanation': 'casa — ж. р.; описание — после.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я иду в парк.»',
             'options': ['Voy a el parque.', 'Voy al parque.', 'Voy del parque.'],
             'correct_answer': 'Voy al parque.', 'explanation': 'a + el = al (обязательно).'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «книга преподавателя»',
             'options': ['el libro del profesor', 'el libro de el profesor', 'del profesor el libro'],
             'correct_answer': 'el libro del profesor', 'explanation': 'de + el = del.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «холодная вода»',
             'options': ['la agua fría', 'el agua fría', 'el agua frío'],
             'correct_answer': 'el agua fría', 'explanation': 'el agua, но прилагательное — ж. р.: fría.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «хороший друг»',
             'options': ['un bueno amigo', 'un buen amigo', 'un amigo buen'],
             'correct_answer': 'un buen amigo', 'explanation': 'Усечение: buen перед сущ.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «зелёные столы»',
             'options': ['las mesas verdes', 'las mesas verdas', 'los mesas verdes'],
             'correct_answer': 'las mesas verdes', 'explanation': 'ж. р. мн.: las … verdes.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «большой город (по размеру)»',
             'options': ['una gran ciudad', 'una ciudad grande', 'un ciudad grande'],
             'correct_answer': 'una ciudad grande', 'explanation': 'Размер → grande после сущ.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «великий человек»',
             'options': ['un hombre grande', 'un gran hombre', 'un grande hombre'],
             'correct_answer': 'un gran hombre', 'explanation': '«Великий» → gran перед сущ.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «испанский писатель»',
             'options': ['un español escritor', 'un escritor español', 'un escritor española'],
             'correct_answer': 'un escritor español', 'explanation': 'Национальность — после сущ.'},
        ],
    },
]

_B = [
    {
        'n': 4, 'level': 'A1', 'title': 'Порядок слов. Вопрос и отрицание',
        'theory': (
            'Обычный порядок слов в испанском повествовательном предложении — прямой: подлежащее + '
            'сказуемое + дополнения: María compra pan (Мария покупает хлеб). Однако порядок гибче '
            'русского: определения-прилагательные обычно стоят после существительного, а личные '
            'местоимения-подлежащие часто опускаются, потому что лицо видно по окончанию глагола: '
            'Hablo español (я говорю по-испански).\n\n'
            '1. Вопросительное предложение. На письме вопрос обрамляется двумя знаками: '
            'перевёрнутым ¿ в начале и обычным ? в конце. В общем вопросе (да/нет) чаще всего '
            'делается инверсия — глагол выходит вперёд: ¿Habla usted español? (Вы говорите '
            'по-испански?), ¿Vive María aquí? (Мария живёт здесь?). Возможен и прямой порядок с '
            'вопросительной интонацией: ¿María vive aquí?\n\n'
            '2. Специальный вопрос строится с вопросительными словами, которые всегда пишутся '
            'с тильдой:\n'
            '• ¿qué? — что? какой?: ¿Qué es esto? (Что это?)\n'
            '• ¿quién? / ¿quiénes? — кто?: ¿Quién es? (Кто это?)\n'
            '• ¿dónde? — где?, ¿adónde? — куда?: ¿Dónde vives? (Где ты живёшь?)\n'
            '• ¿cómo? — как?: ¿Cómo estás? (Как дела?)\n'
            '• ¿cuándo? — когда?, ¿cuánto? — сколько?, ¿por qué? — почему?\n'
            'После вопросительного слова глагол идёт перед подлежащим: ¿Dónde vive María?\n\n'
            '3. Отрицание. Частица no ставится непосредственно ПЕРЕД глаголом: No hablo francés '
            '(я не говорю по-французски). María no vive aquí. В ответе no повторяется: '
            '¿Hablas inglés? — No, no hablo inglés.\n\n'
            '4. Двойное отрицание — норма испанского языка. Отрицательные слова nada (ничего), '
            'nadie (никто), nunca (никогда), tampoco (тоже не) после глагола требуют no перед ним: '
            'No veo nada (я ничего не вижу), No viene nadie (никто не приходит), No fumo nunca. '
            'Если отрицательное слово стоит ПЕРЕД глаголом, no не нужно: Nadie viene. Nunca fumo.'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Выберите вопросительное слово', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ vives? — En Madrid.', 'options': ['Qué', 'Dónde', 'Quién'], 'correct_answer': 'Dónde',
             'translation': 'Где ты живёшь? — В Мадриде.', 'explanation': 'Место → dónde.'},
            {'section': 'Упражнение 1. Выберите вопросительное слово', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ es esto? — Es un libro.', 'options': ['Quién', 'Qué', 'Cómo'], 'correct_answer': 'Qué',
             'translation': 'Что это? — Это книга.', 'explanation': 'О предмете → qué.'},
            {'section': 'Упражнение 1. Выберите вопросительное слово', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ es? — Es mi hermano.', 'options': ['Qué', 'Dónde', 'Quién'], 'correct_answer': 'Quién',
             'translation': 'Кто это? — Это мой брат.', 'explanation': 'О человеке → quién.'},
            {'section': 'Упражнение 1. Выберите вопросительное слово', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ estás? — Muy bien, gracias.', 'options': ['Cómo', 'Cuándo', 'Dónde'], 'correct_answer': 'Cómo',
             'translation': 'Как ты? — Очень хорошо, спасибо.', 'explanation': 'Состояние → cómo.'},
            {'section': 'Упражнение 1. Выберите вопросительное слово', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ llega el tren? — A las dos.', 'options': ['Dónde', 'Cuándo', 'Quién'], 'correct_answer': 'Cuándo',
             'translation': 'Когда приходит поезд? — В два.', 'explanation': 'Время → cuándo.'},
            {'section': 'Упражнение 1. Выберите вопросительное слово', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ cuesta? — Diez euros.', 'options': ['Cuánto', 'Cómo', 'Qué'], 'correct_answer': 'Cuánto',
             'translation': 'Сколько стоит? — Десять евро.', 'explanation': 'Количество → cuánto.'},
            {'section': 'Упражнение 1. Выберите вопросительное слово', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ no vienes? — Porque trabajo.', 'options': ['Por qué', 'Cuándo', 'Dónde'], 'correct_answer': 'Por qué',
             'translation': 'Почему ты не идёшь? — Потому что работаю.', 'explanation': 'Причина → por qué.'},
            {'section': 'Упражнение 1. Выберите вопросительное слово', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ vas? — Al cine.', 'options': ['Adónde', 'Dónde', 'Quién'], 'correct_answer': 'Adónde',
             'translation': 'Куда ты идёшь? — В кино.', 'explanation': 'Направление → adónde.'},
            {'section': 'Упражнение 1. Выберите вопросительное слово', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ son? — Son mis padres.', 'options': ['Quién', 'Quiénes', 'Qué'], 'correct_answer': 'Quiénes',
             'translation': 'Кто они? — Это мои родители.', 'explanation': 'Мн. ч. → quiénes.'},
            {'section': 'Упражнение 1. Выберите вопросительное слово', 'exercise_type': 'multiple_choice',
             'prompt': 'Правильная запись вопроса:', 'options': ['Dónde vives?', '¿Dónde vives?', '¿Donde vives?'],
             'correct_answer': '¿Dónde vives?', 'translation': 'Где ты живёшь?', 'explanation': '¿ … ? и тильда в dónde.'},
            # 2
            {'section': 'Упражнение 2. Сделайте предложение отрицательным', 'exercise_type': 'fill_blank',
             'prompt': 'María ___ vive aquí.', 'options': ['no', 'nada', 'nadie'], 'correct_answer': 'no',
             'translation': 'Мария здесь не живёт.', 'explanation': 'no перед глаголом.'},
            {'section': 'Упражнение 2. Сделайте предложение отрицательным', 'exercise_type': 'fill_blank',
             'prompt': 'No veo ___.', 'options': ['nada', 'algo', 'todo'], 'correct_answer': 'nada',
             'translation': 'Я ничего не вижу.', 'explanation': 'no … nada — двойное отрицание.'},
            {'section': 'Упражнение 2. Сделайте предложение отрицательным', 'exercise_type': 'fill_blank',
             'prompt': 'No viene ___.', 'options': ['alguien', 'nadie', 'nada'], 'correct_answer': 'nadie',
             'translation': 'Никто не приходит.', 'explanation': 'no … nadie.'},
            {'section': 'Упражнение 2. Сделайте предложение отрицательным', 'exercise_type': 'fill_blank',
             'prompt': 'No fumo ___.', 'options': ['siempre', 'nunca', 'ahora'], 'correct_answer': 'nunca',
             'translation': 'Я никогда не курю.', 'explanation': 'no … nunca.'},
            {'section': 'Упражнение 2. Сделайте предложение отрицательным', 'exercise_type': 'fill_blank',
             'prompt': '___ viene. (никто, без no)', 'options': ['Nadie', 'No nadie', 'Alguien'], 'correct_answer': 'Nadie',
             'translation': 'Никто не приходит.', 'explanation': 'Отрицательное слово перед глаголом — без no.'},
            {'section': 'Упражнение 2. Сделайте предложение отрицательным', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ hablo francés. (тоже не)', 'options': ['también', 'tampoco', 'nunca'], 'correct_answer': 'tampoco',
             'translation': 'Я тоже не говорю по-французски.', 'explanation': '«Тоже не» → tampoco.'},
            {'section': 'Упражнение 2. Сделайте предложение отрицательным', 'exercise_type': 'fill_blank',
             'prompt': '¿Hablas inglés? — No, ___ hablo inglés.', 'options': ['no', 'nada', 'ni'], 'correct_answer': 'no',
             'translation': 'Ты говоришь по-английски? — Нет, не говорю.', 'explanation': 'no повторяется перед глаголом.'},
            {'section': 'Упражнение 2. Сделайте предложение отрицательным', 'exercise_type': 'fill_blank',
             'prompt': '___ fumo. (никогда, без no)', 'options': ['Nunca', 'No nunca', 'Siempre'], 'correct_answer': 'Nunca',
             'translation': 'Я никогда не курю.', 'explanation': 'nunca перед глаголом — без no.'},
            {'section': 'Упражнение 2. Сделайте предложение отрицательным', 'exercise_type': 'fill_blank',
             'prompt': 'No como ___ por la noche.', 'options': ['nada', 'algo', 'nadie'], 'correct_answer': 'nada',
             'translation': 'Я ничего не ем ночью.', 'explanation': 'no … nada.'},
            {'section': 'Упражнение 2. Сделайте предложение отрицательным', 'exercise_type': 'fill_blank',
             'prompt': 'Ella no estudia, y él ___.', 'options': ['también', 'tampoco', 'nada'], 'correct_answer': 'tampoco',
             'translation': 'Она не учится, и он тоже (не учится).', 'explanation': 'После отрицания «тоже» → tampoco.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Где ты живёшь?»',
             'options': ['¿Dónde vives?', '¿Dónde tú vives?', 'Dónde vives.'],
             'correct_answer': '¿Dónde vives?', 'explanation': 'Вопросительное слово + глагол; ¿ … ?'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я не говорю по-французски.»',
             'options': ['No hablo francés.', 'Hablo no francés.', 'No yo hablo francés.'],
             'correct_answer': 'No hablo francés.', 'explanation': 'no перед глаголом.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я ничего не вижу.»',
             'options': ['No veo nada.', 'Veo nada.', 'No veo algo.'],
             'correct_answer': 'No veo nada.', 'explanation': 'Двойное отрицание обязательно.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Кто это? — Это моя сестра.»',
             'options': ['¿Quién es? — Es mi hermana.', '¿Qué es? — Es mi hermana.', '¿Quién está? — Está mi hermana.'],
             'correct_answer': '¿Quién es? — Es mi hermana.', 'explanation': 'О человеке → quién + ser.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Никто не приходит.»',
             'options': ['Nadie viene.', 'No nadie viene.', 'Alguien no viene.'],
             'correct_answer': 'Nadie viene.', 'explanation': 'nadie перед глаголом — без no.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Почему ты не работаешь?»',
             'options': ['¿Por qué no trabajas?', '¿Porque no trabajas?', '¿Por qué trabajas no?'],
             'correct_answer': '¿Por qué no trabajas?', 'explanation': 'por qué (вопрос) + no перед глаголом.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мария покупает хлеб.»',
             'options': ['María compra pan.', 'Compra María pan.', 'María pan compra.'],
             'correct_answer': 'María compra pan.', 'explanation': 'Прямой порядок: S + V + O.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я никогда не курю.»',
             'options': ['Nunca fumo.', 'No fumo siempre.', 'Nunca no fumo.'],
             'correct_answer': 'Nunca fumo.', 'explanation': 'nunca перед глаголом — без no.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Как тебя зовут?» (досл. «как ты называешься»)',
             'options': ['¿Cómo te llamas?', '¿Como te llamas?', '¿Cómo llamas te?'],
             'correct_answer': '¿Cómo te llamas?', 'explanation': 'cómo с тильдой; te перед глаголом.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я тоже не понимаю.»',
             'options': ['Yo tampoco entiendo.', 'Yo también no entiendo.', 'Tampoco yo no entiendo.'],
             'correct_answer': 'Yo tampoco entiendo.', 'explanation': '«Тоже не» → tampoco (без no перед глаголом).'},
        ],
    },
    {
        'n': 5, 'level': 'A1', 'title': 'Ser и estar. Предлоги места',
        'theory': (
            'В испанском два глагола «быть», и они не взаимозаменяемы.\n\n'
            '1. SER — постоянная сущность. Формы настоящего: soy, eres, es, somos, sois, son.\n'
            'Употребляется для:\n'
            '• тождества и определения: Esto es un libro. Soy Iván.\n'
            '• профессии и рода занятий: Soy médico (я врач). Ella es estudiante.\n'
            '• происхождения и национальности: Soy de Rusia. Es español.\n'
            '• постоянных качеств: María es alta (Мария высокая). El coche es rojo.\n'
            '• времени и дат: Es la una. Son las tres. Hoy es lunes.\n'
            '• материала и принадлежности: La mesa es de madera (стол из дерева). El libro es de Ana.\n\n'
            '2. ESTAR — состояние и местоположение. Формы: estoy, estás, está, estamos, estáis, están '
            '(обратите внимание на ударения).\n'
            'Употребляется для:\n'
            '• местонахождения: Estoy en casa (я дома). Madrid está en España. El libro está en la mesa.\n'
            '• временных состояний и самочувствия: Estoy cansado (я устал). La sopa está caliente '
            '(суп горячий — сейчас). ¿Cómo estás? — Estoy bien.\n\n'
            'Сравните пары: Es alegre (он весёлый по характеру) — Está alegre (он сейчас весел); '
            'La manzana es verde (яблоко зелёного цвета) — La manzana está verde (яблоко неспелое).\n\n'
            '3. Предлоги и наречия места (обычно с estar):\n'
            '• en — в, на: en casa, en la mesa;\n'
            '• sobre / encima de — на, поверх: sobre la mesa;\n'
            '• bajo / debajo de — под: debajo de la cama (под кроватью);\n'
            '• delante de — перед; detrás de — за, позади;\n'
            '• entre — между: entre la ventana y la puerta;\n'
            '• al lado de — рядом с; cerca de — близко от; lejos de — далеко от.\n'
            'Пример: El banco está al lado de la farmacia (банк рядом с аптекой).'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Ser или estar?', 'exercise_type': 'multiple_choice',
             'prompt': 'Yo ___ profesor.', 'options': ['soy', 'estoy'], 'correct_answer': 'soy',
             'translation': 'Я преподаватель.', 'explanation': 'Профессия → ser.'},
            {'section': 'Упражнение 1. Ser или estar?', 'exercise_type': 'multiple_choice',
             'prompt': 'Yo ___ en casa.', 'options': ['soy', 'estoy'], 'correct_answer': 'estoy',
             'translation': 'Я дома.', 'explanation': 'Местоположение → estar.'},
            {'section': 'Упражнение 1. Ser или estar?', 'exercise_type': 'multiple_choice',
             'prompt': 'María ___ alta.', 'options': ['es', 'está'], 'correct_answer': 'es',
             'translation': 'Мария высокая.', 'explanation': 'Постоянное качество → ser.'},
            {'section': 'Упражнение 1. Ser или estar?', 'exercise_type': 'multiple_choice',
             'prompt': 'La sopa ___ caliente.', 'options': ['es', 'está'], 'correct_answer': 'está',
             'translation': 'Суп горячий (сейчас).', 'explanation': 'Временное состояние → estar.'},
            {'section': 'Упражнение 1. Ser или estar?', 'exercise_type': 'multiple_choice',
             'prompt': 'Madrid ___ en España.', 'options': ['es', 'está'], 'correct_answer': 'está',
             'translation': 'Мадрид находится в Испании.', 'explanation': 'Местоположение → estar.'},
            {'section': 'Упражнение 1. Ser или estar?', 'exercise_type': 'multiple_choice',
             'prompt': 'Hoy ___ lunes.', 'options': ['es', 'está'], 'correct_answer': 'es',
             'translation': 'Сегодня понедельник.', 'explanation': 'Дата/день → ser.'},
            {'section': 'Упражнение 1. Ser или estar?', 'exercise_type': 'multiple_choice',
             'prompt': 'Nosotros ___ cansados.', 'options': ['somos', 'estamos'], 'correct_answer': 'estamos',
             'translation': 'Мы устали.', 'explanation': 'Состояние → estar.'},
            {'section': 'Упражнение 1. Ser или estar?', 'exercise_type': 'multiple_choice',
             'prompt': 'Ellos ___ de México.', 'options': ['son', 'están'], 'correct_answer': 'son',
             'translation': 'Они из Мексики.', 'explanation': 'Происхождение → ser (de).'},
            {'section': 'Упражнение 1. Ser или estar?', 'exercise_type': 'multiple_choice',
             'prompt': 'La mesa ___ de madera.', 'options': ['es', 'está'], 'correct_answer': 'es',
             'translation': 'Стол из дерева.', 'explanation': 'Материал → ser de.'},
            {'section': 'Упражнение 1. Ser или estar?', 'exercise_type': 'multiple_choice',
             'prompt': '¿Cómo ___ (tú)? — Bien, gracias.', 'options': ['eres', 'estás'], 'correct_answer': 'estás',
             'translation': 'Как ты? — Хорошо, спасибо.', 'explanation': 'Самочувствие → estar.'},
            # 2
            {'section': 'Упражнение 2. Вставьте предлог места', 'exercise_type': 'fill_blank',
             'prompt': 'El libro está ___ la mesa. (на)', 'options': ['sobre', 'bajo', 'entre'], 'correct_answer': 'sobre',
             'translation': 'Книга на столе.', 'explanation': 'sobre = на, поверх.'},
            {'section': 'Упражнение 2. Вставьте предлог места', 'exercise_type': 'fill_blank',
             'prompt': 'El gato está ___ la cama. (под)', 'options': ['sobre', 'debajo de', 'delante de'], 'correct_answer': 'debajo de',
             'translation': 'Кот под кроватью.', 'explanation': 'debajo de = под.'},
            {'section': 'Упражнение 2. Вставьте предлог места', 'exercise_type': 'fill_blank',
             'prompt': 'Vivo ___ Madrid.', 'options': ['en', 'sobre', 'entre'], 'correct_answer': 'en',
             'translation': 'Я живу в Мадриде.', 'explanation': 'en = в.'},
            {'section': 'Упражнение 2. Вставьте предлог места', 'exercise_type': 'fill_blank',
             'prompt': 'El coche está ___ la casa. (перед)', 'options': ['detrás de', 'delante de', 'debajo de'], 'correct_answer': 'delante de',
             'translation': 'Машина перед домом.', 'explanation': 'delante de = перед.'},
            {'section': 'Упражнение 2. Вставьте предлог места', 'exercise_type': 'fill_blank',
             'prompt': 'El jardín está ___ la casa. (за)', 'options': ['delante de', 'detrás de', 'sobre'], 'correct_answer': 'detrás de',
             'translation': 'Сад за домом.', 'explanation': 'detrás de = за.'},
            {'section': 'Упражнение 2. Вставьте предлог места', 'exercise_type': 'fill_blank',
             'prompt': 'La farmacia está ___ el banco y el bar. (между)', 'options': ['entre', 'sobre', 'en'], 'correct_answer': 'entre',
             'translation': 'Аптека между банком и баром.', 'explanation': 'entre = между.'},
            {'section': 'Упражнение 2. Вставьте предлог места', 'exercise_type': 'fill_blank',
             'prompt': 'El banco está ___ la farmacia. (рядом с)', 'options': ['lejos de', 'al lado de', 'debajo de'], 'correct_answer': 'al lado de',
             'translation': 'Банк рядом с аптекой.', 'explanation': 'al lado de = рядом с.'},
            {'section': 'Упражнение 2. Вставьте предлог места', 'exercise_type': 'fill_blank',
             'prompt': 'La escuela está ___ mi casa. (близко от)', 'options': ['cerca de', 'lejos de', 'entre'], 'correct_answer': 'cerca de',
             'translation': 'Школа близко от моего дома.', 'explanation': 'cerca de = близко от.'},
            {'section': 'Упражнение 2. Вставьте предлог места', 'exercise_type': 'fill_blank',
             'prompt': 'El aeropuerto está ___ la ciudad. (далеко от)', 'options': ['cerca de', 'lejos de', 'al lado de'], 'correct_answer': 'lejos de',
             'translation': 'Аэропорт далеко от города.', 'explanation': 'lejos de = далеко от.'},
            {'section': 'Упражнение 2. Вставьте предлог места', 'exercise_type': 'fill_blank',
             'prompt': 'Las llaves están ___ la mesa. (на/в контакте)', 'options': ['en', 'entre', 'bajo'], 'correct_answer': 'en',
             'translation': 'Ключи на столе.', 'explanation': 'en покрывает и «на»: en la mesa.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я врач.»',
             'options': ['Soy médico.', 'Estoy médico.', 'Soy un médico alto.'],
             'correct_answer': 'Soy médico.', 'explanation': 'Профессия → ser, без артикля.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я дома.»',
             'options': ['Soy en casa.', 'Estoy en casa.', 'Estoy casa.'],
             'correct_answer': 'Estoy en casa.', 'explanation': 'Местоположение → estar + en.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Суп горячий (сейчас).»',
             'options': ['La sopa es caliente.', 'La sopa está caliente.', 'La sopa hay caliente.'],
             'correct_answer': 'La sopa está caliente.', 'explanation': 'Временное состояние → estar.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы из России.»',
             'options': ['Somos de Rusia.', 'Estamos de Rusia.', 'Somos en Rusia.'],
             'correct_answer': 'Somos de Rusia.', 'explanation': 'Происхождение → ser de.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Кот под столом.»',
             'options': ['El gato está debajo de la mesa.', 'El gato es debajo de la mesa.', 'El gato está sobre la mesa.'],
             'correct_answer': 'El gato está debajo de la mesa.', 'explanation': 'Местоположение → estar; под → debajo de.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Сегодня понедельник.»',
             'options': ['Hoy es lunes.', 'Hoy está lunes.', 'Hoy es el lunes.'],
             'correct_answer': 'Hoy es lunes.', 'explanation': 'День недели в «сегодня …» → es lunes.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Банк рядом с аптекой.»',
             'options': ['El banco está al lado de la farmacia.', 'El banco es al lado de la farmacia.', 'El banco está lejos de la farmacia.'],
             'correct_answer': 'El banco está al lado de la farmacia.', 'explanation': 'estar + al lado de.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Стол из дерева.»',
             'options': ['La mesa es de madera.', 'La mesa está de madera.', 'La mesa es madera de.'],
             'correct_answer': 'La mesa es de madera.', 'explanation': 'Материал → ser de.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я устал.»',
             'options': ['Soy cansado.', 'Estoy cansado.', 'Estoy cansar.'],
             'correct_answer': 'Estoy cansado.', 'explanation': 'Состояние → estar cansado.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Школа далеко от центра.»',
             'options': ['La escuela está lejos del centro.', 'La escuela es lejos del centro.', 'La escuela está lejos el centro.'],
             'correct_answer': 'La escuela está lejos del centro.', 'explanation': 'estar + lejos de; de + el = del.'},
        ],
    },
    {
        'n': 6, 'level': 'A1', 'title': 'Конструкция hay. Место прилагательного',
        'theory': (
            '1. Конструкция HAY. Особая безличная форма глагола haber означает «есть, имеется, '
            'находится». У неё ОДНА форма для единственного и множественного числа: '
            'Hay un libro en la mesa (на столе есть книга). Hay muchos coches en la calle (на улице '
            'много машин). ¿Qué hay en la caja? (Что в коробке?)\n\n'
            '2. Hay против está/están. Правило выбора связано с определённостью:\n'
            '• hay вводит НОВОЕ, неизвестное — поэтому сочетается с неопределённым артиклем, '
            'числительными, словами mucho/poco/varios или вовсе без артикля: Hay una farmacia cerca. '
            'Hay dos ventanas. Hay pan.\n'
            '• estar говорит о местоположении ИЗВЕСТНОГО, конкретного предмета — с определённым '
            'артиклем, притяжательными, именами: La farmacia está cerca. El pan está en la mesa. '
            'María está en casa.\n'
            'НЕЛЬЗЯ: *Hay la farmacia…, *El libro hay en la mesa.\n\n'
            '3. Вопрос о количестве с hay: ¿Cuántos alumnos hay en la clase? (Сколько учеников '
            'в классе?) — Hay veinte (двадцать).\n\n'
            '4. Место прилагательного (продолжение). Описательные прилагательные, выделяющие предмет '
            'среди других (цвет, форма, размер, национальность), стоят ПОСЛЕ существительного: '
            'una casa blanca, un problema difícil. ПЕРЕД существительным ставятся:\n'
            '• числительные и слова количества: dos libros, muchas casas, pocos amigos;\n'
            '• указательные и притяжательные: este libro, mi casa;\n'
            '• оценочные bueno, malo, gran(de) — часто с усечением: un buen amigo, un mal día, '
            'una gran idea (отличная идея).\n'
            'Некоторые прилагательные меняют смысл от позиции: un viejo amigo (старый = давний друг) — '
            'un amigo viejo (пожилой друг); un gran hombre (великий) — un hombre grande (крупный).'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Hay или está/están?', 'exercise_type': 'multiple_choice',
             'prompt': '___ un libro en la mesa.', 'options': ['Hay', 'Está'], 'correct_answer': 'Hay',
             'translation': 'На столе есть книга.', 'explanation': 'Новое, с un → hay.'},
            {'section': 'Упражнение 1. Hay или está/están?', 'exercise_type': 'multiple_choice',
             'prompt': 'El libro ___ en la mesa.', 'options': ['hay', 'está'], 'correct_answer': 'está',
             'translation': 'Книга (та самая) на столе.', 'explanation': 'Известное el → está.'},
            {'section': 'Упражнение 1. Hay или está/están?', 'exercise_type': 'multiple_choice',
             'prompt': '___ muchos coches en la calle.', 'options': ['Hay', 'Están'], 'correct_answer': 'Hay',
             'translation': 'На улице много машин.', 'explanation': 'mucho → hay (одна форма!).'},
            {'section': 'Упражнение 1. Hay или está/están?', 'exercise_type': 'multiple_choice',
             'prompt': 'María ___ en casa.', 'options': ['hay', 'está'], 'correct_answer': 'está',
             'translation': 'Мария дома.', 'explanation': 'Имя собственное → está.'},
            {'section': 'Упражнение 1. Hay или está/están?', 'exercise_type': 'multiple_choice',
             'prompt': '¿Cuántos alumnos ___ en la clase?', 'options': ['hay', 'están'], 'correct_answer': 'hay',
             'translation': 'Сколько учеников в классе?', 'explanation': 'Количество/наличие → hay.'},
            {'section': 'Упражнение 1. Hay или está/están?', 'exercise_type': 'multiple_choice',
             'prompt': '___ una farmacia cerca.', 'options': ['Hay', 'Está'], 'correct_answer': 'Hay',
             'translation': 'Поблизости есть аптека.', 'explanation': 'una → hay.'},
            {'section': 'Упражнение 1. Hay или está/están?', 'exercise_type': 'multiple_choice',
             'prompt': 'La farmacia ___ cerca.', 'options': ['hay', 'está'], 'correct_answer': 'está',
             'translation': 'Аптека (та) находится близко.', 'explanation': 'la → está.'},
            {'section': 'Упражнение 1. Hay или está/están?', 'exercise_type': 'multiple_choice',
             'prompt': '___ pan en la cocina.', 'options': ['Hay', 'Está'], 'correct_answer': 'Hay',
             'translation': 'На кухне есть хлеб.', 'explanation': 'Без артикля (вещество) → hay.'},
            {'section': 'Упражнение 1. Hay или está/están?', 'exercise_type': 'multiple_choice',
             'prompt': 'Mis llaves ___ en el bolso.', 'options': ['hay', 'están'], 'correct_answer': 'están',
             'translation': 'Мои ключи в сумке.', 'explanation': 'Притяжательное mis → están.'},
            {'section': 'Упражнение 1. Hay или está/están?', 'exercise_type': 'multiple_choice',
             'prompt': '___ dos ventanas en la habitación.', 'options': ['Hay', 'Están'], 'correct_answer': 'Hay',
             'translation': 'В комнате два окна.', 'explanation': 'Числительное → hay.'},
            # 2
            {'section': 'Упражнение 2. Поставьте прилагательное на место', 'exercise_type': 'multiple_choice',
             'prompt': '«белый дом»', 'options': ['una blanca casa', 'una casa blanca'], 'correct_answer': 'una casa blanca',
             'translation': 'casa blanca — белый дом', 'explanation': 'Цвет — после существительного.'},
            {'section': 'Упражнение 2. Поставьте прилагательное на место', 'exercise_type': 'multiple_choice',
             'prompt': '«две книги»', 'options': ['dos libros', 'libros dos'], 'correct_answer': 'dos libros',
             'translation': 'dos libros — две книги', 'explanation': 'Числительное — перед.'},
            {'section': 'Упражнение 2. Поставьте прилагательное на место', 'exercise_type': 'multiple_choice',
             'prompt': '«трудная проблема»', 'options': ['un difícil problema', 'un problema difícil'], 'correct_answer': 'un problema difícil',
             'translation': 'problema difícil — трудная проблема', 'explanation': 'Описание — после.'},
            {'section': 'Упражнение 2. Поставьте прилагательное на место', 'exercise_type': 'multiple_choice',
             'prompt': '«много домов»', 'options': ['casas muchas', 'muchas casas'], 'correct_answer': 'muchas casas',
             'translation': 'muchas casas — много домов', 'explanation': 'Количество — перед.'},
            {'section': 'Упражнение 2. Поставьте прилагательное на место', 'exercise_type': 'multiple_choice',
             'prompt': '«хороший друг» (усечение)', 'options': ['un buen amigo', 'un bueno amigo'], 'correct_answer': 'un buen amigo',
             'translation': 'buen amigo — хороший друг', 'explanation': 'bueno → buen перед м. р. ед.'},
            {'section': 'Упражнение 2. Поставьте прилагательное на место', 'exercise_type': 'multiple_choice',
             'prompt': '«давний друг»', 'options': ['un viejo amigo', 'un amigo viejo'], 'correct_answer': 'un viejo amigo',
             'translation': 'viejo amigo — давний друг', 'explanation': 'viejo перед сущ. = давний.'},
            {'section': 'Упражнение 2. Поставьте прилагательное на место', 'exercise_type': 'multiple_choice',
             'prompt': '«пожилой друг»', 'options': ['un viejo amigo', 'un amigo viejo'], 'correct_answer': 'un amigo viejo',
             'translation': 'amigo viejo — пожилой друг', 'explanation': 'viejo после сущ. = старый по возрасту.'},
            {'section': 'Упражнение 2. Поставьте прилагательное на место', 'exercise_type': 'multiple_choice',
             'prompt': '«отличная идея»', 'options': ['una gran idea', 'una idea gran'], 'correct_answer': 'una gran idea',
             'translation': 'gran idea — отличная идея', 'explanation': 'gran перед сущ. = великая/отличная.'},
            {'section': 'Упражнение 2. Поставьте прилагательное на место', 'exercise_type': 'multiple_choice',
             'prompt': '«мой дом»', 'options': ['mi casa', 'casa mi'], 'correct_answer': 'mi casa',
             'translation': 'mi casa — мой дом', 'explanation': 'Притяжательное — перед.'},
            {'section': 'Упражнение 2. Поставьте прилагательное на место', 'exercise_type': 'multiple_choice',
             'prompt': '«испанский писатель»', 'options': ['un español escritor', 'un escritor español'], 'correct_answer': 'un escritor español',
             'translation': 'escritor español — испанский писатель', 'explanation': 'Национальность — после.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «На столе есть книга.»',
             'options': ['Hay un libro en la mesa.', 'Está un libro en la mesa.', 'Hay el libro en la mesa.'],
             'correct_answer': 'Hay un libro en la mesa.', 'explanation': 'Новое с un → hay.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Книга — на столе.» (та самая)',
             'options': ['Hay el libro en la mesa.', 'El libro está en la mesa.', 'El libro hay en la mesa.'],
             'correct_answer': 'El libro está en la mesa.', 'explanation': 'Известное el → está.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «В комнате два окна.»',
             'options': ['Hay dos ventanas en la habitación.', 'Están dos ventanas en la habitación.', 'Hay dos ventana en la habitación.'],
             'correct_answer': 'Hay dos ventanas en la habitación.', 'explanation': 'Числительное → hay.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Поблизости много магазинов.»',
             'options': ['Hay muchas tiendas cerca.', 'Están muchas tiendas cerca.', 'Hay muchas tienda cerca.'],
             'correct_answer': 'Hay muchas tiendas cerca.', 'explanation': 'mucho + новое → hay.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Сколько студентов в классе?»',
             'options': ['¿Cuántos estudiantes hay en la clase?', '¿Cuántos estudiantes están en la clase?', '¿Cuánto estudiantes hay en la clase?'],
             'correct_answer': '¿Cuántos estudiantes hay en la clase?', 'explanation': 'Количество → cuántos + hay.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Аптека рядом.» (та самая)',
             'options': ['Hay la farmacia cerca.', 'La farmacia está cerca.', 'La farmacia hay cerca.'],
             'correct_answer': 'La farmacia está cerca.', 'explanation': 'С la — только estar.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «хороший день»',
             'options': ['un buen día', 'un bueno día', 'un día buen'],
             'correct_answer': 'un buen día', 'explanation': 'bueno → buen перед м. р. ед.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «На кухне есть хлеб.»',
             'options': ['Hay pan en la cocina.', 'El pan hay en la cocina.', 'Está pan en la cocina.'],
             'correct_answer': 'Hay pan en la cocina.', 'explanation': 'Вещество без артикля → hay.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мои ключи в сумке.»',
             'options': ['Mis llaves están en el bolso.', 'Hay mis llaves en el bolso.', 'Mis llaves hay en el bolso.'],
             'correct_answer': 'Mis llaves están en el bolso.', 'explanation': 'Притяжательное → están.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «великий писатель»',
             'options': ['un gran escritor', 'un escritor gran', 'un grande escritor'],
             'correct_answer': 'un gran escritor', 'explanation': 'grande → gran перед сущ. = великий.'},
        ],
    },
]
A1_FULL = A1_FULL + _B
