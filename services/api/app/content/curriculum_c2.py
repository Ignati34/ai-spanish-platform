"""Full hand-authored C2 curriculum (syllabus Lessons 74–84), aligned to syllabus numbers.

Original, license-clean mastery-level content (individual conjugation, adjective government,
subjunctive/indicative nuance, discourse & register, idioms, derivation, diacritics, emphasis,
middle/involuntary se). Cloze / multiple-choice practice. Each correct_answer matches an option.
"""

C2_LESSONS = [
    {
        'n': 74, 'level': 'C2', 'title': 'Индивидуальное спряжение: ir, hacer, decir, tener',
        'theory': (
            'Ключевые неправильные — по формам во всех временах:\n'
            '• ir: voy / fui / iba / iré / vaya / ve (императив)\n'
            '• hacer: hago / hice / haré / haga / haz; participio hecho\n'
            '• decir: digo / dije / diré / diga / di; participio dicho; gerundio diciendo\n'
            '• tener: tengo / tuve / tendré / tenga / ten'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer él ___ (decir) la verdad.',
             'options': ['dice', 'dijo', 'diría'], 'correct_answer': 'dijo', 'explanation': 'decir indefinido: dijo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Императив (tú) от hacer:',
             'options': ['hace', 'haz', 'haga'], 'correct_answer': 'haz', 'explanation': 'Императив: haz.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Participio от decir:',
             'options': ['decido', 'dicho', 'diciendo'], 'correct_answer': 'dicho', 'explanation': 'decir → dicho.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Mañana yo ___ (tener) tiempo.',
             'options': ['tuve', 'tendré', 'tenía'], 'correct_answer': 'tendré', 'explanation': 'tener futuro: tendré.'},
        ],
    },
    {
        'n': 75, 'level': 'C2', 'title': 'Индивидуальное спряжение: poder, poner, venir, salir',
        'theory': (
            '• poder: puedo / pude / podré / pueda; gerundio pudiendo\n'
            '• poner: pongo / puse / pondré / ponga / pon; participio puesto\n'
            '• venir: vengo / vine / vendré / venga / ven; gerundio viniendo\n'
            '• salir: salgo / salí / saldré / salga / sal'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer yo ___ (poner) la mesa.',
             'options': ['puse', 'ponía', 'pongo'], 'correct_answer': 'puse', 'explanation': 'poner indefinido: puse.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Mañana ellos ___ (venir) a casa.',
             'options': ['vinieron', 'vendrán', 'vienen'], 'correct_answer': 'vendrán', 'explanation': 'venir futuro: vendrán.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Participio от poner:',
             'options': ['ponido', 'puesto', 'poniendo'], 'correct_answer': 'puesto', 'explanation': 'poner → puesto.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Императив (tú) от salir:',
             'options': ['sale', 'sal', 'salga'], 'correct_answer': 'sal', 'explanation': 'Императив: sal.'},
        ],
    },
    {
        'n': 76, 'level': 'C2', 'title': 'Индивидуальное спряжение: caer, oír, traer, ver',
        'theory': (
            '• caer: caigo / caí / caeré / caiga; gerundio cayendo\n'
            '• oír: oigo, oyes, oye, oímos, oís, oyen / oí / oiré / oiga; gerundio oyendo\n'
            '• traer: traigo / traje / traeré / traiga; participio traído\n'
            '• ver: veo / vi / veía / veré / vea; participio visto'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Yo ___ (oír) música ahora. (presente)',
             'options': ['oyo', 'oigo', 'oío'], 'correct_answer': 'oigo', 'explanation': 'oír, 1 л.: oigo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer yo ___ (traer) el vino.',
             'options': ['traí', 'traje', 'traía'], 'correct_answer': 'traje', 'explanation': 'traer indefinido: traje.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Participio от ver:',
             'options': ['veído', 'visto', 'viendo'], 'correct_answer': 'visto', 'explanation': 'ver → visto.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Gerundio от caer:',
             'options': ['caiendo', 'cayendo', 'caendo'], 'correct_answer': 'cayendo', 'explanation': 'caer → cayendo.'},
        ],
    },
    {
        'n': 77, 'level': 'C2', 'title': 'Управление прилагательных',
        'theory': (
            'Прилагательные требуют фиксированного предлога:\n'
            '• lleno de — полный чего-то; capaz de — способный на; difícil de — трудный для;\n'
            '• responsable de — ответственный за; consciente de — осознающий;\n'
            '• harto de — сытый по горло; orgulloso de — гордый; contento con — довольный.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Un vaso lleno ___ agua.',
             'options': ['de', 'con', 'en'], 'correct_answer': 'de', 'explanation': 'lleno de.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es capaz ___ cualquier cosa.',
             'options': ['a', 'de', 'por'], 'correct_answer': 'de', 'explanation': 'capaz de.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Estoy contento ___ el resultado.',
             'options': ['de', 'con', 'por'], 'correct_answer': 'con', 'explanation': 'contento con.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es responsable ___ el equipo.',
             'options': ['de', 'por', 'a'], 'correct_answer': 'de', 'explanation': 'responsable de.'},
        ],
    },
    {
        'n': 78, 'level': 'C2', 'title': 'Subjuntivo vs indicativo: тонкие оттенки',
        'theory': (
            'Выбор наклонения меняет смысл:\n'
            '• Creo que viene (уверен) / No creo que venga (сомнение).\n'
            '• El hecho de que + subjuntivo (оценка факта): El hecho de que llueva no importa.\n'
            '• Cuando + indicativo (привычка/факт) / + subjuntivo (будущее): Cuando llega vs Cuando llegue.\n'
            '• Quizá(s) + indicativo (вероятнее) / + subjuntivo (менее вероятно).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'No creo que ___ (tener) razón.',
             'options': ['tiene', 'tenga', 'tendrá'], 'correct_answer': 'tenga', 'explanation': 'Сомнение → subjuntivo: tenga.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Creo que ella ___ (venir) hoy.',
             'options': ['venga', 'viene', 'viniera'], 'correct_answer': 'viene', 'explanation': 'Уверенность → indicativo: viene.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Cuando ___ (llegar) el jefe, avísame. (будущее)',
             'options': ['llega', 'llegue', 'llegará'], 'correct_answer': 'llegue', 'explanation': 'Будущее после cuando → subjuntivo: llegue.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El hecho de que ___ (llover) no cambia el plan.',
             'options': ['llueve', 'llueva', 'lloverá'], 'correct_answer': 'llueva', 'explanation': '«El hecho de que» → subjuntivo: llueva.'},
        ],
    },
    {
        'n': 79, 'level': 'C2', 'title': 'Маркеры дискурса и регистр',
        'theory': (
            'Регистр — соответствие ситуации:\n'
            '• формально: usted, le saluda atentamente, quisiera, ruego.\n'
            '• нейтрально/устно: o sea, es decir (то есть), pues, bueno, en fin.\n'
            '• уточнение: es decir / o sea; вывод: en resumen, en definitiva.\n\n'
            'Обращение на «Вы»: usted + 3 л. глагола (¿Cómo está usted?).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '¿Cómo ___ usted? (вежливо)',
             'options': ['estás', 'está', 'estáis'], 'correct_answer': 'está', 'explanation': 'usted + 3 л.: está.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Llegó tarde; ___, perdió el tren. (то есть)',
             'options': ['o sea', 'sin embargo', 'aunque'], 'correct_answer': 'o sea', 'explanation': 'Уточнение → o sea / es decir.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___, el proyecto fue un éxito. (в итоге)',
             'options': ['En definitiva', 'Es decir', 'Sino'], 'correct_answer': 'En definitiva', 'explanation': 'Вывод → en definitiva.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Форма для официального письма:',
             'options': ['Un abrazo', 'Le saluda atentamente', 'Nos vemos'], 'correct_answer': 'Le saluda atentamente',
             'explanation': 'Официальная концовка письма.'},
        ],
    },
    {
        'n': 80, 'level': 'C2', 'title': 'Устойчивые выражения и идиомы',
        'theory': (
            'Частые идиомы (значение не выводится дословно):\n'
            '• echar de menos — скучать по: Echo de menos a mi familia.\n'
            '• tener ganas de — хотеть/жаждать: Tengo ganas de verte.\n'
            '• dar con — наткнуться/найти: Di con la solución.\n'
            '• tomar el pelo — подшучивать: Me estás tomando el pelo.\n'
            '• meter la pata — сплоховать; hacer caso — обращать внимание/слушаться.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '«Скучаю по дому» — Echo ___ menos mi casa.',
             'options': ['de', 'a', 'en'], 'correct_answer': 'de', 'explanation': 'echar de menos.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Tengo ___ de un café. (хочу)',
             'options': ['ganas', 'gana', 'gusto'], 'correct_answer': 'ganas', 'explanation': 'tener ganas de.'},
            {'exercise_type': 'multiple_choice', 'prompt': '«Ты меня разыгрываешь» — Me tomas el ___.',
             'options': ['pelo', 'pie', 'pata'], 'correct_answer': 'pelo', 'explanation': 'tomar el pelo — подшучивать.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Por fin ___ con la respuesta. (нашёл)',
             'options': ['di', 'hice', 'puse'], 'correct_answer': 'di', 'explanation': 'dar con — наткнуться/найти: di con.'},
        ],
    },
    {
        'n': 81, 'level': 'C2', 'title': 'Словообразование: суффиксы и приставки',
        'theory': (
            'Суффиксы образуют новые слова:\n'
            '• -ción (действие): nación, canción; -dad (качество): verdad, ciudad;\n'
            '• -oso (обладание качеством): famoso; -ero (профессия/место): panadero.\n\n'
            'Приставки меняют смысл:\n'
            '• des- (отрицание/обратное): hacer → deshacer; in-/im- (не-): posible → imposible; '
            're- (повтор): hacer → rehacer.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Противоположность «posible» с приставкой:',
             'options': ['desposible', 'imposible', 'reposible'], 'correct_answer': 'imposible', 'explanation': 'in-/im-: imposible.'},
            {'exercise_type': 'multiple_choice', 'prompt': '«Сделать заново» — ___ el trabajo.',
             'options': ['deshacer', 'rehacer', 'inhacer'], 'correct_answer': 'rehacer', 'explanation': 're- (повтор): rehacer.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Существительное от «ciudad» — суффикс:',
             'options': ['-ción', '-dad', '-oso'], 'correct_answer': '-dad', 'explanation': '-dad — качество/существительное.'},
            {'exercise_type': 'multiple_choice', 'prompt': '«Развязать/расстегнуть» от hacer — ___.',
             'options': ['deshacer', 'rehacer', 'inhacer'], 'correct_answer': 'deshacer', 'explanation': 'des- (обратное действие): deshacer.'},
        ],
    },
    {
        'n': 82, 'level': 'C2', 'title': 'Ударение и различительный акцент (tilde diacrítica)',
        'theory': (
            'Различительный акцент отличает одинаковые по написанию слова:\n'
            '• tú (ты) / tu (твой); él (он) / el (артикль); sí (да) / si (если);\n'
            '• más (больше) / mas (но, книжн.); sé (знаю/будь) / se (местоимение);\n'
            '• té (чай) / te (тебя); qué/quién/cómo (вопрос) / que/quien/como (союз).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '¿___ tienes hambre? (ты)',
             'options': ['Tu', 'Tú', 'Tuu'], 'correct_answer': 'Tú', 'explanation': 'tú (ты) — с акцентом.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Quiero ___ café, por favor. (больше)',
             'options': ['mas', 'más', 'mass'], 'correct_answer': 'más', 'explanation': 'más (больше) — с акцентом.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Yo ___ la respuesta. (знаю)',
             'options': ['se', 'sé', 'sée'], 'correct_answer': 'sé', 'explanation': 'sé (знаю) — с акцентом.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿___ es tu nombre? (какой)',
             'options': ['Que', 'Qué', 'Qué?'], 'correct_answer': 'Qué', 'explanation': 'Вопросительное qué — с акцентом.'},
        ],
    },
    {
        'n': 83, 'level': 'C2', 'title': 'Эмфатические конструкции и порядок слов',
        'theory': (
            'Для выделения используют расщеплённые конструкции:\n'
            '• Fue Juan quien lo hizo. (именно Хуан сделал это)\n'
            '• Lo que necesito es tiempo. (что мне нужно — так это время)\n'
            '• Es aquí donde vivo. (именно здесь я живу)\n\n'
            'Вынос элемента в начало усиливает акцент: A ti te lo digo.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '___ Juan quien ganó. (именно Хуан)',
             'options': ['Es', 'Fue', 'Está'], 'correct_answer': 'Fue', 'explanation': 'Расщепление: fue Juan quien.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ que necesito es descansar.',
             'options': ['El', 'Lo', 'La'], 'correct_answer': 'Lo', 'explanation': 'Lo que … es — выделение.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es aquí ___ nos conocimos.',
             'options': ['que', 'donde', 'cuando'], 'correct_answer': 'donde', 'explanation': 'Место → es aquí donde.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Fue ayer ___ llegó la carta.',
             'options': ['donde', 'cuando', 'que'], 'correct_answer': 'cuando', 'explanation': 'Время → fue ayer cuando.'},
        ],
    },
    {
        'n': 84, 'level': 'C2', 'title': 'Средний залог и продвинутая безличность (se accidental)',
        'theory': (
            '«Se accidental» снимает вину с деятеля — действие как бы случайно:\n'
            '• Se me cayó el vaso. (я нечаянно уронил стакан)\n'
            '• Se me olvidó la cita. (я забыл о встрече)\n'
            '• Se nos rompió la tele. (у нас сломался телевизор)\n\n'
            'Структура: se + местоимение (me/te/le/nos/os/les) + глагол, согласованный с предметом.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Se ___ cayó el vaso. (я уронил)',
             'options': ['me', 'lo', 'le'], 'correct_answer': 'me', 'explanation': 'se me cayó — «у меня» упало.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Se me ___ las llaves. (я забыл)',
             'options': ['olvidó', 'olvidaron', 'olvido'], 'correct_answer': 'olvidaron', 'explanation': 'Согласование с «las llaves» (мн.): olvidaron.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Se nos ___ la tele. (у нас сломался)',
             'options': ['rompió', 'rompimos', 'rompemos'], 'correct_answer': 'rompió', 'explanation': 'Согласование с «la tele» (ед.): rompió.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Se ___ olvidó la cita (a ti).',
             'options': ['me', 'te', 'le'], 'correct_answer': 'te', 'explanation': 'se te olvidó — «ты забыл».'},
        ],
    },
]
