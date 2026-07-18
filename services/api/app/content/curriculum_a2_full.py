# -*- coding: utf-8 -*-
"""Upgraded A2 lessons 17–22 (full theory + 3 blocks of 10 items with translations).
Examples reuse the learner's personal vocab bank (aguantar, añorar, que yo sepa, nunca he visto...).
"""

A2_FULL = [
    {
        'n': 17, 'level': 'A2', 'title': 'Прошедшее несовершенное (Imperfecto)',
        'theory': (
            'Pretérito imperfecto — первое прошедшее время курса. Оно отвечает на вопрос '
            '«что делал? каким был?» и описывает:\n'
            '• привычки и повторяющиеся действия в прошлом: Antes jugaba al fútbol todos los '
            'días (раньше я играл в футбол каждый день);\n'
            '• фон, обстановку, состояние: Hacía frío y llovía (было холодно и шёл дождь);\n'
            '• возраст, время, внешность и чувства в прошлом: Tenía diez años (мне было десять). '
            'Eran las tres (было три часа). Añoraba su ciudad (он тосковал по своему городу).\n\n'
            '1. Образование. Окончания присоединяются к основе:\n'
            '• -ar: -aba, -abas, -aba, -ábamos, -abais, -aban\n'
            '  hablar: hablaba, hablabas, hablaba, hablábamos, hablabais, hablaban\n'
            '• -er/-ir (окончания одинаковые): -ía, -ías, -ía, -íamos, -íais, -ían\n'
            '  comer: comía, comías, comía, comíamos, comíais, comían\n'
            '  vivir: vivía, vivías, vivía, vivíamos, vivíais, vivían\n\n'
            'Формы yo и él/ella совпадают (hablaba, comía) — лицо уточняет контекст или '
            'местоимение.\n\n'
            '2. Слова-маркеры imperfecto: antes (раньше), siempre (всегда), todos los días '
            '(каждый день), cada verano (каждое лето), normalmente, de niño / de pequeño '
            '(в детстве), cuando era joven (когда был молодым).\n\n'
            '3. Типичные употребления:\n'
            '• De niño vivía en un pueblo pequeño (в детстве я жил в маленькой деревне);\n'
            '• Mi abuela cocinaba muy bien y siempre añadía algo especial (бабушка отлично '
            'готовила и всегда добавляла что-то особенное);\n'
            '• No aguantaba el calor del verano (я не выносил летнюю жару);\n'
            '• Cada domingo comíamos juntos (каждое воскресенье мы ели вместе).\n\n'
            '4. Отрицание и вопрос строятся как обычно: No trabajaba los sábados. '
            '¿Dónde vivías antes? (где ты жил раньше?)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Поставьте глагол в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Antes yo ___ (vivir) en Valencia.', 'options': ['vivía', 'viví', 'vivaba'], 'correct_answer': 'vivía',
             'translation': 'Раньше я жил в Валенсии.', 'explanation': '-ir → -ía.'},
            {'section': 'Упражнение 1. Поставьте глагол в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'De niño él ___ (jugar) al fútbol.', 'options': ['jugaba', 'jugó', 'juega'], 'correct_answer': 'jugaba',
             'translation': 'В детстве он играл в футбол.', 'explanation': '-ar → -aba.'},
            {'section': 'Упражнение 1. Поставьте глагол в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ (comer) juntos cada domingo.', 'options': ['comíamos', 'comemos', 'comábamos'], 'correct_answer': 'comíamos',
             'translation': 'Каждое воскресенье мы ели вместе.', 'explanation': '-er → -íamos.'},
            {'section': 'Упражнение 1. Поставьте глагол в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Mi abuela ___ (cocinar) muy bien.', 'options': ['cocinaba', 'cocinó', 'cocina'], 'correct_answer': 'cocinaba',
             'translation': 'Моя бабушка очень хорошо готовила.', 'explanation': 'Характеристика в прошлом → imperfecto.'},
            {'section': 'Упражнение 1. Поставьте глагол в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Ella siempre ___ (añadir) algo especial.', 'options': ['añadía', 'añadaba', 'añade'], 'correct_answer': 'añadía',
             'translation': 'Она всегда добавляла что-то особенное.', 'explanation': '-ir → -ía: añadía.'},
            {'section': 'Упражнение 1. Поставьте глагол в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Yo no ___ (aguantar) el calor.', 'options': ['aguantaba', 'aguanté', 'aguanto'], 'correct_answer': 'aguantaba',
             'translation': 'Я не выносил жару.', 'explanation': 'Постоянное состояние → aguantaba.'},
            {'section': 'Упражнение 1. Поставьте глагол в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': '¿Dónde ___ (trabajar, tú) antes?', 'options': ['trabajabas', 'trabajaste', 'trabajas'], 'correct_answer': 'trabajabas',
             'translation': 'Где ты раньше работал?', 'explanation': '2 л.: trabajabas.'},
            {'section': 'Упражнение 1. Поставьте глагол в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ (recibir) muchas cartas.', 'options': ['recibían', 'recibieron', 'recibaban'], 'correct_answer': 'recibían',
             'translation': 'Они получали много писем.', 'explanation': '-ir → -ían.'},
            {'section': 'Упражнение 1. Поставьте глагол в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Vosotros ___ (estudiar) en Madrid, ¿no?', 'options': ['estudiabais', 'estudiasteis', 'estudiáis'], 'correct_answer': 'estudiabais',
             'translation': 'Вы ведь учились в Мадриде?', 'explanation': '2 л. мн.: -abais.'},
            {'section': 'Упражнение 1. Поставьте глагол в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Él ___ (añorar) su ciudad natal.', 'options': ['añoraba', 'añoró', 'añora'], 'correct_answer': 'añoraba',
             'translation': 'Он тосковал по родному городу.', 'explanation': 'Длительное чувство → añoraba.'},
            # 2
            {'section': 'Упражнение 2. Возраст, время и фон в прошлом', 'exercise_type': 'multiple_choice',
             'prompt': 'Cuando era niño, ___ diez años.', 'options': ['tenía', 'tuve', 'tengo'], 'correct_answer': 'tenía',
             'translation': 'Когда я был ребёнком, мне было десять лет.', 'explanation': 'Возраст в прошлом → imperfecto.'},
            {'section': 'Упражнение 2. Возраст, время и фон в прошлом', 'exercise_type': 'multiple_choice',
             'prompt': '___ las tres de la tarde.', 'options': ['Eran', 'Fueron', 'Son'], 'correct_answer': 'Eran',
             'translation': 'Было три часа дня.', 'explanation': 'Время в прошлом → eran.'},
            {'section': 'Упражнение 2. Возраст, время и фон в прошлом', 'exercise_type': 'multiple_choice',
             'prompt': '___ frío y llovía.', 'options': ['Hacía', 'Hizo', 'Hace'], 'correct_answer': 'Hacía',
             'translation': 'Было холодно, и шёл дождь.', 'explanation': 'Фон/погода → hacía.'},
            {'section': 'Упражнение 2. Возраст, время и фон в прошлом', 'exercise_type': 'multiple_choice',
             'prompt': 'Antes ___ mucha gente en este barrio.', 'options': ['había', 'hubo', 'hay'], 'correct_answer': 'había',
             'translation': 'Раньше в этом районе было много людей.', 'explanation': 'hay в imperfecto → había.'},
            {'section': 'Упражнение 2. Возраст, время и фон в прошлом', 'exercise_type': 'multiple_choice',
             'prompt': 'Mi casa ___ pequeña pero bonita.', 'options': ['era', 'fue', 'es'], 'correct_answer': 'era',
             'translation': 'Мой дом был маленький, но красивый.', 'explanation': 'Описание → era (подробнее в след. уроке).'},
            {'section': 'Упражнение 2. Возраст, время и фон в прошлом', 'exercise_type': 'multiple_choice',
             'prompt': 'Какой маркер указывает на imperfecto?', 'options': ['todos los días', 'ayer', 'una vez'], 'correct_answer': 'todos los días',
             'translation': 'todos los días — каждый день', 'explanation': 'Регулярность → imperfecto.'},
            {'section': 'Упражнение 2. Возраст, время и фон в прошлом', 'exercise_type': 'multiple_choice',
             'prompt': 'De pequeño no me ___ las verduras.', 'options': ['gustaban', 'gustaron', 'gustan'], 'correct_answer': 'gustaban',
             'translation': 'В детстве мне не нравились овощи.', 'explanation': 'Привычное отношение → gustaban.'},
            {'section': 'Упражнение 2. Возраст, время и фон в прошлом', 'exercise_type': 'multiple_choice',
             'prompt': 'Cada verano ___ a la playa.', 'options': ['íbamos', 'fuimos', 'vamos'], 'correct_answer': 'íbamos',
             'translation': 'Каждое лето мы ездили на пляж.', 'explanation': 'Регулярность → imperfecto (ir → iba).'},
            {'section': 'Упражнение 2. Возраст, время и фон в прошлом', 'exercise_type': 'multiple_choice',
             'prompt': '«(Я) говорил» в imperfecto =', 'options': ['hablaba', 'hablabas', 'hablábamos'], 'correct_answer': 'hablaba',
             'translation': 'hablaba — я/он говорил', 'explanation': '1 и 3 л. ед. совпадают.'},
            {'section': 'Упражнение 2. Возраст, время и фон в прошлом', 'exercise_type': 'multiple_choice',
             'prompt': 'Normalmente ella ___ temprano.', 'options': ['se levantaba', 'se levantó', 'se levanta'], 'correct_answer': 'se levantaba',
             'translation': 'Обычно она вставала рано.', 'explanation': 'Привычка → se levantaba.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Раньше я жил в маленькой деревне.»',
             'options': ['Antes vivía en un pueblo pequeño.', 'Antes viví en un pueblo pequeño.', 'Antes vivaba en un pueblo pequeño.'],
             'correct_answer': 'Antes vivía en un pueblo pequeño.', 'explanation': 'antes + imperfecto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мне было пятнадцать лет.»',
             'options': ['Tenía quince años.', 'Tuve quince años.', 'Era quince años.'],
             'correct_answer': 'Tenía quince años.', 'explanation': 'Возраст → tenía.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Каждый день мы говорили по-испански.»',
             'options': ['Todos los días hablábamos español.', 'Todos los días hablamos español ayer.', 'Cada día habláis español.'],
             'correct_answer': 'Todos los días hablábamos español.', 'explanation': 'Регулярность → hablábamos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Было холодно.»',
             'options': ['Hacía frío.', 'Hizo frío una vez para siempre.', 'Estaba frío el tiempo.'],
             'correct_answer': 'Hacía frío.', 'explanation': 'Погодный фон → hacía.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Она всегда слушала музыку.»',
             'options': ['Siempre escuchaba música.', 'Siempre escuchó música.', 'Siempre escucha música.'],
             'correct_answer': 'Siempre escuchaba música.', 'explanation': 'siempre + imperfecto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я не выносил шум.» (aguantar)',
             'options': ['No aguantaba el ruido.', 'No aguanté el ruido nunca jamás.', 'No aguanto el ruido.'],
             'correct_answer': 'No aguantaba el ruido.', 'explanation': 'Постоянное отношение → aguantaba.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Где ты работал раньше?»',
             'options': ['¿Dónde trabajabas antes?', '¿Dónde trabajaste mañana?', '¿Dónde trabajas antes?'],
             'correct_answer': '¿Dónde trabajabas antes?', 'explanation': 'antes → imperfecto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «В детстве он тосковал по морю.» (añorar)',
             'options': ['De niño añoraba el mar.', 'De niño añoró el mar.', 'De niño añora el mar.'],
             'correct_answer': 'De niño añoraba el mar.', 'explanation': 'de niño + imperfecto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Раньше здесь было кафе.»',
             'options': ['Antes había un café aquí.', 'Antes hubo un café aquí siempre.', 'Antes hay un café aquí.'],
             'correct_answer': 'Antes había un café aquí.', 'explanation': 'había — «имелось».'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы получали письма каждую неделю.»',
             'options': ['Recibíamos cartas cada semana.', 'Recibimos cartas ayer cada semana.', 'Recibíais cartas cada semana.'],
             'correct_answer': 'Recibíamos cartas cada semana.', 'explanation': 'Регулярность → recibíamos.'},
        ],
    },
    {
        'n': 18, 'level': 'A2', 'title': 'Imperfecto неправильных и возвратных глаголов',
        'theory': (
            '1. В imperfecto — только ТРИ неправильных глагола (легче всего в испанском!):\n\n'
            '• ser (быть): era, eras, era, éramos, erais, eran\n'
            '  De joven era muy tímido (в молодости я был очень застенчивым).\n'
            '• ir (идти/ехать): iba, ibas, iba, íbamos, ibais, iban\n'
            '  Iba al colegio en autobús (я ездил в школу на автобусе).\n'
            '• ver (видеть): veía, veías, veía, veíamos, veíais, veían\n'
            '  Veíamos esa serie cada noche (мы смотрели тот сериал каждый вечер).\n\n'
            '2. Возвратные глаголы в imperfecto сохраняют местоимение перед формой:\n'
            '  levantarse: me levantaba, te levantabas, se levantaba, nos levantábamos, '
            'os levantabais, se levantaban.\n'
            '  Antes me acostaba muy tarde (раньше я ложился очень поздно). '
            'Se despertaba a las seis (он просыпался в шесть).\n\n'
            '3. Imperfecto рядом с indefinido (забегая вперёд): imperfecto — ФОН и процесс, '
            'indefinido — СОБЫТИЕ, которое его прервало:\n'
            '• Mientras cenábamos, llamó mi madre (пока мы ужинали, позвонила моя мама);\n'
            '• Cuando era estudiante, conocí a mi mujer (когда я был студентом, я познакомился '
            'с женой).\n'
            'Союз mientras (пока) — верный спутник imperfecto.\n\n'
            '4. Сводная табличка окончаний:\n'
            '  -ar: -aba -abas -aba -ábamos -abais -aban\n'
            '  -er/-ir: -ía -ías -ía -íamos -íais -ían\n'
            '  ser: era… | ir: iba… | ver: veía…\n\n'
            '5. Полезный контраст: Era feliz (я был счастлив — фон) vs Fui feliz allí dos años '
            '(прожил там счастливо два года — законченный период; это уже indefinido, '
            'подробно — в уроках 26–28).'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Ser, ir, ver в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'De joven yo ___ (ser) muy tímido.', 'options': ['era', 'fui', 'soy'], 'correct_answer': 'era',
             'translation': 'В молодости я был очень застенчивым.', 'explanation': 'ser → era.'},
            {'section': 'Упражнение 1. Ser, ir, ver в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ (ser) buenos amigos.', 'options': ['éramos', 'fuimos', 'somos'], 'correct_answer': 'éramos',
             'translation': 'Мы были хорошими друзьями.', 'explanation': 'ser → éramos.'},
            {'section': 'Упражнение 1. Ser, ir, ver в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (ir) al colegio a pie.', 'options': ['iba', 'fui', 'voy'], 'correct_answer': 'iba',
             'translation': 'Я ходил в школу пешком.', 'explanation': 'ir → iba.'},
            {'section': 'Упражнение 1. Ser, ir, ver в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Cada verano ellos ___ (ir) al pueblo.', 'options': ['iban', 'fueron', 'van'], 'correct_answer': 'iban',
             'translation': 'Каждое лето они ездили в деревню.', 'explanation': 'Регулярность → iban.'},
            {'section': 'Упражнение 1. Ser, ir, ver в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ (ver) esa serie cada noche.', 'options': ['veíamos', 'vimos', 'vemos'], 'correct_answer': 'veíamos',
             'translation': 'Мы смотрели тот сериал каждый вечер.', 'explanation': 'ver → veíamos.'},
            {'section': 'Упражнение 1. Ser, ir, ver в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'De pequeña ella ___ (ver) mucho a sus abuelos.', 'options': ['veía', 'vio', 've'], 'correct_answer': 'veía',
             'translation': 'В детстве она часто виделась с бабушкой и дедушкой.', 'explanation': 'ver → veía.'},
            {'section': 'Упражнение 1. Ser, ir, ver в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': '¿Adónde ___ (ir, vosotros) los domingos?', 'options': ['ibais', 'fuisteis', 'vais'], 'correct_answer': 'ibais',
             'translation': 'Куда вы ходили по воскресеньям?', 'explanation': 'ir → ibais.'},
            {'section': 'Упражнение 1. Ser, ir, ver в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Mi abuelo ___ (ser) profesor.', 'options': ['era', 'fue', 'es'], 'correct_answer': 'era',
             'translation': 'Мой дедушка был учителем.', 'explanation': 'Характеристика → era.'},
            {'section': 'Упражнение 1. Ser, ir, ver в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Tú ___ (ser) el mejor de la clase, ¿no?', 'options': ['eras', 'fuiste', 'eres'], 'correct_answer': 'eras',
             'translation': 'Ты же был лучшим в классе?', 'explanation': 'ser → eras.'},
            {'section': 'Упражнение 1. Ser, ir, ver в imperfecto', 'exercise_type': 'fill_blank',
             'prompt': 'Yo no ___ (ver) bien sin gafas.', 'options': ['veía', 'vi', 'veo'], 'correct_answer': 'veía',
             'translation': 'Я плохо видел без очков.', 'explanation': 'Состояние → veía.'},
            # 2
            {'section': 'Упражнение 2. Возвратные глаголы и mientras', 'exercise_type': 'fill_blank',
             'prompt': 'Antes yo ___ acostaba muy tarde.', 'options': ['me', 'te', 'se'], 'correct_answer': 'me',
             'translation': 'Раньше я ложился очень поздно.', 'explanation': 'yo → me acostaba.'},
            {'section': 'Упражнение 2. Возвратные глаголы и mientras', 'exercise_type': 'fill_blank',
             'prompt': 'Él se ___ (despertar) a las seis.', 'options': ['despertaba', 'despertó', 'despierta'], 'correct_answer': 'despertaba',
             'translation': 'Он просыпался в шесть.', 'explanation': 'Привычка → despertaba.'},
            {'section': 'Упражнение 2. Возвратные глаголы и mientras', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ levantábamos temprano.', 'options': ['nos', 'os', 'se'], 'correct_answer': 'nos',
             'translation': 'Мы вставали рано.', 'explanation': 'nosotros → nos.'},
            {'section': 'Упражнение 2. Возвратные глаголы и mientras', 'exercise_type': 'fill_blank',
             'prompt': '___ cenábamos, llamó mi madre.', 'options': ['Mientras', 'Siempre', 'Ayer'], 'correct_answer': 'Mientras',
             'translation': 'Пока мы ужинали, позвонила мама.', 'explanation': 'mientras + imperfecto (фон).'},
            {'section': 'Упражнение 2. Возвратные глаголы и mientras', 'exercise_type': 'multiple_choice',
             'prompt': 'Mientras yo ___ (leer), sonó el teléfono.', 'options': ['leía', 'leí', 'leo'], 'correct_answer': 'leía',
             'translation': 'Пока я читал, зазвонил телефон.', 'explanation': 'Процесс-фон → leía.'},
            {'section': 'Упражнение 2. Возвратные глаголы и mientras', 'exercise_type': 'multiple_choice',
             'prompt': 'Cuando ___ estudiante, conocí a mi mujer.', 'options': ['era', 'fui', 'soy'], 'correct_answer': 'era',
             'translation': 'Когда я был студентом, я познакомился с женой.', 'explanation': 'Фон → era; событие → conocí.'},
            {'section': 'Упражнение 2. Возвратные глаголы и mientras', 'exercise_type': 'multiple_choice',
             'prompt': 'Что здесь ФОН? «Mientras cenábamos, llamó mi madre.»', 'options': ['cenábamos', 'llamó'], 'correct_answer': 'cenábamos',
             'translation': 'Пока мы ужинали, позвонила мама.', 'explanation': 'Imperfecto = фон, indefinido = событие.'},
            {'section': 'Упражнение 2. Возвратные глаголы и mientras', 'exercise_type': 'fill_blank',
             'prompt': 'Vosotros os ___ (duchar) por la noche, ¿verdad?', 'options': ['duchabais', 'duchasteis', 'ducháis'], 'correct_answer': 'duchabais',
             'translation': 'Вы принимали душ по вечерам, верно?', 'explanation': 'os duchabais.'},
            {'section': 'Упражнение 2. Возвратные глаголы и mientras', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ vestían muy elegante.', 'options': ['se', 'os', 'nos'], 'correct_answer': 'se',
             'translation': 'Они очень элегантно одевались.', 'explanation': 'ellos → se vestían.'},
            {'section': 'Упражнение 2. Возвратные глаголы и mientras', 'exercise_type': 'multiple_choice',
             'prompt': 'Mientras ella ___ (ducharse), yo preparaba el café.', 'options': ['se duchaba', 'se duchó', 'se ducha'], 'correct_answer': 'se duchaba',
             'translation': 'Пока она принимала душ, я готовил кофе.', 'explanation': 'Два параллельных фона → оба imperfecto.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «В детстве она была очень застенчивой.»',
             'options': ['De pequeña era muy tímida.', 'De pequeña fue muy tímida.', 'De pequeña es muy tímida.'],
             'correct_answer': 'De pequeña era muy tímida.', 'explanation': 'Описание → era.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я ездил на работу на метро.»',
             'options': ['Iba al trabajo en metro.', 'Fui al trabajo en metro ayer.', 'Voy al trabajo en metro.'],
             'correct_answer': 'Iba al trabajo en metro.', 'explanation': 'Привычка → iba.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы смотрели телевизор каждый вечер.»',
             'options': ['Veíamos la tele cada noche.', 'Vimos la tele cada noche una vez.', 'Vemos la tele cada noche.'],
             'correct_answer': 'Veíamos la tele cada noche.', 'explanation': 'ver → veíamos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Пока я читал, зазвонил телефон.»',
             'options': ['Mientras leía, sonó el teléfono.', 'Mientras leí, sonaba el teléfono.', 'Mientras leo, sonó el teléfono.'],
             'correct_answer': 'Mientras leía, sonó el teléfono.', 'explanation': 'Фон (leía) + событие (sonó).'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Раньше я вставал в шесть.»',
             'options': ['Antes me levantaba a las seis.', 'Antes me levanté a las seis.', 'Antes levantaba a las seis.'],
             'correct_answer': 'Antes me levantaba a las seis.', 'explanation': 'me levantaba.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы были соседями.»',
             'options': ['Éramos vecinos.', 'Fuimos vecinos ayer.', 'Somos vecinos.'],
             'correct_answer': 'Éramos vecinos.', 'explanation': 'ser → éramos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Куда ты ходил по субботам?»',
             'options': ['¿Adónde ibas los sábados?', '¿Adónde fuiste los sábados una vez?', '¿Adónde vas los sábados?'],
             'correct_answer': '¿Adónde ibas los sábados?', 'explanation': 'Регулярность → ibas.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он плохо видел без очков.»',
             'options': ['No veía bien sin gafas.', 'No vio bien sin gafas.', 'No ve bien sin gafas.'],
             'correct_answer': 'No veía bien sin gafas.', 'explanation': 'Состояние → veía.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Пока она принимала душ, я готовил завтрак.»',
             'options': ['Mientras se duchaba, yo preparaba el desayuno.', 'Mientras se duchó, yo preparé el desayuno.', 'Mientras se ducha, yo preparaba el desayuno.'],
             'correct_answer': 'Mientras se duchaba, yo preparaba el desayuno.', 'explanation': 'Два фона → оба imperfecto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Когда мне было десять, мы жили у моря.»',
             'options': ['Cuando tenía diez años, vivíamos junto al mar.', 'Cuando tuve diez años, vivimos junto al mar.', 'Cuando tengo diez años, vivíamos junto al mar.'],
             'correct_answer': 'Cuando tenía diez años, vivíamos junto al mar.', 'explanation': 'Оба — фон детства → imperfecto.'},
        ],
    },
    {
        'n': 19, 'level': 'A2', 'title': 'Вопросы с предлогами. Tanto/tan. Внешность',
        'theory': (
            '1. Предлог в испанском вопросе ставится ПЕРЕД вопросительным словом — никогда '
            'в конце (в отличие от английского):\n'
            '• ¿Con quién vives? (с кем ты живёшь?) — Vivo con mi hermano.\n'
            '• ¿De qué habláis? (о чём вы говорите?) — Hablamos de la película.\n'
            '• ¿De dónde eres? (откуда ты?) — Soy de Rusia.\n'
            '• ¿A quién esperas? (кого ты ждёшь?) — Espero a María.\n'
            '• ¿Para quién es el regalo? (для кого подарок?)\n'
            '• ¿En qué trabajas? (кем ты работаешь? досл. «в чём»)\n'
            '• ¿De quién es este coche? (чья это машина?)\n\n'
            '2. Сравнение равенства tanto/tan («такой же… как», «столько же… сколько»):\n'
            '• tan + ПРИЛАГАТЕЛЬНОЕ/НАРЕЧИЕ + como: Es tan alto como su padre (он такой же '
            'высокий, как его отец). Habla tan rápido como tú.\n'
            '• tanto/-a/-os/-as + СУЩЕСТВИТЕЛЬНОЕ + como (согласуется!): Tengo tantos libros '
            'como tú (у меня столько же книг, сколько у тебя). Hay tanta gente como ayer.\n'
            '• глагол + tanto como: Trabaja tanto como yo (он работает столько же, сколько я).\n'
            'В восклицаниях: ¡Tanto tiempo! (сколько лет, сколько зим!) ¡Es tan bonito! '
            '(это так красиво!)\n\n'
            '3. Описание внешности (постоянные черты — через ser и tener):\n'
            '• рост/сложение: alto (высокий), bajo (низкий), delgado (худой), fuerte (крепкий);\n'
            '• волосы: Tiene el pelo largo / corto / rubio / moreno / rizado (у него длинные / '
            'короткие / светлые / тёмные / кудрявые волосы);\n'
            '• глаза: Tiene los ojos azules / verdes / marrones;\n'
            '• общее: guapo (красивый), joven (молодой), mayor (пожилой); lleva gafas / barba '
            '(носит очки / бороду).\n\n'
            'Пример-портрет: Mi hermana es alta y delgada, tiene el pelo moreno y los ojos '
            'verdes, y es tan simpática como mi madre. Que yo sepa, no lleva gafas '
            '(насколько я знаю, очки она не носит).'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Вопрос с предлогом', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ quién vives? — Con mi hermano.', 'options': ['Con', 'De', 'A'], 'correct_answer': 'Con',
             'translation': 'С кем ты живёшь? — С братом.', 'explanation': 'Ответ con → вопрос ¿Con quién?'},
            {'section': 'Упражнение 1. Вопрос с предлогом', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ qué habláis? — De la película.', 'options': ['De', 'En', 'Con'], 'correct_answer': 'De',
             'translation': 'О чём вы говорите? — О фильме.', 'explanation': 'hablar de → ¿De qué?'},
            {'section': 'Упражнение 1. Вопрос с предлогом', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ dónde eres? — De Ucrania.', 'options': ['De', 'A', 'En'], 'correct_answer': 'De',
             'translation': 'Откуда ты? — Из Украины.', 'explanation': 'ser de → ¿De dónde?'},
            {'section': 'Упражнение 1. Вопрос с предлогом', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ quién esperas? — A María.', 'options': ['A', 'De', 'Para'], 'correct_answer': 'A',
             'translation': 'Кого ты ждёшь? — Марию.', 'explanation': 'esperar a (личное a) → ¿A quién?'},
            {'section': 'Упражнение 1. Вопрос с предлогом', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ quién es el regalo? — Para mi madre.', 'options': ['Para', 'Por', 'De'], 'correct_answer': 'Para',
             'translation': 'Для кого подарок? — Для мамы.', 'explanation': 'para → ¿Para quién?'},
            {'section': 'Упражнение 1. Вопрос с предлогом', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ qué trabajas? — Soy programador.', 'options': ['En', 'De', 'A'], 'correct_answer': 'En',
             'translation': 'Кем ты работаешь? — Я программист.', 'explanation': 'trabajar en → ¿En qué?'},
            {'section': 'Упражнение 1. Вопрос с предлогом', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ quién es este coche? — De Juan.', 'options': ['De', 'A', 'Con'], 'correct_answer': 'De',
             'translation': 'Чья это машина? — Хуана.', 'explanation': 'Принадлежность → ¿De quién?'},
            {'section': 'Упражнение 1. Вопрос с предлогом', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ qué piensas? — En las vacaciones.', 'options': ['En', 'De', 'Por'], 'correct_answer': 'En',
             'translation': 'О чём ты думаешь? — Об отпуске.', 'explanation': 'pensar en → ¿En qué?'},
            {'section': 'Упражнение 1. Вопрос с предлогом', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ quiénes vais al cine? — Con unos amigos.', 'options': ['Con', 'A', 'De'], 'correct_answer': 'Con',
             'translation': 'С кем вы идёте в кино? — С друзьями.', 'explanation': 'con + quiénes (мн.).'},
            {'section': 'Упражнение 1. Вопрос с предлогом', 'exercise_type': 'multiple_choice',
             'prompt': 'Правильный порядок:', 'options': ['¿Con quién hablas?', '¿Quién hablas con?', '¿Hablas con quién tú?'], 'correct_answer': '¿Con quién hablas?',
             'translation': 'С кем ты говоришь?', 'explanation': 'Предлог всегда перед вопросительным словом.'},
            # 2
            {'section': 'Упражнение 2. Tanto или tan?', 'exercise_type': 'multiple_choice',
             'prompt': 'Es ___ alto como su padre.', 'options': ['tan', 'tanto', 'tantos'], 'correct_answer': 'tan',
             'translation': 'Он такой же высокий, как его отец.', 'explanation': 'Перед прилагательным → tan.'},
            {'section': 'Упражнение 2. Tanto или tan?', 'exercise_type': 'multiple_choice',
             'prompt': 'Tengo ___ libros como tú.', 'options': ['tantos', 'tan', 'tanto'], 'correct_answer': 'tantos',
             'translation': 'У меня столько же книг, сколько у тебя.', 'explanation': 'libros — м. р. мн.: tantos.'},
            {'section': 'Упражнение 2. Tanto или tan?', 'exercise_type': 'multiple_choice',
             'prompt': 'Hay ___ gente como ayer.', 'options': ['tanta', 'tan', 'tanto'], 'correct_answer': 'tanta',
             'translation': 'Народу столько же, сколько вчера.', 'explanation': 'gente — ж. р.: tanta.'},
            {'section': 'Упражнение 2. Tanto или tan?', 'exercise_type': 'multiple_choice',
             'prompt': 'Trabaja ___ como yo.', 'options': ['tanto', 'tan', 'tanta'], 'correct_answer': 'tanto',
             'translation': 'Он работает столько же, сколько я.', 'explanation': 'После глагола → tanto (не меняется).'},
            {'section': 'Упражнение 2. Tanto или tan?', 'exercise_type': 'multiple_choice',
             'prompt': 'Habla ___ rápido como un nativo.', 'options': ['tan', 'tanto', 'tanta'], 'correct_answer': 'tan',
             'translation': 'Он говорит так же быстро, как носитель.', 'explanation': 'Перед наречием → tan.'},
            {'section': 'Упражнение 2. Tanto или tan?', 'exercise_type': 'multiple_choice',
             'prompt': '¡___ tiempo sin verte!', 'options': ['Tanto', 'Tan', 'Tantos'], 'correct_answer': 'Tanto',
             'translation': 'Сколько лет, сколько зим!', 'explanation': 'tiempo — сущ.: tanto.'},
            {'section': 'Упражнение 2. Tanto или tan?', 'exercise_type': 'multiple_choice',
             'prompt': '¡Es ___ bonito!', 'options': ['tan', 'tanto', 'tanta'], 'correct_answer': 'tan',
             'translation': 'Это так красиво!', 'explanation': 'Восклицание с прилагательным → tan.'},
            {'section': 'Упражнение 2. Tanto или tan?', 'exercise_type': 'multiple_choice',
             'prompt': 'Ella tiene ___ ganas de viajar como yo.', 'options': ['tantas', 'tan', 'tanto'], 'correct_answer': 'tantas',
             'translation': 'Ей так же хочется путешествовать, как и мне.', 'explanation': 'ganas — ж. р. мн.: tantas.'},
            {'section': 'Упражнение 2. Tanto или tan?', 'exercise_type': 'multiple_choice',
             'prompt': 'No como ___ como antes.', 'options': ['tanto', 'tan', 'tantos'], 'correct_answer': 'tanto',
             'translation': 'Я ем не столько, сколько раньше.', 'explanation': 'Глагол + tanto como.'},
            {'section': 'Упражнение 2. Tanto или tan?', 'exercise_type': 'multiple_choice',
             'prompt': 'Es ___ simpática como su madre.', 'options': ['tan', 'tanta', 'tanto'], 'correct_answer': 'tan',
             'translation': 'Она такая же милая, как её мама.', 'explanation': 'tan + прилагательное.'},
            # 3
            {'section': 'Упражнение 3. Внешность. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «С кем ты живёшь?»',
             'options': ['¿Con quién vives?', '¿Quién vives con?', '¿Con quien vives?'],
             'correct_answer': '¿Con quién vives?', 'explanation': 'Предлог перед quién (с тильдой).'},
            {'section': 'Упражнение 3. Внешность. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «У неё длинные волосы.»',
             'options': ['Tiene el pelo largo.', 'Es el pelo largo.', 'Tiene la pelo larga.'],
             'correct_answer': 'Tiene el pelo largo.', 'explanation': 'tener + el pelo + прилагательное.'},
            {'section': 'Упражнение 3. Внешность. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «У него голубые глаза.»',
             'options': ['Tiene los ojos azules.', 'Es los ojos azules.', 'Tiene ojos los azules.'],
             'correct_answer': 'Tiene los ojos azules.', 'explanation': 'tener los ojos + цвет (мн.).'},
            {'section': 'Упражнение 3. Внешность. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Моя сестра высокая и худая.»',
             'options': ['Mi hermana es alta y delgada.', 'Mi hermana está alta y delgada.', 'Mi hermana es alto y delgado.'],
             'correct_answer': 'Mi hermana es alta y delgada.', 'explanation': 'Внешность → ser; ж. р.'},
            {'section': 'Упражнение 3. Внешность. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он носит очки и бороду.»',
             'options': ['Lleva gafas y barba.', 'Tiene que gafas y barba.', 'Es gafas y barba.'],
             'correct_answer': 'Lleva gafas y barba.', 'explanation': 'llevar — носить.'},
            {'section': 'Упражнение 3. Внешность. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Он такой же высокий, как ты.»',
             'options': ['Es tan alto como tú.', 'Es tanto alto como tú.', 'Es tan alto que tú.'],
             'correct_answer': 'Es tan alto como tú.', 'explanation': 'tan … como.'},
            {'section': 'Упражнение 3. Внешность. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «О чём вы говорите?»',
             'options': ['¿De qué habláis?', '¿Qué habláis de?', '¿De que habláis?'],
             'correct_answer': '¿De qué habláis?', 'explanation': 'de + qué (с тильдой).'},
            {'section': 'Упражнение 3. Внешность. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Насколько я знаю, она не носит очки.»',
             'options': ['Que yo sepa, no lleva gafas.', 'Que yo sé, no lleva gafas.', 'Como yo sepa, no lleva gafas.'],
             'correct_answer': 'Que yo sepa, no lleva gafas.', 'explanation': 'que yo sepa — «насколько я знаю».'},
            {'section': 'Упражнение 3. Внешность. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «У меня столько же работы, сколько вчера.»',
             'options': ['Tengo tanto trabajo como ayer.', 'Tengo tan trabajo como ayer.', 'Tengo tantos trabajo como ayer.'],
             'correct_answer': 'Tengo tanto trabajo como ayer.', 'explanation': 'trabajo — м. р. ед.: tanto.'},
            {'section': 'Упражнение 3. Внешность. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Для кого эти цветы?»',
             'options': ['¿Para quién son estas flores?', '¿Por quién son estas flores?', '¿Quién son estas flores para?'],
             'correct_answer': '¿Para quién son estas flores?', 'explanation': 'para quién + son (мн.).'},
        ],
    },
]

_C = [
    {
        'n': 20, 'level': 'A2', 'title': 'Местоимения-дополнения. Poder, saber, conocer',
        'theory': (
            '1. Местоимения-дополнения заменяют существительные, чтобы не повторяться.\n\n'
            'ПРЯМОЕ дополнение (кого? что?): me, te, lo/la, nos, os, los/las:\n'
            '• ¿Ves a Ana? — Sí, la veo (да, я её вижу).\n'
            '• ¿Compras el pan? — Sí, lo compro.\n'
            '• ¿Nos escuchas? — Sí, os escucho.\n\n'
            'КОСВЕННОЕ дополнение (кому? чему?): me, te, le, nos, os, les:\n'
            '• Le escribo una carta (a María) — я пишу ей письмо.\n'
            '• Les doy las gracias (a mis padres) — я благодарю их.\n'
            'Формы различаются только в 3 лице: lo/la/los/las (прямое) против le/les (косвенное).\n\n'
            '2. Место: перед спрягаемым глаголом (Lo veo. No lo veo.) или приклеенным к '
            'инфинитиву: Quiero verlo (хочу это увидеть) = Lo quiero ver.\n\n'
            '3. Три глагола, которые путают:\n'
            '• poder (o→ue) — мочь (возможность/разрешение): puedo, puedes, puede, podemos, '
            'podéis, pueden. ¿Puedo pasar? (можно войти?) No puedo ir hoy.\n'
            '• saber — знать факт/информацию, уметь: sé, sabes, sabe, sabemos, sabéis, saben. '
            'Sé la respuesta (я знаю ответ). Sé nadar (я умею плавать). Que yo sepa… '
            '(насколько я знаю…)\n'
            '• conocer — быть знакомым с человеком/местом: conozco, conoces, conoce… '
            'Conozco a María (я знаком с Марией). ¿Conoces Madrid? (ты бывал в Мадриде?)\n\n'
            'Сравните: Sé dónde vive (знаю, где он живёт) — Conozco su casa (я знаю его дом, '
            'бывал там). Sé nadar (умею) — Puedo nadar hoy (могу сегодня — есть возможность).\n\n'
            '4. С дополнением-человеком не забывайте личное a: Conozco a tu hermano. '
            'Veo a los niños. Заменяя местоимением: Lo conozco. Los veo.'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Замените дополнение местоимением', 'exercise_type': 'multiple_choice',
             'prompt': '¿Ves a Ana? — Sí, ___ veo.', 'options': ['la', 'lo', 'le'], 'correct_answer': 'la',
             'translation': 'Видишь Ану? — Да, я её вижу.', 'explanation': 'Ana — прямое ж. р. → la.'},
            {'section': 'Упражнение 1. Замените дополнение местоимением', 'exercise_type': 'multiple_choice',
             'prompt': '¿Compras el pan? — Sí, ___ compro.', 'options': ['lo', 'la', 'le'], 'correct_answer': 'lo',
             'translation': 'Купишь хлеб? — Да, куплю (его).', 'explanation': 'el pan — прямое м. р. → lo.'},
            {'section': 'Упражнение 1. Замените дополнение местоимением', 'exercise_type': 'multiple_choice',
             'prompt': '¿Lees las noticias? — Sí, ___ leo.', 'options': ['las', 'los', 'les'], 'correct_answer': 'las',
             'translation': 'Читаешь новости? — Да, читаю (их).', 'explanation': 'las noticias → las.'},
            {'section': 'Упражнение 1. Замените дополнение местоимением', 'exercise_type': 'multiple_choice',
             'prompt': 'A María ___ escribo una carta.', 'options': ['le', 'la', 'lo'], 'correct_answer': 'le',
             'translation': 'Марии я пишу письмо.', 'explanation': 'Кому → косвенное le.'},
            {'section': 'Упражнение 1. Замените дополнение местоимением', 'exercise_type': 'multiple_choice',
             'prompt': 'A mis padres ___ doy las gracias.', 'options': ['les', 'los', 'las'], 'correct_answer': 'les',
             'translation': 'Родителей я благодарю (им даю благодарность).', 'explanation': 'Кому мн. → les.'},
            {'section': 'Упражнение 1. Замените дополнение местоимением', 'exercise_type': 'multiple_choice',
             'prompt': '¿Me escuchas? — Sí, ___ escucho.', 'options': ['te', 'me', 'le'], 'correct_answer': 'te',
             'translation': 'Ты меня слушаешь? — Да, я тебя слушаю.', 'explanation': 'Тебя → te.'},
            {'section': 'Упражнение 1. Замените дополнение местоимением', 'exercise_type': 'multiple_choice',
             'prompt': '¿Compras los billetes? — Sí, ___ compro.', 'options': ['los', 'las', 'les'], 'correct_answer': 'los',
             'translation': 'Купишь билеты? — Да, куплю (их).', 'explanation': 'los billetes → los.'},
            {'section': 'Упражнение 1. Замените дополнение местоимением', 'exercise_type': 'multiple_choice',
             'prompt': 'Quiero ver___ mañana. (это)', 'options': ['lo', 'le', 'la'], 'correct_answer': 'lo',
             'translation': 'Я хочу увидеть это завтра.', 'explanation': 'К инфинитиву: verlo.'},
            {'section': 'Упражнение 1. Замените дополнение местоимением', 'exercise_type': 'multiple_choice',
             'prompt': 'No ___ veo bien. (тебя)', 'options': ['te', 'me', 'le'], 'correct_answer': 'te',
             'translation': 'Я тебя плохо вижу.', 'explanation': 'no + te + глагол.'},
            {'section': 'Упражнение 1. Замените дополнение местоимением', 'exercise_type': 'multiple_choice',
             'prompt': 'A ella ___ regalo flores.', 'options': ['le', 'la', 'les'], 'correct_answer': 'le',
             'translation': 'Ей я дарю цветы.', 'explanation': 'Кому → le.'},
            # 2
            {'section': 'Упражнение 2. Poder, saber или conocer?', 'exercise_type': 'multiple_choice',
             'prompt': '___ nadar muy bien. (умею)', 'options': ['Sé', 'Puedo', 'Conozco'], 'correct_answer': 'Sé',
             'translation': 'Я очень хорошо умею плавать.', 'explanation': 'Навык → saber.'},
            {'section': 'Упражнение 2. Poder, saber или conocer?', 'exercise_type': 'multiple_choice',
             'prompt': 'No ___ nadar hoy: la piscina está cerrada.', 'options': ['puedo', 'sé', 'conozco'], 'correct_answer': 'puedo',
             'translation': 'Сегодня я не могу поплавать: бассейн закрыт.', 'explanation': 'Возможность → poder.'},
            {'section': 'Упражнение 2. Poder, saber или conocer?', 'exercise_type': 'multiple_choice',
             'prompt': '___ a tu hermano: es muy simpático.', 'options': ['Conozco', 'Sé', 'Puedo'], 'correct_answer': 'Conozco',
             'translation': 'Я знаком с твоим братом: он очень милый.', 'explanation': 'Знаком с человеком → conocer.'},
            {'section': 'Упражнение 2. Poder, saber или conocer?', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ dónde vive María?', 'options': ['Sabes', 'Conoces', 'Puedes'], 'correct_answer': 'Sabes',
             'translation': 'Ты знаешь, где живёт Мария?', 'explanation': 'Факт → saber.'},
            {'section': 'Упражнение 2. Poder, saber или conocer?', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ Madrid? — Sí, es precioso.', 'options': ['Conoces', 'Sabes', 'Puedes'], 'correct_answer': 'Conoces',
             'translation': 'Ты бывал в Мадриде? — Да, он прекрасен.', 'explanation': 'Знаком с местом → conocer.'},
            {'section': 'Упражнение 2. Poder, saber или conocer?', 'exercise_type': 'multiple_choice',
             'prompt': '¿___ pasar? — Claro, adelante.', 'options': ['Puedo', 'Sé', 'Conozco'], 'correct_answer': 'Puedo',
             'translation': 'Можно войти? — Конечно, проходи.', 'explanation': 'Разрешение → poder.'},
            {'section': 'Упражнение 2. Poder, saber или conocer?', 'exercise_type': 'multiple_choice',
             'prompt': 'Nosotros no ___ (poder) ir a la fiesta.', 'options': ['podemos', 'pudemos', 'puedemos'], 'correct_answer': 'podemos',
             'translation': 'Мы не можем пойти на праздник.', 'explanation': 'nosotros без чередования: podemos.'},
            {'section': 'Упражнение 2. Poder, saber или conocer?', 'exercise_type': 'multiple_choice',
             'prompt': 'Yo ___ (conocer) bien esta ciudad.', 'options': ['conozco', 'conoco', 'conozo'], 'correct_answer': 'conozco',
             'translation': 'Я хорошо знаю этот город.', 'explanation': '1 л.: conozco.'},
            {'section': 'Упражнение 2. Poder, saber или conocer?', 'exercise_type': 'multiple_choice',
             'prompt': 'Que yo ___ , la tienda abre a las diez.', 'options': ['sepa', 'sé', 'sabe'], 'correct_answer': 'sepa',
             'translation': 'Насколько я знаю, магазин открывается в десять.', 'explanation': 'Оборот que yo sepa.'},
            {'section': 'Упражнение 2. Poder, saber или conocer?', 'exercise_type': 'multiple_choice',
             'prompt': 'Ellos ___ (poder) ayudarte.', 'options': ['pueden', 'poden', 'podéis'], 'correct_answer': 'pueden',
             'translation': 'Они могут тебе помочь.', 'explanation': 'o→ue: pueden.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я её вижу.»',
             'options': ['La veo.', 'Le veo.', 'Veo la.'],
             'correct_answer': 'La veo.', 'explanation': 'Прямое ж. р. → la перед глаголом.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я тебе пишу письмо.»',
             'options': ['Te escribo una carta.', 'Escribo te una carta.', 'Ti escribo una carta.'],
             'correct_answer': 'Te escribo una carta.', 'explanation': 'te перед глаголом.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я это знаю.»',
             'options': ['Lo sé.', 'Le sé.', 'Sé lo.'],
             'correct_answer': 'Lo sé.', 'explanation': 'lo + sé.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я знаком с Марией.»',
             'options': ['Conozco a María.', 'Sé a María.', 'Conozco María.'],
             'correct_answer': 'Conozco a María.', 'explanation': 'conocer + личное a.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Ты умеешь готовить?»',
             'options': ['¿Sabes cocinar?', '¿Puedes cocinar?', '¿Conoces cocinar?'],
             'correct_answer': '¿Sabes cocinar?', 'explanation': 'Навык → saber + инф.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Можно открыть окно?»',
             'options': ['¿Puedo abrir la ventana?', '¿Sé abrir la ventana?', '¿Conozco abrir la ventana?'],
             'correct_answer': '¿Puedo abrir la ventana?', 'explanation': 'Разрешение → poder.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я хочу это купить.»',
             'options': ['Quiero comprarlo.', 'Quiero lo comprar.', 'Lo quiero comprarlo.'],
             'correct_answer': 'Quiero comprarlo.', 'explanation': 'К инфинитиву: comprarlo.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Им я говорю правду.»',
             'options': ['Les digo la verdad.', 'Los digo la verdad.', 'Digo les la verdad.'],
             'correct_answer': 'Les digo la verdad.', 'explanation': 'Кому мн. → les.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я его не выношу.» (aguantar)',
             'options': ['No lo aguanto.', 'No le aguanto lo.', 'Aguanto no lo.'],
             'correct_answer': 'No lo aguanto.', 'explanation': 'no + lo + aguanto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Ты знаешь этот город? (бывал)»',
             'options': ['¿Conoces esta ciudad?', '¿Sabes esta ciudad?', '¿Puedes esta ciudad?'],
             'correct_answer': '¿Conoces esta ciudad?', 'explanation': 'Знаком с местом → conocer.'},
        ],
    },
    {
        'n': 21, 'level': 'A2', 'title': 'Безличная форма se и согласование',
        'theory': (
            '1. Конструкция с se позволяет говорить обобщённо, не называя деятеля — '
            'по-русски «здесь говорят», «продаётся», «так делают».\n\n'
            '2. Пассивно-возвратная форма (se + глагол, согласованный с предметом):\n'
            '• Se vende piso (продаётся квартира) — Se venden pisos (продаются квартиры);\n'
            '• Se habla español (здесь говорят по-испански);\n'
            '• Se necesitan camareros (требуются официанты);\n'
            '• ¿Cómo se escribe tu nombre? (как пишется твоё имя?)\n'
            'Глагол в ед. или мн. числе — по существительному!\n\n'
            '3. Чисто безличная форма (se + глагол ТОЛЬКО в ед. числе) — об образе жизни, '
            'правилах, обычаях:\n'
            '• En España se cena tarde (в Испании поздно ужинают);\n'
            '• Aquí se trabaja mucho (здесь много работают);\n'
            '• No se puede fumar aquí (здесь нельзя курить);\n'
            '• ¿Cómo se dice «спасибо» en español? — Se dice «gracias».\n'
            'Формула вежливого запрета/разрешения: (no) se puede + инфинитив.\n\n'
            '4. Se dice que… (говорят, что…) — удобный способ передать слухи и общее мнение: '
            'Se dice que este restaurante es muy bueno (говорят, этот ресторан очень хорош).\n\n'
            '5. Согласование прилагательных (повторение на новом материале): прилагательное '
            'согласуется с существительным всегда, в т. ч. в se-конструкциях: '
            'Se venden coches usados (продаются подержанные машины). '
            'Se alquila habitación luminosa (сдаётся светлая комната).\n\n'
            'Мини-объявления — типичное место se-конструкций: SE VENDE, SE ALQUILA, '
            'SE BUSCA, SE NECESITA.'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Согласуйте глагол с существительным', 'exercise_type': 'multiple_choice',
             'prompt': 'Se ___ piso. (одна квартира)', 'options': ['vende', 'venden', 'vendo'], 'correct_answer': 'vende',
             'translation': 'Продаётся квартира.', 'explanation': 'Ед. ч. → vende.'},
            {'section': 'Упражнение 1. Согласуйте глагол с существительным', 'exercise_type': 'multiple_choice',
             'prompt': 'Se ___ pisos. (много)', 'options': ['venden', 'vende', 'vendemos'], 'correct_answer': 'venden',
             'translation': 'Продаются квартиры.', 'explanation': 'Мн. ч. → venden.'},
            {'section': 'Упражнение 1. Согласуйте глагол с существительным', 'exercise_type': 'multiple_choice',
             'prompt': 'Aquí se ___ español.', 'options': ['habla', 'hablan', 'hablo'], 'correct_answer': 'habla',
             'translation': 'Здесь говорят по-испански.', 'explanation': 'español — ед. → habla.'},
            {'section': 'Упражнение 1. Согласуйте глагол с существительным', 'exercise_type': 'multiple_choice',
             'prompt': 'Se ___ camareros.', 'options': ['necesitan', 'necesita', 'necesito'], 'correct_answer': 'necesitan',
             'translation': 'Требуются официанты.', 'explanation': 'camareros — мн. → necesitan.'},
            {'section': 'Упражнение 1. Согласуйте глагол с существительным', 'exercise_type': 'multiple_choice',
             'prompt': 'Se ___ habitación luminosa.', 'options': ['alquila', 'alquilan', 'alquilo'], 'correct_answer': 'alquila',
             'translation': 'Сдаётся светлая комната.', 'explanation': 'Ед. ч. → alquila.'},
            {'section': 'Упражнение 1. Согласуйте глагол с существительным', 'exercise_type': 'multiple_choice',
             'prompt': 'Se ___ coches usados.', 'options': ['venden', 'vende', 'vendéis'], 'correct_answer': 'venden',
             'translation': 'Продаются подержанные машины.', 'explanation': 'coches — мн. → venden.'},
            {'section': 'Упражнение 1. Согласуйте глагол с существительным', 'exercise_type': 'multiple_choice',
             'prompt': '¿Cómo se ___ tu nombre?', 'options': ['escribe', 'escriben', 'escribes'], 'correct_answer': 'escribe',
             'translation': 'Как пишется твоё имя?', 'explanation': 'nombre — ед. → escribe.'},
            {'section': 'Упражнение 1. Согласуйте глагол с существительным', 'exercise_type': 'multiple_choice',
             'prompt': 'Se ___ dos dependientes para la tienda.', 'options': ['buscan', 'busca', 'buscamos'], 'correct_answer': 'buscan',
             'translation': 'Ищут двух продавцов в магазин.', 'explanation': 'dos → мн.: buscan.'},
            {'section': 'Упражнение 1. Согласуйте глагол с существительным', 'exercise_type': 'multiple_choice',
             'prompt': 'En este restaurante se ___ paella riquísima.', 'options': ['prepara', 'preparan', 'preparo'], 'correct_answer': 'prepara',
             'translation': 'В этом ресторане готовят вкуснейшую паэлью.', 'explanation': 'paella — ед. → prepara.'},
            {'section': 'Упражнение 1. Согласуйте глагол с существительным', 'exercise_type': 'multiple_choice',
             'prompt': 'Se ___ entradas en la taquilla.', 'options': ['venden', 'vende', 'vendo'], 'correct_answer': 'venden',
             'translation': 'Билеты продаются в кассе.', 'explanation': 'entradas — мн. → venden.'},
            # 2
            {'section': 'Упражнение 2. Безличные обороты', 'exercise_type': 'multiple_choice',
             'prompt': 'En España se ___ tarde.', 'options': ['cena', 'cenan', 'cenamos'], 'correct_answer': 'cena',
             'translation': 'В Испании поздно ужинают.', 'explanation': 'Безличное → только ед. ч.'},
            {'section': 'Упражнение 2. Безличные обороты', 'exercise_type': 'multiple_choice',
             'prompt': 'Aquí se ___ mucho.', 'options': ['trabaja', 'trabajan', 'trabajo'], 'correct_answer': 'trabaja',
             'translation': 'Здесь много работают.', 'explanation': 'Безличное → trabaja.'},
            {'section': 'Упражнение 2. Безличные обороты', 'exercise_type': 'multiple_choice',
             'prompt': 'No se ___ fumar aquí.', 'options': ['puede', 'pueden', 'puedo'], 'correct_answer': 'puede',
             'translation': 'Здесь нельзя курить.', 'explanation': 'no se puede + инф.'},
            {'section': 'Упражнение 2. Безличные обороты', 'exercise_type': 'multiple_choice',
             'prompt': '¿Cómo se ___ «спасибо» en español?', 'options': ['dice', 'dicen', 'digo'], 'correct_answer': 'dice',
             'translation': 'Как сказать «спасибо» по-испански?', 'explanation': 'se dice — «говорится».'},
            {'section': 'Упражнение 2. Безличные обороты', 'exercise_type': 'multiple_choice',
             'prompt': 'Se ___ que este bar es muy bueno.', 'options': ['dice', 'dicen', 'digo'], 'correct_answer': 'dice',
             'translation': 'Говорят, этот бар очень хорош.', 'explanation': 'se dice que — говорят, что.'},
            {'section': 'Упражнение 2. Безличные обороты', 'exercise_type': 'multiple_choice',
             'prompt': '¿Se ___ pagar con tarjeta?', 'options': ['puede', 'pueden', 'puedes'], 'correct_answer': 'puede',
             'translation': 'Можно заплатить картой?', 'explanation': 'se puede + инф.'},
            {'section': 'Упражнение 2. Безличные обороты', 'exercise_type': 'multiple_choice',
             'prompt': 'En mi país se ___ mucho té.', 'options': ['bebe', 'beben', 'bebo'], 'correct_answer': 'bebe',
             'translation': 'В моей стране пьют много чая.', 'explanation': 'té — ед. → bebe.'},
            {'section': 'Упражнение 2. Безличные обороты', 'exercise_type': 'multiple_choice',
             'prompt': 'Aquí no se ___ entrar con perro.', 'options': ['puede', 'puedes', 'pueden'], 'correct_answer': 'puede',
             'translation': 'Сюда нельзя входить с собакой.', 'explanation': 'Безличный запрет.'},
            {'section': 'Упражнение 2. Безличные обороты', 'exercise_type': 'multiple_choice',
             'prompt': '¿Cómo se ___ al centro? (как добраться)', 'options': ['va', 'van', 'vas'], 'correct_answer': 'va',
             'translation': 'Как добраться до центра?', 'explanation': '¿Cómo se va a…?'},
            {'section': 'Упражнение 2. Безличные обороты', 'exercise_type': 'multiple_choice',
             'prompt': 'Se ___ bien en esta ciudad. (живётся)', 'options': ['vive', 'viven', 'vivo'], 'correct_answer': 'vive',
             'translation': 'В этом городе хорошо живётся.', 'explanation': 'Безличное: se vive bien.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Здесь говорят по-испански.»',
             'options': ['Aquí se habla español.', 'Aquí se hablan español.', 'Aquí hablan se español.'],
             'correct_answer': 'Aquí se habla español.', 'explanation': 'se habla.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Продаётся дом.»',
             'options': ['Se vende casa.', 'Se venden casa.', 'Vende se casa.'],
             'correct_answer': 'Se vende casa.', 'explanation': 'Ед. ч. → se vende.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Продаются билеты.»',
             'options': ['Se venden entradas.', 'Se vende entradas.', 'Venden se entradas.'],
             'correct_answer': 'Se venden entradas.', 'explanation': 'Мн. ч. → se venden.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «В Испании поздно ужинают.»',
             'options': ['En España se cena tarde.', 'En España se cenan tarde.', 'En España cenan se tarde.'],
             'correct_answer': 'En España se cena tarde.', 'explanation': 'Безличное ед. ч.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Здесь нельзя курить.»',
             'options': ['Aquí no se puede fumar.', 'Aquí no se pueden fumar.', 'Aquí no puede se fumar.'],
             'correct_answer': 'Aquí no se puede fumar.', 'explanation': 'no se puede + инф.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Как это пишется?»',
             'options': ['¿Cómo se escribe?', '¿Cómo se escriben?', '¿Cómo escribe se?'],
             'correct_answer': '¿Cómo se escribe?', 'explanation': 'se escribe.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Говорят, что здесь хорошо живётся.»',
             'options': ['Se dice que aquí se vive bien.', 'Se dicen que aquí se viven bien.', 'Dicen se que aquí vive se bien.'],
             'correct_answer': 'Se dice que aquí se vive bien.', 'explanation': 'se dice que + se vive.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Требуется официант.»',
             'options': ['Se necesita camarero.', 'Se necesitan camarero.', 'Necesita se camarero.'],
             'correct_answer': 'Se necesita camarero.', 'explanation': 'Ед. ч. → se necesita.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Можно заплатить картой?»',
             'options': ['¿Se puede pagar con tarjeta?', '¿Se pueden pagar con tarjeta?', '¿Puede se pagar con tarjeta?'],
             'correct_answer': '¿Se puede pagar con tarjeta?', 'explanation': 'se puede + инф.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Как добраться до вокзала?»',
             'options': ['¿Cómo se va a la estación?', '¿Cómo se van a la estación?', '¿Cómo va se a la estación?'],
             'correct_answer': '¿Cómo se va a la estación?', 'explanation': '¿Cómo se va a…?'},
        ],
    },
    {
        'n': 22, 'level': 'A2', 'title': 'Сложное прошедшее (Pretérito perfecto)',
        'theory': (
            'Pretérito perfecto — «прошлое, связанное с настоящим»: недавние события и '
            'жизненный опыт «до сих пор».\n\n'
            '1. Образование: haber (в настоящем) + participio (причастие).\n'
            '  haber: he, has, ha, hemos, habéis, han\n'
            '  participio: -ar → -ado (hablado), -er/-ir → -ido (comido, vivido)\n'
            '  He trabajado mucho hoy (я сегодня много работал). ¿Has comido? (ты поел?)\n\n'
            'Между haber и причастием ничего не вставляется; местоимения — перед haber: '
            'Lo he visto (я это видел). No he terminado (я не закончил).\n\n'
            '2. Когда употребляется:\n'
            '• период, который ещё длится: hoy (сегодня), esta semana (на этой неделе), '
            'este mes, este año, esta mañana: Esta semana hemos estudiado mucho;\n'
            '• жизненный опыт: alguna vez (когда-нибудь), nunca, ya (уже), todavía no (ещё нет): '
            '¿Has estado alguna vez en México? — No, nunca he estado (я никогда не был). '
            'Nunca he visto nada parecido (я никогда не видел ничего подобного);\n'
            '• результат к настоящему: ¿Cómo te ha ido el examen? (как прошёл твой экзамен?) '
            'Ha sido un día difícil (день выдался трудным).\n\n'
            '3. Счёт до 100: 11 once, 12 doce, 13 trece, 14 catorce, 15 quince, 16 dieciséis, '
            '20 veinte, 21 veintiuno, 30 treinta, 31 treinta y uno, 40 cuarenta, 50 cincuenta, '
            '60 sesenta, 70 setenta, 80 ochenta, 90 noventa, 100 cien. '
            'От 31 — через y: cuarenta y cinco (45), sesenta y ocho (68).\n\n'
            'Мини-диалог:\n'
            '— ¿Cómo te ha ido el examen? (Как прошёл экзамен?)\n'
            '— ¡Muy bien! He contestado todas las preguntas. (Отлично! Я ответил на все вопросы.)\n'
            '— ¡Cuánto me alegro! (Как я рад!)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Составьте perfecto: haber + participio', 'exercise_type': 'fill_blank',
             'prompt': 'Hoy yo ___ trabajado mucho.', 'options': ['he', 'has', 'ha'], 'correct_answer': 'he',
             'translation': 'Сегодня я много работал.', 'explanation': '1 л.: he trabajado.'},
            {'section': 'Упражнение 1. Составьте perfecto: haber + participio', 'exercise_type': 'fill_blank',
             'prompt': '¿Ya ___ comido (tú)?', 'options': ['has', 'he', 'ha'], 'correct_answer': 'has',
             'translation': 'Ты уже поел?', 'explanation': '2 л.: has comido.'},
            {'section': 'Упражнение 1. Составьте perfecto: haber + participio', 'exercise_type': 'fill_blank',
             'prompt': 'Esta semana nosotros ___ estudiado mucho.', 'options': ['hemos', 'habéis', 'han'], 'correct_answer': 'hemos',
             'translation': 'На этой неделе мы много занимались.', 'explanation': '1 л. мн.: hemos.'},
            {'section': 'Упражнение 1. Составьте perfecto: haber + participio', 'exercise_type': 'fill_blank',
             'prompt': 'Ella ___ vivido en tres países.', 'options': ['ha', 'he', 'han'], 'correct_answer': 'ha',
             'translation': 'Она жила в трёх странах.', 'explanation': '3 л.: ha vivido.'},
            {'section': 'Упражнение 1. Составьте perfecto: haber + participio', 'exercise_type': 'multiple_choice',
             'prompt': 'Participio от «hablar»:', 'options': ['hablado', 'hablido', 'hablando'], 'correct_answer': 'hablado',
             'translation': 'hablar — говорить', 'explanation': '-ar → -ado.'},
            {'section': 'Упражнение 1. Составьте perfecto: haber + participio', 'exercise_type': 'multiple_choice',
             'prompt': 'Participio от «vivir»:', 'options': ['vivido', 'vivado', 'viviendo'], 'correct_answer': 'vivido',
             'translation': 'vivir — жить', 'explanation': '-ir → -ido.'},
            {'section': 'Упражнение 1. Составьте perfecto: haber + participio', 'exercise_type': 'fill_blank',
             'prompt': 'Vosotros ___ llegado tarde.', 'options': ['habéis', 'hemos', 'han'], 'correct_answer': 'habéis',
             'translation': 'Вы пришли поздно.', 'explanation': '2 л. мн.: habéis.'},
            {'section': 'Упражнение 1. Составьте perfecto: haber + participio', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos no ___ terminado todavía.', 'options': ['han', 'ha', 'hemos'], 'correct_answer': 'han',
             'translation': 'Они ещё не закончили.', 'explanation': '3 л. мн.: han.'},
            {'section': 'Упражнение 1. Составьте perfecto: haber + participio', 'exercise_type': 'multiple_choice',
             'prompt': '«Я это видел» —', 'options': ['Lo he visto.', 'He lo visto.', 'Lo he veído.'], 'correct_answer': 'Lo he visto.',
             'translation': 'Я это видел.', 'explanation': 'Местоимение перед haber; ver → visto.'},
            {'section': 'Упражнение 1. Составьте perfecto: haber + participio', 'exercise_type': 'fill_blank',
             'prompt': 'Esta mañana yo me ___ levantado temprano.', 'options': ['he', 'has', 'ha'], 'correct_answer': 'he',
             'translation': 'Сегодня утром я встал рано.', 'explanation': 'me he levantado.'},
            # 2
            {'section': 'Упражнение 2. Опыт и маркеры. Числа до 100', 'exercise_type': 'multiple_choice',
             'prompt': '¿Has estado ___ vez en México?', 'options': ['alguna', 'nunca', 'ya'], 'correct_answer': 'alguna',
             'translation': 'Ты когда-нибудь был в Мексике?', 'explanation': 'alguna vez — когда-нибудь.'},
            {'section': 'Упражнение 2. Опыт и маркеры. Числа до 100', 'exercise_type': 'multiple_choice',
             'prompt': 'No, ___ he estado allí.', 'options': ['nunca', 'ya', 'siempre'], 'correct_answer': 'nunca',
             'translation': 'Нет, я никогда там не был.', 'explanation': 'nunca + perfecto.'},
            {'section': 'Упражнение 2. Опыт и маркеры. Числа до 100', 'exercise_type': 'multiple_choice',
             'prompt': '¿ ___ has terminado? — Sí, todo listo.', 'options': ['Ya', 'Todavía', 'Nunca'], 'correct_answer': 'Ya',
             'translation': 'Уже закончил? — Да, всё готово.', 'explanation': 'ya — уже.'},
            {'section': 'Упражнение 2. Опыт и маркеры. Числа до 100', 'exercise_type': 'multiple_choice',
             'prompt': '___ no he leído ese libro.', 'options': ['Todavía', 'Ya', 'Alguna'], 'correct_answer': 'Todavía',
             'translation': 'Я ещё не читал эту книгу.', 'explanation': 'todavía no — ещё нет.'},
            {'section': 'Упражнение 2. Опыт и маркеры. Числа до 100', 'exercise_type': 'multiple_choice',
             'prompt': 'Nunca he ___ nada parecido.', 'options': ['visto', 'veído', 'viendo'], 'correct_answer': 'visto',
             'translation': 'Я никогда не видел ничего подобного.', 'explanation': 'ver → visto.'},
            {'section': 'Упражнение 2. Опыт и маркеры. Числа до 100', 'exercise_type': 'multiple_choice',
             'prompt': '¿Cómo te ___ ido el examen?', 'options': ['ha', 'has', 'he'], 'correct_answer': 'ha',
             'translation': 'Как прошёл твой экзамен?', 'explanation': 'te ha ido — «тебе прошло».'},
            {'section': 'Упражнение 2. Опыт и маркеры. Числа до 100', 'exercise_type': 'multiple_choice',
             'prompt': '15 = ___', 'options': ['quince', 'cinco', 'cincuenta'], 'correct_answer': 'quince',
             'translation': '15 — quince', 'explanation': 'quince.'},
            {'section': 'Упражнение 2. Опыт и маркеры. Числа до 100', 'exercise_type': 'multiple_choice',
             'prompt': '45 = ___', 'options': ['cuarenta y cinco', 'cincuenta y cuatro', 'catorce y cinco'], 'correct_answer': 'cuarenta y cinco',
             'translation': '45 — сорок пять', 'explanation': 'cuarenta y cinco.'},
            {'section': 'Упражнение 2. Опыт и маркеры. Числа до 100', 'exercise_type': 'multiple_choice',
             'prompt': '90 = ___', 'options': ['noventa', 'ochenta', 'sesenta'], 'correct_answer': 'noventa',
             'translation': '90 — девяносто', 'explanation': 'noventa.'},
            {'section': 'Упражнение 2. Опыт и маркеры. Числа до 100', 'exercise_type': 'multiple_choice',
             'prompt': '100 = ___', 'options': ['cien', 'ciento uno', 'mil'], 'correct_answer': 'cien',
             'translation': '100 — сто', 'explanation': 'Ровно сто → cien.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Сегодня я много работал.»',
             'options': ['Hoy he trabajado mucho.', 'Hoy trabajé mucho ayer.', 'Hoy he trabajo mucho.'],
             'correct_answer': 'Hoy he trabajado mucho.', 'explanation': 'hoy → perfecto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Ты уже поел?»',
             'options': ['¿Ya has comido?', '¿Ya comes?', '¿Ya has comido tú has?'],
             'correct_answer': '¿Ya has comido?', 'explanation': 'ya + has comido.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я никогда не был в Испании.»',
             'options': ['Nunca he estado en España.', 'Nunca estuve en España mañana.', 'Nunca he sido en España.'],
             'correct_answer': 'Nunca he estado en España.', 'explanation': 'Опыт → nunca he estado.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я никогда не видел ничего подобного.»',
             'options': ['Nunca he visto nada parecido.', 'Nunca he veído nada parecido.', 'Nunca visto nada parecido he yo.'],
             'correct_answer': 'Nunca he visto nada parecido.', 'explanation': 'nunca + he visto + nada.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Как прошёл твой экзамен?»',
             'options': ['¿Cómo te ha ido el examen?', '¿Cómo te ha ida el examen?', '¿Cómo ha te ido el examen?'],
             'correct_answer': '¿Cómo te ha ido el examen?', 'explanation': 'te ha ido.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «На этой неделе мы много занимались.»',
             'options': ['Esta semana hemos estudiado mucho.', 'Esta semana estudiamos mucho ayer.', 'Esta semana habemos estudiado mucho.'],
             'correct_answer': 'Esta semana hemos estudiado mucho.', 'explanation': 'esta semana → perfecto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я ещё не закончил.»',
             'options': ['Todavía no he terminado.', 'Ya no he terminado.', 'Todavía no terminado he.'],
             'correct_answer': 'Todavía no he terminado.', 'explanation': 'todavía no + perfecto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я это уже видел.»',
             'options': ['Ya lo he visto.', 'Ya he lo visto.', 'Lo ya he visto.'],
             'correct_answer': 'Ya lo he visto.', 'explanation': 'ya + lo + he visto.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «День выдался трудным.»',
             'options': ['Ha sido un día difícil.', 'Ha estado un día difícil.', 'Fue ser un día difícil hoy.'],
             'correct_answer': 'Ha sido un día difícil.', 'explanation': 'ha sido — результат к настоящему.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мне 45 лет.» (числом-словом)',
             'options': ['Tengo cuarenta y cinco años.', 'Tengo cuarenta cinco años.', 'Soy cuarenta y cinco años.'],
             'correct_answer': 'Tengo cuarenta y cinco años.', 'explanation': 'cuarenta y cinco + tener.'},
        ],
    },
]
A2_FULL = A2_FULL + _C
