# -*- coding: utf-8 -*-
"""Upgraded A1 lessons 13–16 (full theory + 3 blocks of 10 items with translations).
Examples reuse the learner's personal vocab bank (tener ganas de, dale saludos, me encantaría...).
"""

A1_FULL_3 = [
    {
        'n': 13, 'level': 'A1', 'title': 'III спряжение (-ir). Mucho и muy. Tener',
        'theory': (
            '1. Третье спряжение — глаголы на -ir. Окончания настоящего времени почти совпадают '
            'с -er; отличаются только формы nosotros и vosotros:\n\n'
            '  vivir (жить): vivo, vives, vive, vivimos, vivís, viven\n\n'
            'Так же спрягаются: escribir (писать), abrir (открывать), recibir (получать), '
            'subir (подниматься), compartir (делить, делиться), decidir (решать). '
            'Сравните: comemos/coméis (-er), но vivimos/vivís (-ir).\n\n'
            '2. Важнейший глагол TENER (иметь) — неправильный:\n\n'
            '  tengo, tienes, tiene, tenemos, tenéis, tienen\n\n'
            'Tener образует множество устойчивых оборотов, где по-русски мы говорим «мне …»:\n'
            '• tener … años — возраст: Tengo veinte años (мне двадцать лет);\n'
            '• tener hambre / sed — быть голодным / хотеть пить: Tengo hambre;\n'
            '• tener frío / calor — мёрзнуть / изнывать от жары; tener sueño — хотеть спать;\n'
            '• tener ganas de + инфинитив — очень хотеть, «не терпится»: Tengo ganas de un café '
            '(очень хочу кофе), Tengo ganas de verte (не терпится тебя увидеть);\n'
            '• tener que + инфинитив — быть должным: Tengo que trabajar (мне надо работать).\n\n'
            '3. mucho и muy — оба переводятся «очень/много», но употребляются по-разному:\n'
            '• muy + прилагательное или наречие: muy bueno (очень хороший), muy bien (очень '
            'хорошо), muy tarde (очень поздно);\n'
            '• mucho + существительное — согласуется в роде и числе: mucho trabajo, mucha agua, '
            'muchos libros, muchas ganas;\n'
            '• глагол + mucho (не меняется): Trabajo mucho (я много работаю). Te lo agradezco '
            'mucho (я тебе очень благодарен).\n'
            'НЕЛЬЗЯ: *muy mucho, *muy trabajo.\n\n'
            '4. Дни недели (все мужского рода): lunes, martes, miércoles, jueves, viernes, '
            'sábado, domingo. «По понедельникам» — los lunes: Los viernes recibo a mis amigos '
            '(по пятницам я принимаю друзей).'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Поставьте глагол -ir или tener в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (vivir) en Madrid.', 'options': ['vivo', 'vives', 'vive'], 'correct_answer': 'vivo',
             'translation': 'Я живу в Мадриде.', 'explanation': '1 л.: vivo.'},
            {'section': 'Упражнение 1. Поставьте глагол -ir или tener в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ (vivir) cerca del centro.', 'options': ['vivimos', 'vivemos', 'viven'], 'correct_answer': 'vivimos',
             'translation': 'Мы живём недалеко от центра.', 'explanation': '-ir: vivimos (не *vivemos).'},
            {'section': 'Упражнение 1. Поставьте глагол -ir или tener в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Ella ___ (escribir) una carta.', 'options': ['escribo', 'escribe', 'escribes'], 'correct_answer': 'escribe',
             'translation': 'Она пишет письмо.', 'explanation': '3 л.: escribe.'},
            {'section': 'Упражнение 1. Поставьте глагол -ir или tener в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Vosotros ___ (vivir) en Sevilla.', 'options': ['vivís', 'vivéis', 'viven'], 'correct_answer': 'vivís',
             'translation': 'Вы живёте в Севилье.', 'explanation': '-ir, 2 л. мн.: vivís.'},
            {'section': 'Упражнение 1. Поставьте глагол -ir или tener в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (tener) dos hermanos.', 'options': ['tengo', 'tienes', 'tiene'], 'correct_answer': 'tengo',
             'translation': 'У меня два брата.', 'explanation': 'tener, 1 л.: tengo.'},
            {'section': 'Упражнение 1. Поставьте глагол -ir или tener в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': '¿Cuántos años ___ (tener, tú)?', 'options': ['tienes', 'tiene', 'tengo'], 'correct_answer': 'tienes',
             'translation': 'Сколько тебе лет?', 'explanation': '2 л.: tienes.'},
            {'section': 'Упражнение 1. Поставьте глагол -ir или tener в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ (abrir) la tienda a las diez.', 'options': ['abren', 'abrís', 'abre'], 'correct_answer': 'abren',
             'translation': 'Они открывают магазин в десять.', 'explanation': '3 л. мн.: abren.'},
            {'section': 'Упражнение 1. Поставьте глагол -ir или tener в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (recibir) muchos mensajes.', 'options': ['recibo', 'recibes', 'recibe'], 'correct_answer': 'recibo',
             'translation': 'Я получаю много сообщений.', 'explanation': '1 л.: recibo.'},
            {'section': 'Упражнение 1. Поставьте глагол -ir или tener в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ (tener) que trabajar hoy.', 'options': ['tenemos', 'tenéis', 'tienen'], 'correct_answer': 'tenemos',
             'translation': 'Нам сегодня надо работать.', 'explanation': 'tener que: tenemos que.'},
            {'section': 'Упражнение 1. Поставьте глагол -ir или tener в нужную форму', 'exercise_type': 'fill_blank',
             'prompt': '¿___ (compartir, vosotros) el piso?', 'options': ['Compartís', 'Comparten', 'Compartimos'], 'correct_answer': 'Compartís',
             'translation': 'Вы делите квартиру (снимаете вместе)?', 'explanation': '2 л. мн.: compartís.'},
            # 2
            {'section': 'Упражнение 2. Mucho или muy? Обороты с tener', 'exercise_type': 'multiple_choice',
             'prompt': 'El café está ___ caliente.', 'options': ['muy', 'mucho', 'mucha'], 'correct_answer': 'muy',
             'translation': 'Кофе очень горячий.', 'explanation': 'Перед прилагательным → muy.'},
            {'section': 'Упражнение 2. Mucho или muy? Обороты с tener', 'exercise_type': 'multiple_choice',
             'prompt': 'Tengo ___ trabajo esta semana.', 'options': ['muy', 'mucho', 'muchos'], 'correct_answer': 'mucho',
             'translation': 'У меня много работы на этой неделе.', 'explanation': 'trabajo — м. р. ед.: mucho.'},
            {'section': 'Упражнение 2. Mucho или muy? Обороты с tener', 'exercise_type': 'multiple_choice',
             'prompt': 'Bebo ___ agua.', 'options': ['mucho', 'mucha', 'muy'], 'correct_answer': 'mucha',
             'translation': 'Я пью много воды.', 'explanation': 'agua — ж. р.: mucha.'},
            {'section': 'Упражнение 2. Mucho или muy? Обороты с tener', 'exercise_type': 'multiple_choice',
             'prompt': 'Trabajas ___. (много)', 'options': ['muy', 'mucho', 'muchos'], 'correct_answer': 'mucho',
             'translation': 'Ты много работаешь.', 'explanation': 'После глагола → mucho.'},
            {'section': 'Упражнение 2. Mucho или muy? Обороты с tener', 'exercise_type': 'multiple_choice',
             'prompt': 'Hablas español ___ bien.', 'options': ['mucho', 'muy', 'mucha'], 'correct_answer': 'muy',
             'translation': 'Ты очень хорошо говоришь по-испански.', 'explanation': 'Перед наречием → muy.'},
            {'section': 'Упражнение 2. Mucho или muy? Обороты с tener', 'exercise_type': 'multiple_choice',
             'prompt': 'Tengo ___ de un café. (очень хочу)', 'options': ['ganas', 'gana', 'muchos'], 'correct_answer': 'ganas',
             'translation': 'Мне очень хочется кофе.', 'explanation': 'tener ganas de — хотеть.'},
            {'section': 'Упражнение 2. Mucho или muy? Обороты с tener', 'exercise_type': 'multiple_choice',
             'prompt': 'Tengo ___ : ¿comemos ya?', 'options': ['hambre', 'sed', 'sueño'], 'correct_answer': 'hambre',
             'translation': 'Я голоден: поедим уже?', 'explanation': 'tener hambre — быть голодным.'},
            {'section': 'Упражнение 2. Mucho или muy? Обороты с tener', 'exercise_type': 'multiple_choice',
             'prompt': 'Es tarde y tengo ___ .', 'options': ['sueño', 'calor', 'años'], 'correct_answer': 'sueño',
             'translation': 'Поздно, и я хочу спать.', 'explanation': 'tener sueño — хотеть спать.'},
            {'section': 'Упражнение 2. Mucho или muy? Обороты с tener', 'exercise_type': 'multiple_choice',
             'prompt': '___ que estudiar para el examen. (мне надо)', 'options': ['Tengo', 'Tengo ganas', 'Hay'], 'correct_answer': 'Tengo',
             'translation': 'Мне надо готовиться к экзамену.', 'explanation': 'tener que + инф. — долг.'},
            {'section': 'Упражнение 2. Mucho или muy? Обороты с tener', 'exercise_type': 'multiple_choice',
             'prompt': 'Tengo ___ ganas de verte.', 'options': ['muchas', 'muchos', 'muy'], 'correct_answer': 'muchas',
             'translation': 'Мне очень не терпится тебя увидеть.', 'explanation': 'ganas — ж. р. мн.: muchas ganas.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мне двадцать лет.»',
             'options': ['Tengo veinte años.', 'Soy veinte años.', 'Estoy veinte años.'],
             'correct_answer': 'Tengo veinte años.', 'explanation': 'Возраст → tener.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы живём в Испании.»',
             'options': ['Vivimos en España.', 'Vivemos en España.', 'Viven en España.'],
             'correct_answer': 'Vivimos en España.', 'explanation': '-ir: vivimos.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я хочу пить.»',
             'options': ['Tengo sed.', 'Tengo hambre.', 'Soy sed.'],
             'correct_answer': 'Tengo sed.', 'explanation': 'tener sed — хотеть пить.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мне не терпится тебя увидеть.»',
             'options': ['Tengo ganas de verte.', 'Tengo que verte.', 'Quiero mucho verte muy.'],
             'correct_answer': 'Tengo ganas de verte.', 'explanation': 'tener ganas de + инф.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мне надо работать.»',
             'options': ['Tengo que trabajar.', 'Tengo ganas de trabajar.', 'Hay que trabajo.'],
             'correct_answer': 'Tengo que trabajar.', 'explanation': 'tener que — долженствование.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Она пишет много писем.»',
             'options': ['Escribe muchas cartas.', 'Escribe muy cartas.', 'Escribe mucho cartas.'],
             'correct_answer': 'Escribe muchas cartas.', 'explanation': 'cartas — ж. р. мн.: muchas.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Суп очень вкусный, спасибо!» (очень хороший)',
             'options': ['La sopa está muy buena, ¡gracias!', 'La sopa está mucho buena, ¡gracias!', 'La sopa es muy mucho buena.'],
             'correct_answer': 'La sopa está muy buena, ¡gracias!', 'explanation': 'muy + прилагательное.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я тебе очень благодарен.» (досл. «я тебе это очень ценю»)',
             'options': ['Te lo agradezco mucho.', 'Te lo agradezco muy.', 'Te agradezco muy mucho.'],
             'correct_answer': 'Te lo agradezco mucho.', 'explanation': 'Глагол + mucho.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «По пятницам мы получаем гостей.» (принимаем друзей)',
             'options': ['Los viernes recibimos a los amigos.', 'El viernes recibimos amigos los.', 'Los viernes reciben a los amigos nosotros.'],
             'correct_answer': 'Los viernes recibimos a los amigos.', 'explanation': 'los viernes = по пятницам; личное a.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Сегодня очень жарко, и я изнываю от жары.»',
             'options': ['Hace mucho calor y tengo calor.', 'Está muy calor y soy calor.', 'Hace muy calor y tengo mucho calor yo.'],
             'correct_answer': 'Hace mucho calor y tengo calor.', 'explanation': 'hace calor (погода) + tener calor (о себе).'},
        ],
    },
    {
        'n': 14, 'level': 'A1', 'title': 'Повелительное наклонение (Imperativo)',
        'theory': (
            'Императив выражает просьбы, приказы и советы: «сделай!», «послушай!».\n\n'
            '1. Утвердительная форма для tú (ты) совпадает с формой 3 лица ед. числа настоящего '
            'времени:\n'
            '• hablar → ¡Habla! (говори!), comer → ¡Come!, vivir → ¡Vive!\n'
            '• escuchar → ¡Escucha! (послушай!), mirar → ¡Mira! (смотри!), '
            'perdonar → ¡Perdona! (извини!)\n'
            'Чередования сохраняются: cerrar → ¡Cierra la puerta! (закрой дверь!), '
            'pedir → ¡Pide un taxi!\n\n'
            '2. Восемь неправильных форм tú (выучить наизусть):\n'
            '  hacer → haz, poner → pon, salir → sal, tener → ten, venir → ven, '
            'decir → di, ir → ve, ser → sé.\n'
            '  ¡Haz la tarea! (сделай задание!) ¡Ven aquí! (иди сюда!) ¡Di la verdad! (скажи правду!)\n\n'
            '3. Вежливая форма usted берётся из subjuntivo (пока просто запомним частые):\n'
            '  hablar → hable, comer → coma, hacer → haga, venir → venga.\n'
            '  ¡Pase, por favor! (проходите, пожалуйста!) ¡Perdone! (извините!)\n'
            'Форма vosotros: инфинитив с -d вместо -r: ¡Hablad! ¡Venid!\n\n'
            '4. Местоимения присоединяются к утвердительному императиву СЗАДИ, часто с '
            'появлением ударения:\n'
            '• ¡Dime! (скажи мне!) ¡Dame el libro! (дай мне книгу!)\n'
            '• ¡Dale saludos a tu madre! (передавай привет маме!)\n'
            '• возвратные: ¡Levántate! (вставай!) ¡Siéntate! (садись!)\n\n'
            '5. Разговорные «командочки» из живой речи: ¡Oye! (слушай!), ¡Mira! (смотри/гляди!), '
            '¡Venga! (давай!), ¡Dale! (давай, вперёд!), ¡Cuídate! (береги себя!). '
            'Глагол querer помогает просить вежливо: ¿Quieres abrir la ventana? '
            '(откроешь окно?) Quiero un café, por favor.'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Образуйте императив (tú) от правильных глаголов', 'exercise_type': 'fill_blank',
             'prompt': '¡___ (hablar) más despacio!', 'options': ['Habla', 'Hable', 'Hablas'], 'correct_answer': 'Habla',
             'translation': 'Говори медленнее!', 'explanation': 'tú: habla.'},
            {'section': 'Упражнение 1. Образуйте императив (tú) от правильных глаголов', 'exercise_type': 'fill_blank',
             'prompt': '¡___ (comer) la sopa!', 'options': ['Come', 'Coma', 'Comes'], 'correct_answer': 'Come',
             'translation': 'Ешь суп!', 'explanation': 'tú: come.'},
            {'section': 'Упражнение 1. Образуйте императив (tú) от правильных глаголов', 'exercise_type': 'fill_blank',
             'prompt': '¡___ (escuchar) esta canción!', 'options': ['Escucha', 'Escuche', 'Escuchas'], 'correct_answer': 'Escucha',
             'translation': 'Послушай эту песню!', 'explanation': 'tú: escucha.'},
            {'section': 'Упражнение 1. Образуйте императив (tú) от правильных глаголов', 'exercise_type': 'fill_blank',
             'prompt': '¡___ (mirar) qué bonito!', 'options': ['Mira', 'Mire', 'Miras'], 'correct_answer': 'Mira',
             'translation': 'Смотри, как красиво!', 'explanation': 'tú: mira.'},
            {'section': 'Упражнение 1. Образуйте императив (tú) от правильных глаголов', 'exercise_type': 'fill_blank',
             'prompt': '¡___ (cerrar) la puerta!', 'options': ['Cierra', 'Cerra', 'Cierre'], 'correct_answer': 'Cierra',
             'translation': 'Закрой дверь!', 'explanation': 'e→ie сохраняется: cierra.'},
            {'section': 'Упражнение 1. Образуйте императив (tú) от правильных глаголов', 'exercise_type': 'fill_blank',
             'prompt': '¡___ (abrir) la ventana!', 'options': ['Abre', 'Abra', 'Abres'], 'correct_answer': 'Abre',
             'translation': 'Открой окно!', 'explanation': 'tú: abre.'},
            {'section': 'Упражнение 1. Образуйте императив (tú) от правильных глаголов', 'exercise_type': 'fill_blank',
             'prompt': '¡___ (pedir) un taxi!', 'options': ['Pide', 'Pida', 'Pedi'], 'correct_answer': 'Pide',
             'translation': 'Закажи такси!', 'explanation': 'e→i: pide.'},
            {'section': 'Упражнение 1. Образуйте императив (tú) от правильных глаголов', 'exercise_type': 'fill_blank',
             'prompt': '¡___ (perdonar), llego tarde!', 'options': ['Perdona', 'Perdone', 'Perdonas'], 'correct_answer': 'Perdona',
             'translation': 'Извини, я опаздываю!', 'explanation': 'tú: perdona.'},
            {'section': 'Упражнение 1. Образуйте императив (tú) от правильных глаголов', 'exercise_type': 'fill_blank',
             'prompt': '¡___ (comprar) pan, por favor!', 'options': ['Compra', 'Compre', 'Compras'], 'correct_answer': 'Compra',
             'translation': 'Купи хлеб, пожалуйста!', 'explanation': 'tú: compra.'},
            {'section': 'Упражнение 1. Образуйте императив (tú) от правильных глаголов', 'exercise_type': 'fill_blank',
             'prompt': '¡___ (estudiar) para el examen!', 'options': ['Estudia', 'Estudie', 'Estudias'], 'correct_answer': 'Estudia',
             'translation': 'Готовься к экзамену!', 'explanation': 'tú: estudia.'},
            # 2
            {'section': 'Упражнение 2. Неправильные формы и вежливое usted', 'exercise_type': 'multiple_choice',
             'prompt': '¡___ la tarea! (hacer, tú)', 'options': ['Haz', 'Hace', 'Haga'], 'correct_answer': 'Haz',
             'translation': 'Сделай задание!', 'explanation': 'hacer → haz.'},
            {'section': 'Упражнение 2. Неправильные формы и вежливое usted', 'exercise_type': 'multiple_choice',
             'prompt': '¡___ aquí! (venir, tú)', 'options': ['Ven', 'Viene', 'Venga'], 'correct_answer': 'Ven',
             'translation': 'Иди сюда!', 'explanation': 'venir → ven.'},
            {'section': 'Упражнение 2. Неправильные формы и вежливое usted', 'exercise_type': 'multiple_choice',
             'prompt': '¡___ la verdad! (decir, tú)', 'options': ['Di', 'Dice', 'Diga'], 'correct_answer': 'Di',
             'translation': 'Скажи правду!', 'explanation': 'decir → di.'},
            {'section': 'Упражнение 2. Неправильные формы и вежливое usted', 'exercise_type': 'multiple_choice',
             'prompt': '¡___ la mesa! (poner, tú)', 'options': ['Pon', 'Pone', 'Ponga'], 'correct_answer': 'Pon',
             'translation': 'Накрой на стол!', 'explanation': 'poner → pon.'},
            {'section': 'Упражнение 2. Неправильные формы и вежливое usted', 'exercise_type': 'multiple_choice',
             'prompt': '¡___ de casa ya! (salir, tú)', 'options': ['Sal', 'Sale', 'Salga'], 'correct_answer': 'Sal',
             'translation': 'Выходи уже из дома!', 'explanation': 'salir → sal.'},
            {'section': 'Упражнение 2. Неправильные формы и вежливое usted', 'exercise_type': 'multiple_choice',
             'prompt': '¡___ paciencia! (tener, tú)', 'options': ['Ten', 'Tiene', 'Tenga'], 'correct_answer': 'Ten',
             'translation': 'Имей терпение!', 'explanation': 'tener → ten.'},
            {'section': 'Упражнение 2. Неправильные формы и вежливое usted', 'exercise_type': 'multiple_choice',
             'prompt': '¡___ al supermercado! (ir, tú)', 'options': ['Ve', 'Va', 'Vaya'], 'correct_answer': 'Ve',
             'translation': 'Сходи в супермаркет!', 'explanation': 'ir → ve.'},
            {'section': 'Упражнение 2. Неправильные формы и вежливое usted', 'exercise_type': 'multiple_choice',
             'prompt': '¡___ , por favor! (pasar, usted — проходите)', 'options': ['Pase', 'Pasa', 'Pasad'], 'correct_answer': 'Pase',
             'translation': 'Проходите, пожалуйста!', 'explanation': 'usted: pase.'},
            {'section': 'Упражнение 2. Неправильные формы и вежливое usted', 'exercise_type': 'multiple_choice',
             'prompt': '¡___ ! ¿Es este el autobús al centro? (perdonar, usted)', 'options': ['Perdone', 'Perdona', 'Perdonad'], 'correct_answer': 'Perdone',
             'translation': 'Извините! Это автобус в центр?', 'explanation': 'usted: perdone.'},
            {'section': 'Упражнение 2. Неправильные формы и вежливое usted', 'exercise_type': 'multiple_choice',
             'prompt': '¡___ bueno, hijo! (ser, tú)', 'options': ['Sé', 'Es', 'Sea'], 'correct_answer': 'Sé',
             'translation': 'Будь хорошим, сынок!', 'explanation': 'ser → sé.'},
            # 3
            {'section': 'Упражнение 3. Императив с местоимениями. Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Скажи мне!»',
             'options': ['¡Dime!', '¡Me di!', '¡Dime tú a mí me!'],
             'correct_answer': '¡Dime!', 'explanation': 'di + me = dime.'},
            {'section': 'Упражнение 3. Императив с местоимениями. Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Дай мне книгу.»',
             'options': ['Dame el libro.', 'Me da el libro.', 'Da me el libro.'],
             'correct_answer': 'Dame el libro.', 'explanation': 'da + me = dame.'},
            {'section': 'Упражнение 3. Императив с местоимениями. Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Передавай привет маме!»',
             'options': ['¡Dale saludos a tu madre!', '¡Da saludos le a tu madre!', '¡Le da saludos a tu madre!'],
             'correct_answer': '¡Dale saludos a tu madre!', 'explanation': 'da + le = dale (разговорная формула).'},
            {'section': 'Упражнение 3. Императив с местоимениями. Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Вставай! Уже поздно.»',
             'options': ['¡Levántate! Ya es tarde.', '¡Te levanta! Ya es tarde.', '¡Levanta te! Ya es tarde.'],
             'correct_answer': '¡Levántate! Ya es tarde.', 'explanation': 'levanta + te = levántate (с ударением).'},
            {'section': 'Упражнение 3. Императив с местоимениями. Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Садись, пожалуйста.»',
             'options': ['Siéntate, por favor.', 'Te sienta, por favor.', 'Sienta te, por favor.'],
             'correct_answer': 'Siéntate, por favor.', 'explanation': 'sienta + te = siéntate.'},
            {'section': 'Упражнение 3. Императив с местоимениями. Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Слушай! У меня есть идея.»',
             'options': ['¡Oye! Tengo una idea.', '¡Oír! Tengo una idea.', '¡Oyes! Tengo una idea.'],
             'correct_answer': '¡Oye! Tengo una idea.', 'explanation': 'Разговорное ¡oye! — «слушай!».'},
            {'section': 'Упражнение 3. Императив с местоимениями. Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Береги себя!»',
             'options': ['¡Cuídate!', '¡Te cuida!', '¡Cuida te tú!'],
             'correct_answer': '¡Cuídate!', 'explanation': 'cuida + te = cuídate.'},
            {'section': 'Упражнение 3. Императив с местоимениями. Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Сделай мне одолжение: купи хлеб.»',
             'options': ['Hazme un favor: compra pan.', 'Me haz un favor: compra pan.', 'Haz me un favor: compras pan.'],
             'correct_answer': 'Hazme un favor: compra pan.', 'explanation': 'haz + me = hazme.'},
            {'section': 'Упражнение 3. Императив с местоимениями. Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Иди сюда и посмотри на это!»',
             'options': ['¡Ven aquí y mira esto!', '¡Viene aquí y mira esto!', '¡Ven aquí y miras esto!'],
             'correct_answer': '¡Ven aquí y mira esto!', 'explanation': 'ven + mira (оба tú).'},
            {'section': 'Упражнение 3. Императив с местоимениями. Переведите', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Откроешь окно?» (вежливо через querer)',
             'options': ['¿Quieres abrir la ventana?', '¿Quieres abre la ventana?', '¿Abre quieres la ventana?'],
             'correct_answer': '¿Quieres abrir la ventana?', 'explanation': 'querer + инфинитив — мягкая просьба.'},
        ],
    },
]

_B3 = [
    {
        'n': 15, 'level': 'A1', 'title': 'Притяжательные прилагательные',
        'theory': (
            '1. Притяжательные прилагательные ставятся ПЕРЕД существительным и заменяют артикль '
            '(вместе они не употребляются):\n\n'
            '  mi — мой/моя; tu — твой/твоя; su — его/её/Ваш; \n'
            '  nuestro/nuestra — наш/наша; vuestro/vuestra — ваш/ваша; su — их/Ваш (ustedes)\n\n'
            '2. Согласование. Все формы согласуются в ЧИСЛЕ (mi → mis, tu → tus, su → sus), '
            'а nuestro и vuestro — ещё и в РОДЕ:\n'
            '• mi casa — mis casas (мой дом — мои дома);\n'
            '• tu amigo — tus amigos;\n'
            '• nuestro coche — nuestra familia — nuestros hijos — nuestras hijas;\n'
            '• vuestro piso — vuestras ideas.\n'
            'Важно: род согласуется с ПРЕДМЕТОМ, а не с владельцем: su libro (его/её книга).\n\n'
            '3. Su многозначно: его, её, Ваш (usted), их, Ваш (ustedes). Если контекста мало, '
            'уточняют оборотом de + местоимение: el coche de él (его машина), la casa de ella, '
            'el libro de usted.\n\n'
            '4. Помните из урока о возвратных глаголах: с частями тела и одеждой испанский '
            'предпочитает артикль, а не притяжательное: Me lavo las manos (мою руки), '
            'Se pone el abrigo (надевает пальто).\n\n'
            '5. Три полезных неправильных глагола (неправильна форма yo, у venir ещё e→ie):\n'
            '• salir (выходить, уходить): salgo, sales, sale, salimos, salís, salen — '
            'Salgo de casa a las ocho (выхожу из дома в восемь);\n'
            '• oír (слышать): oigo, oyes, oye, oímos, oís, oyen — ¿Me oyes? (ты меня слышишь?);\n'
            '• venir (приходить): vengo, vienes, viene, venimos, venís, vienen — '
            '¿Vienes a mi fiesta? (придёшь на мой праздник?)\n\n'
            'Мини-диалог:\n'
            '— ¡Oye! ¿Vienes a nuestra cena el sábado? (Слушай! Придёшь на наш ужин в субботу?)\n'
            '— ¡Me encantaría! ¿Viene también tu hermana? (С удовольствием! Твоя сестра тоже придёт?)\n'
            '— Sí, y trae a su novio. (Да, и приведёт своего парня.)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Выберите притяжательное', 'exercise_type': 'fill_blank',
             'prompt': '___ casa es grande. (моя)', 'options': ['Mi', 'Mis', 'Mío'], 'correct_answer': 'Mi',
             'translation': 'Мой дом большой.', 'explanation': 'Ед. ч.: mi.'},
            {'section': 'Упражнение 1. Выберите притяжательное', 'exercise_type': 'fill_blank',
             'prompt': '___ amigos son simpáticos. (твои)', 'options': ['Tu', 'Tus', 'Su'], 'correct_answer': 'Tus',
             'translation': 'Твои друзья симпатичные.', 'explanation': 'Мн. ч.: tus.'},
            {'section': 'Упражнение 1. Выберите притяжательное', 'exercise_type': 'fill_blank',
             'prompt': '___ familia vive en Cádiz. (наша)', 'options': ['Nuestro', 'Nuestra', 'Nuestras'], 'correct_answer': 'Nuestra',
             'translation': 'Наша семья живёт в Кадисе.', 'explanation': 'familia — ж. р.: nuestra.'},
            {'section': 'Упражнение 1. Выберите притяжательное', 'exercise_type': 'fill_blank',
             'prompt': '___ hijos estudian aquí. (наши)', 'options': ['Nuestros', 'Nuestras', 'Nuestro'], 'correct_answer': 'Nuestros',
             'translation': 'Наши дети учатся здесь.', 'explanation': 'hijos — м. р. мн.: nuestros.'},
            {'section': 'Упражнение 1. Выберите притяжательное', 'exercise_type': 'fill_blank',
             'prompt': '¿Es ___ libro, María? (его — Хуана)', 'options': ['su', 'sus', 'tu'], 'correct_answer': 'su',
             'translation': 'Это его книга, Мария?', 'explanation': 'его → su.'},
            {'section': 'Упражнение 1. Выберите притяжательное', 'exercise_type': 'fill_blank',
             'prompt': '___ ideas son buenas. (ваши, vosotros)', 'options': ['Vuestras', 'Vuestros', 'Vuestra'], 'correct_answer': 'Vuestras',
             'translation': 'Ваши идеи хорошие.', 'explanation': 'ideas — ж. р. мн.: vuestras.'},
            {'section': 'Упражнение 1. Выберите притяжательное', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos venden ___ coche. (их)', 'options': ['su', 'sus', 'suyo'], 'correct_answer': 'su',
             'translation': 'Они продают свою машину.', 'explanation': 'Один предмет: su coche.'},
            {'section': 'Упражнение 1. Выберите притяжательное', 'exercise_type': 'fill_blank',
             'prompt': '___ hermana canta muy bien. (моя)', 'options': ['Mi', 'Mis', 'Mía'], 'correct_answer': 'Mi',
             'translation': 'Моя сестра очень хорошо поёт.', 'explanation': 'Перед сущ.: mi.'},
            {'section': 'Упражнение 1. Выберите притяжательное', 'exercise_type': 'fill_blank',
             'prompt': '¿Dónde están ___ llaves? (мои)', 'options': ['mi', 'mis', 'me'], 'correct_answer': 'mis',
             'translation': 'Где мои ключи?', 'explanation': 'llaves — мн. ч.: mis.'},
            {'section': 'Упражнение 1. Выберите притяжательное', 'exercise_type': 'fill_blank',
             'prompt': 'Me lavo ___ manos. (артикль, не притяжательное!)', 'options': ['las', 'mis', 'unas'], 'correct_answer': 'las',
             'translation': 'Я мою руки.', 'explanation': 'С частями тела — артикль: las manos.'},
            # 2
            {'section': 'Упражнение 2. Salir, oír, venir', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (salir) de casa a las ocho.', 'options': ['salgo', 'salo', 'sale'], 'correct_answer': 'salgo',
             'translation': 'Я выхожу из дома в восемь.', 'explanation': 'salir: salgo.'},
            {'section': 'Упражнение 2. Salir, oír, venir', 'exercise_type': 'fill_blank',
             'prompt': '¿Me ___ (oír, tú) bien?', 'options': ['oyes', 'oís', 'oigo'], 'correct_answer': 'oyes',
             'translation': 'Ты меня хорошо слышишь?', 'explanation': 'oír: oyes.'},
            {'section': 'Упражнение 2. Salir, oír, venir', 'exercise_type': 'fill_blank',
             'prompt': 'Yo no ___ (oír) nada.', 'options': ['oigo', 'oyo', 'oye'], 'correct_answer': 'oigo',
             'translation': 'Я ничего не слышу.', 'explanation': 'oír: oigo.'},
            {'section': 'Упражнение 2. Salir, oír, venir', 'exercise_type': 'fill_blank',
             'prompt': '¿___ (venir, tú) a mi fiesta?', 'options': ['Vienes', 'Venes', 'Vengo'], 'correct_answer': 'Vienes',
             'translation': 'Придёшь на мой праздник?', 'explanation': 'venir: vienes (e→ie).'},
            {'section': 'Упражнение 2. Salir, oír, venir', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (venir) del trabajo ahora.', 'options': ['vengo', 'vieno', 'viene'], 'correct_answer': 'vengo',
             'translation': 'Я сейчас иду с работы.', 'explanation': 'venir: vengo.'},
            {'section': 'Упражнение 2. Salir, oír, venir', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ (venir) en coche.', 'options': ['venimos', 'vienimos', 'vienen'], 'correct_answer': 'venimos',
             'translation': 'Мы приезжаем на машине.', 'explanation': 'nosotros без чередования: venimos.'},
            {'section': 'Упражнение 2. Salir, oír, venir', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ (salir) los sábados.', 'options': ['salen', 'salgan', 'salís'], 'correct_answer': 'salen',
             'translation': 'Они гуляют (выходят) по субботам.', 'explanation': '3 л. мн.: salen.'},
            {'section': 'Упражнение 2. Salir, oír, venir', 'exercise_type': 'fill_blank',
             'prompt': '¿___ (oír, vosotros) la música?', 'options': ['Oís', 'Oyes', 'Oyen'], 'correct_answer': 'Oís',
             'translation': 'Вы слышите музыку?', 'explanation': 'vosotros: oís.'},
            {'section': 'Упражнение 2. Salir, oír, venir', 'exercise_type': 'fill_blank',
             'prompt': 'Mi tren ___ (salir) a las nueve.', 'options': ['sale', 'salgo', 'salen'], 'correct_answer': 'sale',
             'translation': 'Мой поезд отходит в девять.', 'explanation': '3 л.: sale.'},
            {'section': 'Упражнение 2. Salir, oír, venir', 'exercise_type': 'fill_blank',
             'prompt': 'Ella ___ (venir) con su novio.', 'options': ['viene', 'vene', 'vengo'], 'correct_answer': 'viene',
             'translation': 'Она придёт со своим парнем.', 'explanation': 'venir: viene.'},
            # 3
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это мой дом, а это твоя машина.»',
             'options': ['Esta es mi casa y este es tu coche.', 'Esta es la mi casa y este es el tu coche.', 'Esta es mía casa y este es tuyo coche.'],
             'correct_answer': 'Esta es mi casa y este es tu coche.', 'explanation': 'Притяжательное без артикля.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Наша семья большая.»',
             'options': ['Nuestra familia es grande.', 'Nuestro familia es grande.', 'La nuestra familia está grande.'],
             'correct_answer': 'Nuestra familia es grande.', 'explanation': 'familia — ж. р.: nuestra.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Где твои ключи?»',
             'options': ['¿Dónde están tus llaves?', '¿Dónde está tus llaves?', '¿Dónde están tuyas llaves?'],
             'correct_answer': '¿Dónde están tus llaves?', 'explanation': 'Мн. ч.: tus + están.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Его сестра приходит с работы в семь.»',
             'options': ['Su hermana viene del trabajo a las siete.', 'Su hermana vene del trabajo a las siete.', 'Sus hermana viene de trabajo a las siete.'],
             'correct_answer': 'Su hermana viene del trabajo a las siete.', 'explanation': 'su + viene + del.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я выхожу из дома в восемь.»',
             'options': ['Salgo de casa a las ocho.', 'Salo de casa a las ocho.', 'Salgo del casa a las ocho.'],
             'correct_answer': 'Salgo de casa a las ocho.', 'explanation': 'salgo; de casa без артикля.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Ты меня слышишь? — Я тебя не слышу.»',
             'options': ['¿Me oyes? — No te oigo.', '¿Me oís? — No te oyo.', '¿Me oyes? — No te oye.'],
             'correct_answer': '¿Me oyes? — No te oigo.', 'explanation': 'oyes / oigo.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Придёшь на наш ужин? — С удовольствием!»',
             'options': ['¿Vienes a nuestra cena? — ¡Me encantaría!', '¿Venes a nuestra cena? — ¡Me encanta mucho!', '¿Vienes a nuestro cena? — ¡Me encantaría!'],
             'correct_answer': '¿Vienes a nuestra cena? — ¡Me encantaría!', 'explanation': 'vienes; cena — ж. р.; me encantaría — с удовольствием.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Их дети учат испанский.»',
             'options': ['Sus hijos aprenden español.', 'Su hijos aprenden español.', 'Suyos hijos aprenden español.'],
             'correct_answer': 'Sus hijos aprenden español.', 'explanation': 'hijos — мн. ч.: sus.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Это машина его (именно его, уточнённо).»',
             'options': ['Es el coche de él.', 'Es su de él coche.', 'Es el su coche.'],
             'correct_answer': 'Es el coche de él.', 'explanation': 'Уточнение su → de él.'},
            {'section': 'Упражнение 3. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Она надевает пальто.» (одежда — с артиклем)',
             'options': ['Se pone el abrigo.', 'Se pone su abrigo siempre suyo.', 'Pone el abrigo.'],
             'correct_answer': 'Se pone el abrigo.', 'explanation': 'ponerse + el (одежда с артиклем).'},
        ],
    },
    {
        'n': 16, 'level': 'A1', 'title': 'Ir + a + инфинитив (ближайшее будущее)',
        'theory': (
            '1. Глагол IR (идти, ехать) — один из самых неправильных и самых нужных:\n\n'
            '  voy, vas, va, vamos, vais, van\n\n'
            'С направлением употребляется предлог a: Voy al trabajo (еду на работу), '
            'Vamos a la playa (едем на пляж). «Как добираешься?» — en: en coche, en metro, '
            'en autobús; пешком — a pie.\n\n'
            '2. Конструкция IR A + ИНФИНИТИВ — ближайшее будущее, планы и намерения '
            '(аналог английского going to):\n'
            '• Voy a estudiar esta noche (сегодня вечером я буду заниматься);\n'
            '• ¿Qué vas a hacer mañana? (что ты будешь делать завтра?);\n'
            '• Vamos a viajar este verano (этим летом мы поедем путешествовать);\n'
            '• Van a comprar una casa (они собираются купить дом).\n'
            'Отрицание: No voy a salir hoy (сегодня я не пойду гулять).\n\n'
            '3. Vamos a + инфинитив также значит «давай(те)…»: ¡Vamos a comer! (давайте есть!), '
            '¡Vamos a ver! (посмотрим!).\n\n'
            '4. Слова-маркеры будущего: hoy (сегодня), esta noche (сегодня вечером), mañana '
            '(завтра), pasado mañana (послезавтра), este fin de semana (в эти выходные), '
            'la semana que viene (на следующей неделе), el año que viene (в следующем году).\n\n'
            '5. Ещё два глагола с неправильным yo: poner (класть, ставить) → pongo, pones, '
            'pone…; traer (приносить) → traigo, traes, trae… — Traigo el postre (я принесу десерт).\n\n'
            'Мини-диалог о планах:\n'
            '— ¿Qué vas a hacer el sábado? (Что будешь делать в субботу?)\n'
            '— Voy a ir al cine con mi hermana. ¿Vienes? (Пойду в кино с сестрой. Пойдёшь?)\n'
            '— ¡Me encantaría poder ir, pero tengo que trabajar! (Я бы с удовольствием, но мне '
            'надо работать!)\n'
            '— ¡Qué pena! Bueno, ¡que te vaya bien! (Как жаль! Ну, удачи тебе!)'
        ),
        'exercises': [
            {'section': 'Упражнение 1. Формы глагола ir', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ al trabajo en metro.', 'options': ['voy', 'vas', 'va'], 'correct_answer': 'voy',
             'translation': 'Я езжу на работу на метро.', 'explanation': '1 л.: voy.'},
            {'section': 'Упражнение 1. Формы глагола ir', 'exercise_type': 'fill_blank',
             'prompt': '¿Adónde ___ (tú)?', 'options': ['vas', 'voy', 'va'], 'correct_answer': 'vas',
             'translation': 'Куда ты идёшь?', 'explanation': '2 л.: vas.'},
            {'section': 'Упражнение 1. Формы глагола ir', 'exercise_type': 'fill_blank',
             'prompt': 'Nosotros ___ a la playa.', 'options': ['vamos', 'vais', 'van'], 'correct_answer': 'vamos',
             'translation': 'Мы едем на пляж.', 'explanation': '1 л. мн.: vamos.'},
            {'section': 'Упражнение 1. Формы глагола ir', 'exercise_type': 'fill_blank',
             'prompt': 'Ellos ___ al cine los viernes.', 'options': ['van', 'vais', 'va'], 'correct_answer': 'van',
             'translation': 'Они ходят в кино по пятницам.', 'explanation': '3 л. мн.: van.'},
            {'section': 'Упражнение 1. Формы глагола ir', 'exercise_type': 'fill_blank',
             'prompt': 'María ___ a la escuela a pie.', 'options': ['va', 'vas', 'van'], 'correct_answer': 'va',
             'translation': 'Мария ходит в школу пешком.', 'explanation': '3 л.: va; a pie.'},
            {'section': 'Упражнение 1. Формы глагола ir', 'exercise_type': 'fill_blank',
             'prompt': '¿___ (vosotros) en autobús?', 'options': ['Vais', 'Van', 'Vamos'], 'correct_answer': 'Vais',
             'translation': 'Вы едете на автобусе?', 'explanation': '2 л. мн.: vais.'},
            {'section': 'Упражнение 1. Формы глагола ir', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (poner) la mesa.', 'options': ['pongo', 'pono', 'pone'], 'correct_answer': 'pongo',
             'translation': 'Я накрываю на стол.', 'explanation': 'poner: pongo.'},
            {'section': 'Упражнение 1. Формы глагола ir', 'exercise_type': 'fill_blank',
             'prompt': 'Yo ___ (traer) el postre.', 'options': ['traigo', 'trao', 'trae'], 'correct_answer': 'traigo',
             'translation': 'Я принесу десерт.', 'explanation': 'traer: traigo.'},
            {'section': 'Упражнение 1. Формы глагола ir', 'exercise_type': 'fill_blank',
             'prompt': 'Vamos ___ centro. (a + артикль)', 'options': ['al', 'a la', 'del'], 'correct_answer': 'al',
             'translation': 'Мы едем в центр.', 'explanation': 'a + el = al.'},
            {'section': 'Упражнение 1. Формы глагола ir', 'exercise_type': 'fill_blank',
             'prompt': 'Ella trae ___ su novio a la fiesta. (личное a)', 'options': ['a', 'de', '— (без предлога)'], 'correct_answer': 'a',
             'translation': 'Она приводит своего парня на праздник.', 'explanation': 'Человек → личное a.'},
            # 2
            {'section': 'Упражнение 2. Постройте ближайшее будущее (ir a + инфинитив)', 'exercise_type': 'multiple_choice',
             'prompt': 'Esta noche yo ___ estudiar.', 'options': ['voy a', 'voy', 'va a'], 'correct_answer': 'voy a',
             'translation': 'Сегодня вечером я буду заниматься.', 'explanation': 'voy a + инфинитив.'},
            {'section': 'Упражнение 2. Постройте ближайшее будущее (ir a + инфинитив)', 'exercise_type': 'multiple_choice',
             'prompt': '¿Qué ___ hacer mañana? (tú)', 'options': ['vas a', 'vas', 'va a'], 'correct_answer': 'vas a',
             'translation': 'Что ты будешь делать завтра?', 'explanation': 'vas a hacer.'},
            {'section': 'Упражнение 2. Постройте ближайшее будущее (ir a + инфинитив)', 'exercise_type': 'multiple_choice',
             'prompt': 'Este verano nosotros ___ viajar.', 'options': ['vamos a', 'vamos', 'van a'], 'correct_answer': 'vamos a',
             'translation': 'Этим летом мы поедем путешествовать.', 'explanation': 'vamos a viajar.'},
            {'section': 'Упражнение 2. Постройте ближайшее будущее (ir a + инфинитив)', 'exercise_type': 'multiple_choice',
             'prompt': 'Ellos ___ comprar una casa.', 'options': ['van a', 'van', 'vais a'], 'correct_answer': 'van a',
             'translation': 'Они собираются купить дом.', 'explanation': 'van a comprar.'},
            {'section': 'Упражнение 2. Постройте ближайшее будущее (ir a + инфинитив)', 'exercise_type': 'multiple_choice',
             'prompt': 'No ___ salir hoy. (yo)', 'options': ['voy a', 'vas a', 'voy'], 'correct_answer': 'voy a',
             'translation': 'Сегодня я не пойду гулять.', 'explanation': 'no voy a salir.'},
            {'section': 'Упражнение 2. Постройте ближайшее будущее (ir a + инфинитив)', 'exercise_type': 'multiple_choice',
             'prompt': '¡___ comer! (давайте есть!)', 'options': ['Vamos a', 'Van a', 'Vais a'], 'correct_answer': 'Vamos a',
             'translation': 'Давайте есть!', 'explanation': 'vamos a + инф. = давай(те).'},
            {'section': 'Упражнение 2. Постройте ближайшее будущее (ir a + инфинитив)', 'exercise_type': 'multiple_choice',
             'prompt': '___ que viene voy a empezar un curso. (на следующей неделе)', 'options': ['La semana', 'El semana', 'Una semana'], 'correct_answer': 'La semana',
             'translation': 'На следующей неделе я начну курс.', 'explanation': 'la semana que viene.'},
            {'section': 'Упражнение 2. Постройте ближайшее будущее (ir a + инфинитив)', 'exercise_type': 'multiple_choice',
             'prompt': '¿Vais a venir ___ fin de semana? (в эти выходные)', 'options': ['este', 'esta', 'esto'], 'correct_answer': 'este',
             'translation': 'Вы приедете в эти выходные?', 'explanation': 'este fin de semana (м. р.).'},
            {'section': 'Упражнение 2. Постройте ближайшее будущее (ir a + инфинитив)', 'exercise_type': 'multiple_choice',
             'prompt': 'Ella va a ___ el postre.', 'options': ['traer', 'trae', 'traigo'], 'correct_answer': 'traer',
             'translation': 'Она принесёт десерт.', 'explanation': 'После ir a — инфинитив.'},
            {'section': 'Упражнение 2. Постройте ближайшее будущее (ir a + инфинитив)', 'exercise_type': 'multiple_choice',
             'prompt': '___ mañana vamos a descansar. (послезавтра)', 'options': ['Pasado', 'Pasada', 'Después'], 'correct_answer': 'Pasado',
             'translation': 'Послезавтра мы будем отдыхать.', 'explanation': 'pasado mañana.'},
            # 3
            {'section': 'Упражнение 3. Планы. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Завтра я буду работать.»',
             'options': ['Mañana voy a trabajar.', 'Mañana voy trabajar.', 'Mañana va a trabajar yo.'],
             'correct_answer': 'Mañana voy a trabajar.', 'explanation': 'voy a + инфинитив.'},
            {'section': 'Упражнение 3. Планы. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Что ты будешь делать в субботу?»',
             'options': ['¿Qué vas a hacer el sábado?', '¿Qué vas hacer el sábado?', '¿Qué va a hacer tú el sábado?'],
             'correct_answer': '¿Qué vas a hacer el sábado?', 'explanation': 'vas a hacer; el sábado.'},
            {'section': 'Упражнение 3. Планы. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Мы пойдём в кино с моей сестрой.»',
             'options': ['Vamos a ir al cine con mi hermana.', 'Vamos ir al cine con mi hermana.', 'Vamos a ir al cine con mí hermana.'],
             'correct_answer': 'Vamos a ir al cine con mi hermana.', 'explanation': 'vamos a ir; mi hermana.'},
            {'section': 'Упражнение 3. Планы. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я бы с удовольствием пошла, но мне надо работать!»',
             'options': ['¡Me encantaría poder ir, pero tengo que trabajar!', '¡Me encanta ir, pero tengo ganas de trabajar!', '¡Me encantaría ir, pero hay que trabajo!'],
             'correct_answer': '¡Me encantaría poder ir, pero tengo que trabajar!', 'explanation': 'me encantaría… pero tengo que…'},
            {'section': 'Упражнение 3. Планы. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Удачи тебе!» (пожелание)',
             'options': ['¡Que te vaya bien!', '¡Que vas bien!', '¡Te va bien!'],
             'correct_answer': '¡Que te vaya bien!', 'explanation': 'Устойчивое пожелание.'},
            {'section': 'Упражнение 3. Планы. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Давайте посмотрим!»',
             'options': ['¡Vamos a ver!', '¡Vemos a ir!', '¡Van a ver!'],
             'correct_answer': '¡Vamos a ver!', 'explanation': 'vamos a ver — посмотрим.'},
            {'section': 'Упражнение 3. Планы. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Они не собираются продавать дом.»',
             'options': ['No van a vender la casa.', 'Van no a vender la casa.', 'No van vender la casa.'],
             'correct_answer': 'No van a vender la casa.', 'explanation': 'no + van a + инф.'},
            {'section': 'Упражнение 3. Планы. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Я принесу десерт, а ты накрой на стол.»',
             'options': ['Yo traigo el postre y tú pon la mesa.', 'Yo trao el postre y tú pones la mesa.', 'Yo traigo el postre y tú pon mesa la.'],
             'correct_answer': 'Yo traigo el postre y tú pon la mesa.', 'explanation': 'traigo + императив pon.'},
            {'section': 'Упражнение 3. Планы. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «В следующем году мы будем жить в Испании.»',
             'options': ['El año que viene vamos a vivir en España.', 'El año que viene vamos vivir en España.', 'El año próximo van a vivir en España nosotros.'],
             'correct_answer': 'El año que viene vamos a vivir en España.', 'explanation': 'el año que viene + vamos a.'},
            {'section': 'Упражнение 3. Планы. Переведите на испанский', 'exercise_type': 'translation',
             'prompt': 'Переведите: «Пойдёшь? — Конечно, мне очень хочется!»',
             'options': ['¿Vienes? — ¡Claro, tengo muchas ganas!', '¿Vas? — ¡Claro, tengo mucho gana!', '¿Vienes? — ¡Claro, estoy muchas ganas!'],
             'correct_answer': '¿Vienes? — ¡Claro, tengo muchas ganas!', 'explanation': 'tener ganas — очень хотеть.'},
        ],
    },
]
A1_FULL_3 = A1_FULL_3 + _B3
