"""Additional original, license-clean curriculum lessons (theory + practice) so every CEFR
level is well populated out of the box. Grammar facts only; wording and exercises are original.

Merged into CURRICULUM by content/curriculum.py. Each exercise's correct_answer exactly
matches one option (validated in tests/at seed time)."""

EXTRA_LESSONS = [
    # ---------------- A1 ----------------
    {
        'level': 'A1',
        'title': 'Presente de indicativo: правильные глаголы',
        'theory': (
            'Правильные глаголы делятся на три группы по окончанию инфинитива: -ar, -er, -ir.\n\n'
            '• hablar: hablo, hablas, habla, hablamos, habláis, hablan\n'
            '• comer: como, comes, come, comemos, coméis, comen\n'
            '• vivir: vivo, vives, vive, vivimos, vivís, viven\n\n'
            'Окончание показывает лицо и число, поэтому местоимение часто опускают: (yo) hablo español.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (hablar) español.',
             'options': ['hablo', 'hablas', 'habla'], 'correct_answer': 'hablo',
             'explanation': '1 л. ед. ч. глагола -ar: hablo.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Nosotros ___ (comer) paella.',
             'options': ['come', 'comemos', 'comen'], 'correct_answer': 'comemos',
             'explanation': '1 л. мн. ч. глагола -er: comemos.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Ella ___ (vivir) en Madrid.',
             'options': ['vivo', 'vives', 'vive'], 'correct_answer': 'vive',
             'explanation': '3 л. ед. ч. глагола -ir: vive.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿Tú ___ (trabajar) aquí?',
             'options': ['trabajo', 'trabajas', 'trabaja'], 'correct_answer': 'trabajas',
             'explanation': '2 л. ед. ч. глагола -ar: trabajas.'},
        ],
    },
    {
        'level': 'A1',
        'title': 'Настоящее время: частые неправильные глаголы',
        'theory': (
            'Некоторые важные глаголы неправильны уже в настоящем времени:\n\n'
            '• tener (иметь): tengo, tienes, tiene, tenemos, tenéis, tienen\n'
            '• ir (идти/ехать): voy, vas, va, vamos, vais, van\n'
            '• hacer (делать): hago, haces, hace, hacemos, hacéis, hacen\n\n'
            'tener используют и для возраста: Tengo veinte años.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (tener) dos hermanos.',
             'options': ['tengo', 'tienes', 'tiene'], 'correct_answer': 'tengo',
             'explanation': 'tener, 1 л. ед. ч.: tengo.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Nosotros ___ (ir) al cine.',
             'options': ['voy', 'vamos', 'van'], 'correct_answer': 'vamos',
             'explanation': 'ir, 1 л. мн. ч.: vamos.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (hacer) la tarea.',
             'options': ['hago', 'haces', 'hace'], 'correct_answer': 'hago',
             'explanation': 'hacer, 1 л. ед. ч.: hago.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Yo ___ veinte años.',
             'options': ['soy', 'tengo', 'hago'], 'correct_answer': 'tengo',
             'explanation': 'Возраст выражается через tener: tengo veinte años.'},
        ],
    },
    {
        'level': 'A1',
        'title': 'Вопрос и отрицание',
        'theory': (
            'Вопрос: порядок слов гибкий, важны вопросительные слова и знаки ¿ ?\n'
            '• qué (что), quién (кто), dónde (где), cómo (как), cuándo (когда), por qué (почему).\n'
            '  ¿Dónde vives? ¿Qué haces?\n\n'
            'Отрицание: no ставится перед глаголом: No hablo francés. '
            'Двойное отрицание — норма: No veo nada. No viene nadie.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '¿___ vives? — En Madrid.',
             'options': ['Qué', 'Dónde', 'Quién'], 'correct_answer': 'Dónde',
             'explanation': 'Спрашиваем место → dónde.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿___ es? — Es mi hermano.',
             'options': ['Quién', 'Dónde', 'Cómo'], 'correct_answer': 'Quién',
             'explanation': 'Спрашиваем о человеке → quién.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ hablo francés. (отрицание)',
             'options': ['no', 'nada', 'nunca'], 'correct_answer': 'no',
             'explanation': 'Отрицание глагола: no перед глаголом.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'No veo ___.',
             'options': ['nada', 'algo', 'todo'], 'correct_answer': 'nada',
             'explanation': 'Двойное отрицание: no ... nada (ничего не вижу).'},
        ],
    },
    # ---------------- A2 ----------------
    {
        'level': 'A2',
        'title': 'Pretérito imperfecto',
        'theory': (
            'Imperfecto описывает фон, привычки и повторяющиеся действия в прошлом (что делал обычно).\n\n'
            '• -ar: hablaba, hablabas, hablaba, hablábamos, hablabais, hablaban\n'
            '• -er/-ir: comía, comías, comía... / vivía, vivías...\n\n'
            'Неправильные: ir → iba; ser → era; ver → veía.\n'
            'Пример: Cuando era niño, jugaba al fútbol todos los días.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Cuando era niño, yo ___ (jugar) mucho.',
             'options': ['jugué', 'jugaba', 'juego'], 'correct_answer': 'jugaba',
             'explanation': 'Привычка в прошлом → imperfecto: jugaba.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Antes nosotros ___ (vivir) en Sevilla.',
             'options': ['vivíamos', 'vivimos', 'viviremos'], 'correct_answer': 'vivíamos',
             'explanation': 'Длительное состояние в прошлом → imperfecto: vivíamos.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'De niña ella ___ (ser) muy tímida.',
             'options': ['fue', 'era', 'es'], 'correct_answer': 'era',
             'explanation': 'ser в imperfecto — era (описание в прошлом).'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Todos los días yo ___ al colegio.',
             'options': ['fui', 'iba', 'voy'], 'correct_answer': 'iba',
             'explanation': 'ir в imperfecto — iba (регулярность).'},
        ],
    },
    {
        'level': 'A2',
        'title': 'Futuro simple',
        'theory': (
            'Будущее образуется от инфинитива + окончания -é, -ás, -á, -emos, -éis, -án:\n'
            '• hablaré, comerás, vivirá, hablaremos...\n\n'
            'Есть неправильные основы: tener → tendré; hacer → haré; poder → podré; decir → diré.\n'
            'Пример: Mañana hablaré con el profesor.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Mañana yo ___ (hablar) con él.',
             'options': ['hablé', 'hablaré', 'hablaba'], 'correct_answer': 'hablaré',
             'explanation': 'Будущее, 1 л.: hablaré.'},
            {'exercise_type': 'fill_blank', 'prompt': 'El año que viene nosotros ___ (viajar) a Perú.',
             'options': ['viajamos', 'viajaremos', 'viajábamos'], 'correct_answer': 'viajaremos',
             'explanation': 'Будущее, 1 л. мн.: viajaremos.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Yo ___ (tener) tiempo el lunes.',
             'options': ['tendré', 'teneré', 'tenré'], 'correct_answer': 'tendré',
             'explanation': 'tener — неправильная основа будущего: tendré.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ellos lo ___ (hacer) pronto.',
             'options': ['hacerán', 'harán', 'harémos'], 'correct_answer': 'harán',
             'explanation': 'hacer → har-: harán.'},
        ],
    },
    {
        'level': 'A2',
        'title': 'Местоимения-дополнения: lo, la, le',
        'theory': (
            'Прямое дополнение (кого/что): lo, la, los, las. Косвенное (кому): le, les.\n\n'
            '• ¿Ves la casa? — Sí, la veo. (la = la casa)\n'
            '• ¿Compras el libro? — Sí, lo compro.\n'
            '• A María le doy un regalo. (le = a María)\n\n'
            'Местоимение ставится перед спрягаемым глаголом.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '¿Ves la casa? — Sí, ___ veo.',
             'options': ['lo', 'la', 'le'], 'correct_answer': 'la',
             'explanation': 'la casa — женский род, прямое дополнение → la.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿Compras el libro? — Sí, ___ compro.',
             'options': ['la', 'lo', 'les'], 'correct_answer': 'lo',
             'explanation': 'el libro — мужской род, прямое дополнение → lo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'A ellos ___ doy las gracias.',
             'options': ['los', 'les', 'las'], 'correct_answer': 'les',
             'explanation': 'Косвенное дополнение мн. ч.: les.'},
            {'exercise_type': 'fill_blank', 'prompt': 'A María ___ escribo una carta.',
             'options': ['la', 'le', 'lo'], 'correct_answer': 'le',
             'explanation': 'Кому пишу (косвенное) → le.'},
        ],
    },
    # ---------------- B1 ----------------
    {
        'level': 'B1',
        'title': 'Subjuntivo: сомнение и отрицание',
        'theory': (
            'После выражений сомнения и отрицания мнения — subjuntivo:\n'
            '• No creo que, dudo que, es posible que, no es verdad que + subjuntivo.\n'
            '  No creo que venga. Dudo que sea fácil.\n\n'
            'Но утверждение уверенности (creo que, es verdad que) идёт с indicativo: Creo que viene.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'No creo que él ___ hoy.',
             'options': ['viene', 'venga', 'vendrá'], 'correct_answer': 'venga',
             'explanation': 'После «no creo que» — subjuntivo: venga.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Dudo que ___ fácil.',
             'options': ['es', 'sea', 'será'], 'correct_answer': 'sea',
             'explanation': 'Сомнение → subjuntivo: sea.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Creo que María ___ razón.',
             'options': ['tenga', 'tiene', 'tener'], 'correct_answer': 'tiene',
             'explanation': 'Уверенность «creo que» → indicativo: tiene.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Es posible que ___ (llover) mañana.',
             'options': ['llueve', 'llueva', 'lloverá'], 'correct_answer': 'llueva',
             'explanation': '«Es posible que» → subjuntivo: llueva.'},
        ],
    },
    {
        'level': 'B1',
        'title': 'Condicional simple',
        'theory': (
            'Условное наклонение образуется от инфинитива + -ía, -ías, -ía, -íamos, -íais, -ían:\n'
            '• hablaría, comería, viviría...\n\n'
            'Неправильные основы те же, что в будущем: tendría, haría, podría, diría.\n'
            'Используется для вежливости и гипотез: ¿Podrías ayudarme? Me gustaría un café.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '¿___ (poder) ayudarme, por favor?',
             'options': ['Puedes', 'Podrías', 'Podrás'], 'correct_answer': 'Podrías',
             'explanation': 'Вежливая просьба → condicional: podrías.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Me ___ (gustar) un café.',
             'options': ['gusta', 'gustaría', 'gustó'], 'correct_answer': 'gustaría',
             'explanation': 'Вежливое желание → condicional: gustaría.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Yo en tu lugar ___ (hablar) con él.',
             'options': ['hablo', 'hablaría', 'hablé'], 'correct_answer': 'hablaría',
             'explanation': 'Совет-гипотеза → condicional: hablaría.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ellos ___ (hacer) lo mismo.',
             'options': ['hacerían', 'harían', 'harán'], 'correct_answer': 'harían',
             'explanation': 'hacer → har- + ían: harían.'},
        ],
    },
    {
        'level': 'B1',
        'title': 'Относительные местоимения: que, quien',
        'theory': (
            'Относительные слова соединяют предложения:\n'
            '• que — универсальное (о людях и вещах): El libro que leo. La chica que canta.\n'
            '• quien/quienes — только о людях, обычно после предлога: La persona con quien hablo.\n'
            '• el que / la que / lo que — «то, что»: Lo que dices es verdad.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'El libro ___ leo es interesante.',
             'options': ['que', 'quien', 'donde'], 'correct_answer': 'que',
             'explanation': 'О вещи → que.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'La persona con ___ hablo es mi jefe.',
             'options': ['que', 'quien', 'cual'], 'correct_answer': 'quien',
             'explanation': 'После предлога о человеке → quien.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ dices es verdad.',
             'options': ['Que', 'Lo que', 'Quien'], 'correct_answer': 'Lo que',
             'explanation': '«То, что» → lo que.'},
            {'exercise_type': 'fill_blank', 'prompt': 'La chica ___ canta es mi prima.',
             'options': ['que', 'quien', 'lo que'], 'correct_answer': 'que',
             'explanation': 'Подлежащее-человек в определительном → que.'},
        ],
    },
    # ---------------- B2 ----------------
    {
        'level': 'B2',
        'title': 'Imperfecto de subjuntivo',
        'theory': (
            'Прошедший субхунтив образуется от 3 л. мн. ч. indefinido, меняя -ron на -ra/-se:\n'
            '• hablaron → hablara/hablase; comieron → comiera; fueron → fuera.\n\n'
            'Используется в нереальных условиях и после прошедших выражений воли/эмоций:\n'
            'Si tuviera dinero... Quería que vinieras.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Si yo ___ (tener) tiempo, iría.',
             'options': ['tengo', 'tuviera', 'tendría'], 'correct_answer': 'tuviera',
             'explanation': 'Нереальное условие после si → imperfecto de subjuntivo: tuviera.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Quería que tú ___ conmigo.',
             'options': ['vienes', 'vinieras', 'vendrías'], 'correct_answer': 'vinieras',
             'explanation': 'Воля в прошлом → imperfecto de subjuntivo: vinieras.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Ojalá ___ (ser) verdad.',
             'options': ['es', 'fuera', 'será'], 'correct_answer': 'fuera',
             'explanation': 'Нереальное желание → fuera.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Me pidió que ___ (hablar) más despacio.',
             'options': ['hablo', 'hablara', 'hablaré'], 'correct_answer': 'hablara',
             'explanation': 'Просьба в прошлом → hablara.'},
        ],
    },
    {
        'level': 'B2',
        'title': 'Условные предложения: три типа',
        'theory': (
            'Тип 1 (реальное): Si + presente, → futuro/presente. Si llueve, me quedo en casa.\n'
            'Тип 2 (маловероятное/нереальное настоящее): Si + imperfecto de subjuntivo, → condicional. '
            'Si tuviera tiempo, viajaría.\n'
            'Тип 3 (нереальное прошлое): Si + pluscuamperfecto de subjuntivo, → condicional compuesto. '
            'Si hubiera estudiado, habría aprobado.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Si llueve, ___ en casa.',
             'options': ['me quedaría', 'me quedo', 'me quedara'], 'correct_answer': 'me quedo',
             'explanation': 'Тип 1: реальное условие → presente/futuro.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Si tuviera dinero, ___ un coche.',
             'options': ['compro', 'compraría', 'compré'], 'correct_answer': 'compraría',
             'explanation': 'Тип 2: главная часть → condicional.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Si ___ estudiado, habría aprobado.',
             'options': ['hubiera', 'había', 'habré'], 'correct_answer': 'hubiera',
             'explanation': 'Тип 3: si + pluscuamperfecto de subjuntivo: hubiera.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Si ___ (poder), te ayudaría.',
             'options': ['puedo', 'pudiera', 'podré'], 'correct_answer': 'pudiera',
             'explanation': 'Тип 2 после si → imperfecto de subjuntivo: pudiera.'},
        ],
    },
    {
        'level': 'B2',
        'title': 'Пассив и безличное se',
        'theory': (
            'Страдательный залог: ser + participio (+ por): La casa fue construida por ellos.\n'
            'Чаще используют пассив-рефлексив (se): Se venden coches. Se habla español.\n'
            'Безличное se — обобщённое «говорят/делают»: Se dice que... En España se cena tarde.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Aquí ___ español.',
             'options': ['se habla', 'es hablado', 'habla'], 'correct_answer': 'se habla',
             'explanation': 'Пассив-рефлексив: se habla.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ venden pisos.',
             'options': ['Se', 'Es', 'Está'], 'correct_answer': 'Se',
             'explanation': 'Пассив с se: se venden.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'La novela ___ escrita en 1980.',
             'options': ['fue', 'estuvo', 'se'], 'correct_answer': 'fue',
             'explanation': 'Пассив ser + participio: fue escrita.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'En España ___ cena tarde.',
             'options': ['se', 'es', 'está'], 'correct_answer': 'se',
             'explanation': 'Безличное se: se cena.'},
        ],
    },
    # ---------------- C1 ----------------
    {
        'level': 'C1',
        'title': 'El verbo Ser: полное спряжение',
        'theory': (
            'Ser неправильный почти во всех временах:\n'
            '• Presente: soy, eres, es, somos, sois, son\n'
            '• Indefinido: fui, fuiste, fue, fuimos, fuisteis, fueron (совпадает с ir)\n'
            '• Imperfecto: era, eras, era...\n'
            '• Futuro: seré, serás...  • Subjuntivo pres.: sea, seas...\n\n'
            'Ser — о сущности: происхождение, профессия, время, качество.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer ___ un día difícil.',
             'options': ['era', 'fue', 'es'], 'correct_answer': 'fue',
             'explanation': 'Завершённая характеристика события → indefinido: fue.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Espero que ___ verdad.',
             'options': ['es', 'sea', 'era'], 'correct_answer': 'sea',
             'explanation': 'После «espero que» → subjuntivo: sea.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Nosotros ___ (ser) amigos.',
             'options': ['somos', 'sois', 'son'], 'correct_answer': 'somos',
             'explanation': 'Presente 1 л. мн.: somos.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Mañana ___ el examen.',
             'options': ['fue', 'será', 'era'], 'correct_answer': 'será',
             'explanation': 'Будущее ser: será.'},
        ],
    },
    {
        'level': 'C1',
        'title': 'Индивидуальный глагол Ir',
        'theory': (
            'ir — крайне неправильный:\n'
            '• Presente: voy, vas, va, vamos, vais, van\n'
            '• Indefinido: fui, fuiste, fue, fuimos, fuisteis, fueron\n'
            '• Imperfecto: iba, ibas, iba...\n'
            '• Subjuntivo: vaya, vayas...  • Imperativo: ve\n\n'
            'ir a + инфинитив = ближайшее будущее: Voy a estudiar.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (ir) a estudiar ahora.',
             'options': ['voy', 'vas', 'va'], 'correct_answer': 'voy',
             'explanation': 'Presente 1 л.: voy (a estudiar).'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer ellos ___ al museo.',
             'options': ['iban', 'fueron', 'van'], 'correct_answer': 'fueron',
             'explanation': 'Завершённое в прошлом → indefinido: fueron.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Espero que ___ bien.',
             'options': ['va', 'vaya', 'iría'], 'correct_answer': 'vaya',
             'explanation': 'Subjuntivo ir: vaya.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'De pequeño yo ___ al parque cada día.',
             'options': ['fui', 'iba', 'voy'], 'correct_answer': 'iba',
             'explanation': 'Привычка → imperfecto: iba.'},
        ],
    },
    {
        'level': 'C1',
        'title': 'Индивидуальный глагол Hacer',
        'theory': (
            'hacer (делать) неправильный:\n'
            '• Presente: hago, haces, hace, hacemos, hacéis, hacen\n'
            '• Indefinido: hice, hiciste, hizo, hicimos, hicisteis, hicieron\n'
            '• Futuro: haré...  • Participio: hecho  • Imperativo: haz\n\n'
            'В выражениях времени: Hace calor. Hace dos años.'
        ),
        'exercises': [
            {'exercise_type': 'fill_blank', 'prompt': 'Yo ___ (hacer) deporte los lunes.',
             'options': ['hago', 'haces', 'hace'], 'correct_answer': 'hago',
             'explanation': 'Presente 1 л.: hago.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer él ___ la tarea.',
             'options': ['hizo', 'hació', 'hacía'], 'correct_answer': 'hizo',
             'explanation': 'Indefinido 3 л.: hizo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Hoy ___ mucho calor.',
             'options': ['hace', 'hay', 'es'], 'correct_answer': 'hace',
             'explanation': 'Погода: hace calor.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El participio de hacer es ___.',
             'options': ['hacido', 'hecho', 'hacho'], 'correct_answer': 'hecho',
             'explanation': 'Неправильное причастие: hecho.'},
        ],
    },
    {
        'level': 'C1',
        'title': 'Estar para vs estar por',
        'theory': (
            'Обе конструкции с estar, но смысл разный:\n'
            '• estar para + инфинитив — вот-вот сделать / готовность: Estoy para salir (я вот-вот выйду).\n'
            '• estar por + инфинитив — склонность/намерение или «ещё не сделано»: '
            'Estoy por llamarlo (я склонен позвонить). La carta está por escribir (письмо ещё не написано).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Ya estoy ___ salir, dame un minuto.',
             'options': ['para', 'por', 'de'], 'correct_answer': 'para',
             'explanation': 'Готовность вот-вот → estar para.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Estoy ___ llamarlo, aún lo dudo.',
             'options': ['para', 'por', 'a'], 'correct_answer': 'por',
             'explanation': 'Склонность/колебание → estar por.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'La cena está ___ preparar todavía.',
             'options': ['para', 'por', 'en'], 'correct_answer': 'por',
             'explanation': '«Ещё не сделано» → estar por.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El tren está ___ llegar.',
             'options': ['para', 'por', 'de'], 'correct_answer': 'para',
             'explanation': 'Вот-вот произойдёт → estar para.'},
        ],
    },
    # ---------------- C2 ----------------
    {
        'level': 'C2',
        'title': 'Управление глаголов: contar con, soñar con',
        'theory': (
            'Предлог con после глагола задаёт смысл:\n'
            '• contar con — рассчитывать на: Cuento con tu ayuda.\n'
            '• soñar con — мечтать о: Sueño con viajar.\n'
            '• casarse con — жениться на: Se casó con Ana.\n\n'
            'Предлог — часть управления, его нельзя опускать или заменять произвольно.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Cuento ___ tu apoyo.',
             'options': ['en', 'con', 'de'], 'correct_answer': 'con',
             'explanation': 'contar con — рассчитывать на.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Sueño ___ vivir junto al mar.',
             'options': ['con', 'de', 'en'], 'correct_answer': 'con',
             'explanation': 'soñar con — мечтать о.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Se casó ___ su novia.',
             'options': ['a', 'con', 'de'], 'correct_answer': 'con',
             'explanation': 'casarse con — жениться на.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Puedes contar ___ nosotros.',
             'options': ['con', 'en', 'para'], 'correct_answer': 'con',
             'explanation': 'contar con — рассчитывать на нас.'},
        ],
    },
    {
        'level': 'C2',
        'title': 'Управление глаголов: tardar en, insistir en',
        'theory': (
            'Предлог en после ряда глаголов:\n'
            '• tardar en — медлить/затрачивать время на: Tarda en responder.\n'
            '• insistir en — настаивать на: Insiste en venir.\n'
            '• pensar en — думать о: Pienso en ti.\n'
            '• consistir en — состоять в: El plan consiste en esperar.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Tarda mucho ___ contestar.',
             'options': ['de', 'en', 'a'], 'correct_answer': 'en',
             'explanation': 'tardar en — медлить с.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Insiste ___ pagar él.',
             'options': ['en', 'de', 'con'], 'correct_answer': 'en',
             'explanation': 'insistir en — настаивать на.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Siempre pienso ___ mi familia.',
             'options': ['de', 'en', 'con'], 'correct_answer': 'en',
             'explanation': 'pensar en — думать о.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El truco consiste ___ practicar cada día.',
             'options': ['de', 'en', 'a'], 'correct_answer': 'en',
             'explanation': 'consistir en — состоять в.'},
        ],
    },
    {
        'level': 'C2',
        'title': 'Управление глаголов: depender de, acordarse de',
        'theory': (
            'Предлог de после ряда глаголов:\n'
            '• depender de — зависеть от: Depende del tiempo.\n'
            '• acordarse de — помнить о: ¿Te acuerdas de mí?\n'
            '• quejarse de — жаловаться на: Se queja del ruido.\n'
            '• darse cuenta de — осознавать: Me di cuenta del error.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Todo depende ___ ti.',
             'options': ['de', 'en', 'a'], 'correct_answer': 'de',
             'explanation': 'depender de — зависеть от.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿Te acuerdas ___ aquel día?',
             'options': ['a', 'de', 'con'], 'correct_answer': 'de',
             'explanation': 'acordarse de — помнить о.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Se queja ___ todo.',
             'options': ['de', 'por', 'en'], 'correct_answer': 'de',
             'explanation': 'quejarse de — жаловаться на.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Me di cuenta ___ mi error.',
             'options': ['en', 'de', 'a'], 'correct_answer': 'de',
             'explanation': 'darse cuenta de — осознавать.'},
        ],
    },
    {
        'level': 'C2',
        'title': 'Адъективное управление',
        'theory': (
            'Прилагательные тоже требуют предлогов:\n'
            '• lleno de — полный чего-то: un vaso lleno de agua.\n'
            '• capaz de — способный на: capaz de todo.\n'
            '• difícil de — трудный для: difícil de entender.\n'
            '• responsable de — ответственный за.\n\n'
            'Предлог фиксирован при данном прилагательном.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Un vaso lleno ___ agua.',
             'options': ['de', 'con', 'en'], 'correct_answer': 'de',
             'explanation': 'lleno de — полный чего-то.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es capaz ___ cualquier cosa.',
             'options': ['a', 'de', 'por'], 'correct_answer': 'de',
             'explanation': 'capaz de — способный на.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es difícil ___ explicar.',
             'options': ['de', 'a', 'en'], 'correct_answer': 'de',
             'explanation': 'difícil de + инфинитив.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ella es responsable ___ el proyecto.',
             'options': ['de', 'por', 'a'], 'correct_answer': 'de',
             'explanation': 'responsable de — ответственный за.'},
        ],
    },
]
