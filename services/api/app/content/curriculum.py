"""Original, license-clean starter curriculum (theory + practice) across A1–C2.

Grammar *facts* (conjugations, spelling rules, verb/adjective government) are not
copyrightable; the wording, structure and exercises here are original and do not
reproduce any textbook's or website's specific expression. Learners extend the course
with their own material via Upload Studio.

Each lesson: level, title, theory (RU with Spanish examples), and interactive exercises
where `correct_answer` exactly matches one `options` entry.
"""

CURRICULUM = [
    # ---------------- A1 ----------------
    {
        'level': 'A1',
        'title': 'Ser и estar: два «быть»',
        'theory': (
            'В испанском есть два глагола со значением «быть».\n\n'
            '• SER — про постоянное: кто/что это, профессия, национальность, характер, время.\n'
            '  Soy estudiante. Es español. Son las tres.\n\n'
            '• ESTAR — про состояние и местоположение: где находится, как себя чувствует.\n'
            '  Estoy en casa. Está cansado. Estamos bien.\n\n'
            'Подсказка: временное состояние и «где» — это estar; всё «по сути» — ser.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Yo ___ estudiante.',
             'options': ['soy', 'estoy', 'es'], 'correct_answer': 'soy',
             'explanation': 'Профессия/роль — это постоянный признак, поэтому ser: yo soy.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Nosotros ___ en el parque.',
             'options': ['somos', 'estamos', 'están'], 'correct_answer': 'estamos',
             'explanation': 'Местоположение всегда через estar: nosotros estamos.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ella ___ cansada hoy.',
             'options': ['es', 'está', 'son'], 'correct_answer': 'está',
             'explanation': 'Временное состояние (усталость) — estar: ella está cansada.'},
        ],
    },
    {
        'level': 'A1',
        'title': 'Артикли и род существительных',
        'theory': (
            'Существительные в испанском мужского или женского рода.\n\n'
            '• Обычно -o → мужской род (el libro), -a → женский (la casa).\n'
            '• Определённый артикль: el / la (мн. los / las).\n'
            '• Неопределённый: un / una (мн. unos / unas).\n\n'
            'Есть исключения (el problema, el día, la mano) — их запоминают отдельно.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '___ casa es grande.',
             'options': ['El', 'La', 'Los'], 'correct_answer': 'La',
             'explanation': 'casa оканчивается на -a и женского рода: la casa.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Quiero ___ libro.',
             'options': ['una', 'un', 'unos'], 'correct_answer': 'un',
             'explanation': 'libro мужского рода, единственное число: un libro.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ problema es difícil.',
             'options': ['La', 'El', 'Las'], 'correct_answer': 'El',
             'explanation': 'problema — исключение: мужской род, хотя оканчивается на -a.'},
        ],
    },
    # ---------------- A2 ----------------
    {
        'level': 'A2',
        'title': 'Pretérito indefinido: рассказ о прошлом',
        'theory': (
            'Indefinido описывает завершённое действие в прошлом (вчера, в прошлом году).\n\n'
            'Правильные окончания:\n'
            '• -ar: hablé, hablaste, habló, hablamos, hablasteis, hablaron\n'
            '• -er/-ir: comí, comiste, comió, comimos, comisteis, comieron\n\n'
            'Частые неправильные: ir и ser совпадают → fui, fuiste, fue…; tener → tuve; hacer → hice.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer ___ al cine.',
             'options': ['voy', 'fui', 'iba'], 'correct_answer': 'fui',
             'explanation': 'Завершённое действие в прошлом; ir в indefinido: yo fui.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Ayer (yo) ___ (comer) paella.',
             'options': ['comí', 'como', 'comía'], 'correct_answer': 'comí',
             'explanation': 'Правильный глагол -er в indefinido, 1 л.: comí.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El año pasado ellos ___ una casa.',
             'options': ['compran', 'compraron', 'compraban'], 'correct_answer': 'compraron',
             'explanation': 'Завершённое действие, 3 л. мн.: compraron.'},
        ],
    },
    {
        'level': 'A2',
        'title': 'Глагол gustar',
        'theory': (
            'gustar работает «наоборот»: нравящееся — подлежащее, а человек — в дательном.\n\n'
            '• Me gusta el café. (мне нравится кофе — ед.)\n'
            '• Me gustan los libros. (мне нравятся книги — мн.)\n\n'
            'Местоимения: me, te, le, nos, os, les. Так же ведут себя encantar, interesar, doler.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'A mí me ___ los libros.',
             'options': ['gusta', 'gustan', 'gusto'], 'correct_answer': 'gustan',
             'explanation': 'Подлежащее «los libros» во мн. числе → gustan.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ gusta el chocolate.',
             'options': ['Me', 'Yo', 'Mi'], 'correct_answer': 'Me',
             'explanation': 'Нужно местоимение дательного падежа: me gusta.'},
            {'exercise_type': 'fill_blank', 'prompt': 'A ella le ___ (encantar) bailar.',
             'options': ['encanta', 'encantan', 'encantas'], 'correct_answer': 'encanta',
             'explanation': 'Инфинитив bailar — единое подлежащее ед. числа → encanta.'},
        ],
    },
    # ---------------- B1 ----------------
    {
        'level': 'B1',
        'title': 'Por и para',
        'theory': (
            'Оба переводятся «для/за», но по смыслу различаются.\n\n'
            '• PARA — цель, назначение, срок, адресат: Estudio para aprobar. Es para ti.\n'
            '• POR — причина, обмен, «через/по», длительность: Gracias por tu ayuda. Paso por el parque.\n\n'
            'Грубо: para смотрит вперёд (цель), por — назад (причина) или «сквозь».'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Estudio español ___ mi trabajo.',
             'options': ['por', 'para', 'de'], 'correct_answer': 'para',
             'explanation': 'Цель (ради работы) → para.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Gracias ___ tu ayuda.',
             'options': ['para', 'por', 'en'], 'correct_answer': 'por',
             'explanation': 'Благодарность за причину/действие → por.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Este regalo es ___ ti.',
             'options': ['por', 'para', 'a'], 'correct_answer': 'para',
             'explanation': 'Адресат подарка → para ti.'},
        ],
    },
    {
        'level': 'B1',
        'title': 'Presente de subjuntivo: желания и эмоции',
        'theory': (
            'Subjuntivo выражает желания, эмоции, сомнение, оценку — не факт, а отношение.\n\n'
            'После espero que, quiero que, es importante que, me alegro de que + subjuntivo:\n'
            '• Espero que estés bien. Quiero que vengas.\n\n'
            'Образование (от 1 л. presente, меняем гласную): hablar → hable; comer → coma; vivir → viva.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Espero que ___ bien.',
             'options': ['estás', 'estés', 'estar'], 'correct_answer': 'estés',
             'explanation': 'После «espero que» — subjuntivo: estés.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Quiero que (tú) ___ conmigo.',
             'options': ['vienes', 'vengas', 'venir'], 'correct_answer': 'vengas',
             'explanation': 'Желание → subjuntivo; venir → vengas.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Es importante que (nosotros) ___ (hablar) español.',
             'options': ['hablamos', 'hablemos', 'hablar'], 'correct_answer': 'hablemos',
             'explanation': 'Оценка «es importante que» → subjuntivo: hablemos.'},
        ],
    },
    # ---------------- B2 ----------------
    {
        'level': 'B2',
        'title': 'Condicional и гипотезы',
        'theory': (
            'Условные предложения о нереальном: si + imperfecto de subjuntivo, главная часть — condicional.\n\n'
            '• Si tuviera tiempo, viajaría más.\n'
            '• Si fuera rico, compraría una casa.\n\n'
            'Condicional образуется от инфинитива + окончания -ía: viajaría, comería, viviría.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Si tuviera tiempo, ___ más.',
             'options': ['viajo', 'viajaré', 'viajaría'], 'correct_answer': 'viajaría',
             'explanation': 'Нереальное условие → главная часть в condicional: viajaría.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Si ___ rico, compraría un coche.',
             'options': ['soy', 'fuera', 'seré'], 'correct_answer': 'fuera',
             'explanation': 'После si в нереальном условии — imperfecto de subjuntivo: fuera.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo en tu lugar ___ (hablar) con él.',
             'options': ['hablo', 'hablaría', 'hablé'], 'correct_answer': 'hablaría',
             'explanation': 'Совет-гипотеза → condicional: hablaría.'},
        ],
    },
    {
        'level': 'B2',
        'title': 'Коннекторы речи',
        'theory': (
            'Связки делают речь логичной и связной.\n\n'
            '• Противопоставление: sin embargo, no obstante, aunque.\n'
            '• Следствие: por lo tanto, así que, por eso.\n'
            '• Причина: porque, ya que, puesto que.\n\n'
            'Пример: No vino, ya que estaba enfermo. Llovía; sin embargo, salimos.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'No vino, ___ estaba enfermo.',
             'options': ['aunque', 'ya que', 'para que'], 'correct_answer': 'ya que',
             'explanation': 'Причина → ya que (= потому что).'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Estudió mucho; ___, aprobó.',
             'options': ['sin embargo', 'por lo tanto', 'aunque'], 'correct_answer': 'por lo tanto',
             'explanation': 'Следствие (усилия → результат) → por lo tanto.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Hacía frío; ___, fuimos a la playa.',
             'options': ['por eso', 'sin embargo', 'porque'], 'correct_answer': 'sin embargo',
             'explanation': 'Противопоставление (холод, но пошли) → sin embargo.'},
        ],
    },
    # ---------------- C1 ----------------
    {
        'level': 'C1',
        'title': 'Орфографические замены при спряжении',
        'theory': (
            'Чтобы сохранить звук основы, при спряжении меняется буква (не звук).\n\n'
            '• -car: c → qu перед e: atacar → ataqué (звук k сохраняется).\n'
            '• -gar: g → gu перед e: pagar → pagué.\n'
            '• -zar: z → c перед e: empezar → empecé.\n'
            '• -cer/-cir: c → z перед o/a: vencer → venzo; proteger → protejo (g → j).\n\n'
            'Логика одна: буква меняется, чтобы звук остался прежним.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Ayer yo ___ (atacar) el problema.',
             'options': ['atacé', 'ataqué', 'ataquè'], 'correct_answer': 'ataqué',
             'explanation': '-car: перед -é пишем qu, чтобы сохранить звук k: ataqué.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (vencer) mis miedos.',
             'options': ['venco', 'venzo', 'venço'], 'correct_answer': 'venzo',
             'explanation': '-cer: перед o пишем z: venzo (звук θ сохраняется).'},
            {'exercise_type': 'fill_blank', 'prompt': 'Ayer yo ___ (pagar) la cuenta.',
             'options': ['pagé', 'pagué', 'paguè'], 'correct_answer': 'pagué',
             'explanation': '-gar: перед -é добавляем u: pagué (звук g твёрдый).'},
        ],
    },
    # ---------------- C2 ----------------
    {
        'level': 'C2',
        'title': 'Индивидуальные глаголы и управление предлогами',
        'theory': (
            'Некоторые глаголы имеют уникальные формы 1 л. и особую основу в прошедшем:\n'
            '• caer → caigo; cayó / cayeron.  • oír → oigo; oyó / oyeron.  • poder → puedo; pudo / pudieron.\n\n'
            'Управление предлогами задаёт смысл:\n'
            '• contar con (рассчитывать на): Cuento contigo.\n'
            '• tardar en (медлить с): Tarda en responder.\n'
            '• temblar de (дрожать от): Temblar de frío.\n'
            '• cesar de (перестать): Cesó de llover.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (caer) al suelo. (presente, 1 л.)',
             'options': ['cao', 'caigo', 'caío'], 'correct_answer': 'caigo',
             'explanation': 'caer имеет особую форму 1 л.: caigo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Cuento ___ tu ayuda mañana.',
             'options': ['en', 'con', 'de'], 'correct_answer': 'con',
             'explanation': 'contar con — рассчитывать на: cuento con tu ayuda.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El profesor tarda ___ corregir los exámenes.',
             'options': ['de', 'en', 'con'], 'correct_answer': 'en',
             'explanation': 'tardar en — медлить с чем-то: tarda en corregir.'},
        ],
    },
]
