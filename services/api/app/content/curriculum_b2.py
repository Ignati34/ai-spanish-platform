"""Full hand-authored B2 curriculum (syllabus Lessons 51–61), aligned to syllabus numbers.

Original, license-clean content. Advanced tenses / subjunctive / conditionals with cloze and
multiple-choice practice mirroring proficiency-test tasks. Each correct_answer exactly matches
one option.
"""

B2_LESSONS = [
    {
        'n': 51, 'level': 'B2', 'title': 'Условное наклонение (Potencial) и согласование',
        'theory': (
            'Condicional simple = инфинитив + -ía, -ías, -ía, -íamos, -íais, -ían: hablaría, comería. '
            'Неправильные основы как в будущем: tendría, haría, podría, diría.\n\n'
            'Значения: вежливость (¿Podría ayudarme?), гипотеза, и «будущее в прошлом» '
            '(согласование): Dijo que vendría (сказал, что придёт).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '¿___ (poder) ayudarme? (вежливо)',
             'options': ['Puede', 'Podría', 'Podrá'], 'correct_answer': 'Podría', 'explanation': 'Вежливость → condicional: podría.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Dijo que ___ (venir) más tarde.',
             'options': ['viene', 'vendría', 'vino'], 'correct_answer': 'vendría', 'explanation': 'Будущее в прошлом → condicional: vendría.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo en tu lugar ___ (hablar) con él.',
             'options': ['hablo', 'hablaría', 'hablé'], 'correct_answer': 'hablaría', 'explanation': 'Совет-гипотеза → hablaría.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ellos ___ (hacer) lo mismo.',
             'options': ['hacerían', 'harían', 'harán'], 'correct_answer': 'harían', 'explanation': 'hacer → har- + ían: harían.'},
        ],
    },
    {
        'n': 52, 'level': 'B2', 'title': 'Imperfecto de subjuntivo. Условия с si',
        'theory': (
            'Imperfecto de subjuntivo образуется от 3 л. мн. ч. indefinido: убираем -ron, '
            'добавляем -ra или -se: hablaron → hablara/hablase; fueron → fuera; tuvieron → tuviera.\n\n'
            'Нереальное/маловероятное условие (тип 2): Si + imperfecto de subjuntivo, → condicional.\n'
            '  Si tuviera dinero, viajaría. Si fuera tú, no lo haría.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Si yo ___ (tener) tiempo, iría.',
             'options': ['tengo', 'tuviera', 'tendría'], 'correct_answer': 'tuviera', 'explanation': 'Тип 2: si + imperfecto de subjuntivo: tuviera.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Si ___ (ser) tú, no lo haría.',
             'options': ['soy', 'fuera', 'sería'], 'correct_answer': 'fuera', 'explanation': 'si + imperfecto de subjuntivo: fuera.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Si tuviera dinero, ___ (comprar) un coche.',
             'options': ['compro', 'compraría', 'comprara'], 'correct_answer': 'compraría', 'explanation': 'Главная часть → condicional: compraría.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Ojalá ___ (ser) verdad.',
             'options': ['es', 'fuera', 'será'], 'correct_answer': 'fuera', 'explanation': 'Нереальное желание → fuera.'},
        ],
    },
    {
        'n': 53, 'level': 'B2', 'title': 'Imperfecto de subjuntivo (-er/-ir и неправильные)',
        'theory': (
            'Правило одно для всех: берём 3 л. мн. ч. indefinido, меняем -ron на -ra/-se:\n'
            '• comer: comieron → comiera; vivir: vivieron → viviera\n'
            '• hacer: hicieron → hiciera; poder: pudieron → pudiera; decir: dijeron → dijera; '
            'ir/ser: fueron → fuera; tener: tuvieron → tuviera.\n\n'
            'Используется после прошедшей воли/эмоции: Quería que vinieras. Me pidió que lo hiciera.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Quería que tú ___ (venir) conmigo.',
             'options': ['vienes', 'vinieras', 'vendrías'], 'correct_answer': 'vinieras', 'explanation': 'venir: vinieron → vinieras.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Me pidió que lo ___ (hacer).',
             'options': ['hago', 'hiciera', 'haría'], 'correct_answer': 'hiciera', 'explanation': 'hacer: hicieron → hiciera.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Si ___ (poder), te ayudaría.',
             'options': ['puedo', 'pudiera', 'podré'], 'correct_answer': 'pudiera', 'explanation': 'poder: pudieron → pudiera.'},
            {'exercise_type': 'fill_blank', 'prompt': 'No creía que él ___ (decir) eso.',
             'options': ['dice', 'dijera', 'diría'], 'correct_answer': 'dijera', 'explanation': 'decir: dijeron → dijera.'},
        ],
    },
    {
        'n': 54, 'level': 'B2', 'title': 'Perfecto de subjuntivo',
        'theory': (
            'Perfecto de subjuntivo = haya + participio: завершённое действие, о котором говорят '
            'с эмоцией/сомнением.\n'
            '  haya, hayas, haya, hayamos, hayáis, hayan + participio.\n\n'
            '  Me alegro de que hayas venido. No creo que lo haya hecho. Espero que haya llegado bien.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Me alegro de que ___ venido.',
             'options': ['has', 'hayas', 'habías'], 'correct_answer': 'hayas', 'explanation': 'Эмоция + завершённость → hayas venido.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'No creo que lo ___ hecho.',
             'options': ['ha', 'haya', 'había'], 'correct_answer': 'haya', 'explanation': 'Сомнение → haya hecho.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Espero que ___ llegado bien.',
             'options': ['han', 'hayan', 'habían'], 'correct_answer': 'hayan', 'explanation': 'Надежда → hayan llegado.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Es posible que ella ya ___ (haber) salido.',
             'options': ['ha', 'haya', 'había'], 'correct_answer': 'haya', 'explanation': 'es posible que → haya salido.'},
        ],
    },
    {
        'n': 55, 'level': 'B2', 'title': 'Condicional compuesto и Pluscuamperfecto de subjuntivo',
        'theory': (
            'Condicional compuesto = habría + participio: то, что произошло бы. '
            'Pluscuamperfecto de subjuntivo = hubiera/hubiese + participio.\n\n'
            'Нереальное условие в ПРОШЛОМ (тип 3): Si + pluscuamperfecto de subjuntivo, → '
            'condicional compuesto.\n'
            '  Si hubiera estudiado, habría aprobado. (но не выучил → не сдал)'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Si ___ estudiado, habría aprobado.',
             'options': ['había', 'hubiera', 'habré'], 'correct_answer': 'hubiera', 'explanation': 'Тип 3: si + pluscuamperfecto de subjuntivo: hubiera.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Si hubiera sabido, te lo ___ dicho.',
             'options': ['habría', 'había', 'hubiera'], 'correct_answer': 'habría', 'explanation': 'Главная часть типа 3 → condicional compuesto: habría dicho.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Yo que tú, ___ ido. (я бы пошёл)',
             'options': ['había', 'habría', 'hubiera'], 'correct_answer': 'habría', 'explanation': 'Гипотеза о прошлом → habría ido.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Si ___ (venir) antes, habrías visto el final.',
             'options': ['habías', 'hubieras', 'habrías'], 'correct_answer': 'hubieras', 'explanation': 'si + pluscuamperfecto de subjuntivo: hubieras venido.'},
        ],
    },
    {
        'n': 56, 'level': 'B2', 'title': 'Согласование глагольных времён (Concordancia)',
        'theory': (
            'Согласование: время придаточного зависит от главного.\n'
            '• Главное в настоящем/будущем → subjuntivo в настоящем: Quiero que vengas.\n'
            '• Главное в прошлом → imperfecto de subjuntivo: Quería que vinieras.\n\n'
            'Косвенная речь: presente → imperfecto (Dijo que venía), futuro → condicional '
            '(Dijo que vendría), indefinido/perfecto → pluscuamperfecto (Dijo que había venido).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Quería que tú ___ (estudiar) más.',
             'options': ['estudies', 'estudiaras', 'estudias'], 'correct_answer': 'estudiaras', 'explanation': 'Главное в прошлом → imperfecto de subjuntivo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Quiero que ___ (venir) hoy.',
             'options': ['vengas', 'vinieras', 'vienes'], 'correct_answer': 'vengas', 'explanation': 'Главное в настоящем → presente de subjuntivo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Dijo que ___ (venir) al día siguiente.',
             'options': ['viene', 'vendría', 'vino'], 'correct_answer': 'vendría', 'explanation': 'futuro → condicional: vendría.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Me contó que ya ___ (llegar). (до того)',
             'options': ['llega', 'había llegado', 'llegará'], 'correct_answer': 'había llegado', 'explanation': 'Действие до прошлого → pluscuamperfecto.'},
        ],
    },
    {
        'n': 57, 'level': 'B2', 'title': 'Сложный инфинитив. Артикль: общие правила',
        'theory': (
            'Сложный (составной) инфинитив = haber + participio: выражает предшествование. '
            'Gracias por haber venido. Después de haber comido, salimos.\n\n'
            'Артикль — общие правила: определённый (el/la) — об известном; неопределённый — о новом; '
            'нулевой — с профессией после ser, с веществами, с большинством стран.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Gracias por ___ venido.',
             'options': ['ha', 'haber', 'habiendo'], 'correct_answer': 'haber', 'explanation': 'Сложный инфинитив: haber venido.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Después de ___ comido, salimos.',
             'options': ['haber', 'ha', 'habido'], 'correct_answer': 'haber', 'explanation': 'haber + participio: haber comido.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Soy ___ ingeniero. (профессия)',
             'options': ['un', '— (без артикля)', 'el'], 'correct_answer': '— (без артикля)', 'explanation': 'Профессия после ser — без артикля.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ agua está fría. (известная)',
             'options': ['La', 'El', 'Una'], 'correct_answer': 'El', 'explanation': 'agua (ж. р.) с ударным a- берёт el: el agua.'},
        ],
    },
    {
        'n': 58, 'level': 'B2', 'title': 'Особые случаи употребления артикля',
        'theory': (
            'Особые случаи:\n'
            '• el/la перед именами не ставят (кроме разговорного): Juan, María.\n'
            '• с титулами при разговоре О человеке: El señor García llegó (но при обращении — без: '
            'Buenos días, señor García).\n'
            '• el agua, el águila — женские слова с ударным a-/ha- берут el в ед. ч. (мн.: las aguas).\n'
            '• дни недели с артиклем: Vengo el lunes. Los sábados descanso.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Vengo ___ lunes. (в понедельник)',
             'options': ['el', 'en', '— (без артикля)'], 'correct_answer': 'el', 'explanation': 'Дни недели с артиклем: el lunes.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ águila vuela alto.',
             'options': ['La', 'El', 'Una'], 'correct_answer': 'El', 'explanation': 'Ударное a- → el águila (ж. р.).'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ señor García ha llegado. (о нём)',
             'options': ['El', '— (без артикля)', 'Un'], 'correct_answer': 'El', 'explanation': 'С титулом о человеке → el señor García.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Las ___ del río están limpias. (воды)',
             'options': ['agua', 'aguas', 'el agua'], 'correct_answer': 'aguas', 'explanation': 'Во мн. ч. — las aguas.'},
        ],
    },
    {
        'n': 59, 'level': 'B2', 'title': 'Порядок слов и место местоимений (энклиза/проклиза)',
        'theory': (
            'Местоимения-дополнения:\n'
            '• перед спрягаемым глаголом (проклиза): Me lo da. No te lo digo.\n'
            '• присоединяются в конце (энклиза) к инфинитиву, герундию и утвердительному '
            'императиву: dármelo, dándomelo, dámelo.\n\n'
            'При двух местоимениях порядок: косвенное + прямое; le/les + lo → se lo. '
            'При энклизе может появляться акцент: dámelo, cuéntamelo.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Quiero ___ (дать это тебе).',
             'options': ['te lo dar', 'dártelo', 'lo darte'], 'correct_answer': 'dártelo', 'explanation': 'Энклиза к инфинитиву: dártelo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Императив: «дай мне это» —',
             'options': ['me lo da', 'dámelo', 'lo dame'], 'correct_answer': 'dámelo', 'explanation': 'Энклиза к утв. императиву: dámelo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Отрицательно: «не говори мне это» —',
             'options': ['no dímelo', 'no me lo digas', 'no me lo dices'], 'correct_answer': 'no me lo digas',
             'explanation': 'Отриц. императив → проклиза + subjuntivo: no me lo digas.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El regalo a Ana: «se ___ doy».',
             'options': ['le lo', 'se lo', 'lo se'], 'correct_answer': 'se lo', 'explanation': 'le + lo → se lo.'},
        ],
    },
    {
        'n': 60, 'level': 'B2', 'title': 'Предлоги и числительные от 100 до миллиона',
        'theory': (
            'Числительные: 100 = cien (перед сущ.: cien libros), но 101 = ciento uno. '
            '200 = doscientos, 500 = quinientos, 700 = setecientos, 900 = novecientos '
            '(согласуются: quinientas casas). 1000 = mil (не «un mil»). 1 000 000 = un millón (de).\n\n'
            'Годы читаются полностью: 1999 = mil novecientos noventa y nueve.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '100 книг: ___ libros.',
             'options': ['ciento', 'cien', 'cientos'], 'correct_answer': 'cien', 'explanation': 'Перед существительным → cien.'},
            {'exercise_type': 'multiple_choice', 'prompt': '500 = ___',
             'options': ['cincocientos', 'quinientos', 'quintos'], 'correct_answer': 'quinientos', 'explanation': '500 = quinientos.'},
            {'exercise_type': 'multiple_choice', 'prompt': '1 000 000 de personas = ___ de personas.',
             'options': ['un mil', 'un millón', 'mil'], 'correct_answer': 'un millón', 'explanation': 'Миллион: un millón de.'},
            {'exercise_type': 'multiple_choice', 'prompt': '500 домов: ___ casas.',
             'options': ['quinientos', 'quinientas', 'quiniento'], 'correct_answer': 'quinientas', 'explanation': 'Согласование с ж. р.: quinientas.'},
        ],
    },
    {
        'n': 61, 'level': 'B2', 'title': 'Правила переносов и пунктуация',
        'theory': (
            'Пунктуация: вопрос и восклицание обрамляются с двух сторон: ¿…? ¡…!\n'
            'Двоеточие, точка с запятой, кавычки «…» используются как в русском.\n\n'
            'Деление на слоги: одна согласная между гласными отходит к следующему слогу '
            '(ca-sa); ll, rr, ch неделимы (ca-lle, pe-rro, mu-cha-cho). Дифтонги не разрываются '
            '(cui-da-do).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Правильная запись вопроса:',
             'options': ['Cómo estás?', '¿Cómo estás?', '¿Cómo estás'], 'correct_answer': '¿Cómo estás?',
             'explanation': 'Вопрос обрамляется ¿ … ?'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Деление слова «calle»:',
             'options': ['cal-le', 'ca-lle', 'call-e'], 'correct_answer': 'ca-lle', 'explanation': 'll неделимо: ca-lle.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Деление слова «perro»:',
             'options': ['per-ro', 'pe-rro', 'perr-o'], 'correct_answer': 'pe-rro', 'explanation': 'rr неделимо: pe-rro.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Правильная запись восклицания:',
             'options': ['¡Qué bien!', 'Qué bien!', '¡Qué bien'], 'correct_answer': '¡Qué bien!',
             'explanation': 'Восклицание обрамляется ¡ … !'},
        ],
    },
]
