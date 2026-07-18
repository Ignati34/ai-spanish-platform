"""Hand-authored B1 curriculum, part 2 (syllabus Lessons 41–50), aligned to syllabus numbers.

Original, license-clean content. Subjunctive-heavy, with cloze / multiple-choice practice.
Each correct_answer exactly matches one option.
"""

B1_LESSONS_2 = [
    {
        'n': 41, 'level': 'B1', 'title': 'Estar, ser, ir, saber, hacer во всех временах. Перифразы',
        'theory': (
            'Ключевые неправильные глаголы стоит знать во всех временах:\n'
            '• ser: soy / fui / era / seré / sería\n'
            '• estar: estoy / estuve / estaba / estaré\n'
            '• ir: voy / fui / iba / iré\n'
            '• hacer: hago / hice / hacía / haré\n\n'
            'Полезные перифразы: acabar de + инф. (только что сделать): Acabo de comer. '
            'dejar de + инф. (перестать): Dejé de fumar. volver a + инф. (снова): Volví a intentarlo.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '___ de comer, no tengo hambre. (только что)',
             'options': ['Acabo', 'Dejo', 'Vuelvo'], 'correct_answer': 'Acabo', 'explanation': 'acabar de — только что.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Él ___ de fumar el año pasado. (перестал)',
             'options': ['acabó', 'dejó', 'volvió'], 'correct_answer': 'dejó', 'explanation': 'dejar de — перестать.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Mañana yo ___ (hacer) el examen.',
             'options': ['hice', 'haré', 'hacía'], 'correct_answer': 'haré', 'explanation': 'hacer futuro: haré.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer ellos ___ (estar) en Madrid.',
             'options': ['estaban', 'estuvieron', 'están'], 'correct_answer': 'estuvieron', 'explanation': 'estar indefinido: estuvieron.'},
        ],
    },
    {
        'n': 42, 'level': 'B1', 'title': 'Estar, ser и безличные формы haber. Смена смысла',
        'theory': (
            'Некоторые прилагательные меняют смысл с ser или estar:\n'
            '• ser bueno (хороший по сути) / estar bueno (вкусный; хорошо себя чувствует)\n'
            '• ser listo (умный) / estar listo (готов)\n'
            '• ser aburrido (скучный) / estar aburrido (скучающий)\n\n'
            'hay (наличие, новое) vs está (конкретное известное): Hay un problema / El problema está claro.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'La paella ___ buenísima. (вкусная)',
             'options': ['es', 'está', 'hay'], 'correct_answer': 'está', 'explanation': 'estar bueno — вкусный.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Mi hermano ___ muy listo. (умный)',
             'options': ['es', 'está', 'hay'], 'correct_answer': 'es', 'explanation': 'ser listo — умный.'},
            {'exercise_type': 'multiple_choice', 'prompt': '¿Ya ___ listos para salir? (готовы)',
             'options': ['sois', 'estáis', 'hay'], 'correct_answer': 'estáis', 'explanation': 'estar listo — готов.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ un problema con el coche.',
             'options': ['Es', 'Está', 'Hay'], 'correct_answer': 'Hay', 'explanation': 'Наличие нового → hay.'},
        ],
    },
    {
        'n': 43, 'level': 'B1', 'title': 'El cual, предлог por. Sentir, soltar, poner',
        'theory': (
            'el cual / la cual / los cuales — «который», обычно после предлога в книжной речи: '
            'la razón por la cual...\n\n'
            'Предлог por (много значений): причина (por eso), «через/по» (por el parque), '
            'обмен/цена (por 10 euros), деятель в пассиве (por ellos), время суток (por la mañana).\n\n'
            'sentir (e→ie): siento; poner: pongo; volver a + инф. — снова.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Caminamos ___ el parque. («через»)',
             'options': ['para', 'por', 'en'], 'correct_answer': 'por', 'explanation': 'Движение через → por.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Lo compré ___ 10 euros. (за)',
             'options': ['para', 'por', 'de'], 'correct_answer': 'por', 'explanation': 'Цена/обмен → por.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Estudio ___ la mañana.',
             'options': ['por', 'para', 'en'], 'correct_answer': 'por', 'explanation': 'Время суток → por la mañana.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Lo ___ (sentir) mucho.',
             'options': ['sento', 'siento', 'siente'], 'correct_answer': 'siento', 'explanation': 'e→ie: siento.'},
        ],
    },
    {
        'n': 44, 'level': 'B1', 'title': 'Subjuntivo. Отрицательный императив',
        'theory': (
            'Presente de subjuntivo образуется от 1 л. ед. настоящего, меняя окончание:\n'
            '• -ar → -e: hablar (hablo) → hable, hables, hable, hablemos, habléis, hablen\n'
            '• -er/-ir → -a: comer → coma; vivir → viva\n\n'
            'Используется после воли/желания: Quiero que hables. Es отрицательный императив: '
            'no hables, no comas, no vengas (формы subjuntivo).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Quiero que tú ___ (hablar) más despacio.',
             'options': ['hablas', 'hables', 'hablar'], 'correct_answer': 'hables', 'explanation': 'Воля → subjuntivo: hables.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Отрицательный императив (tú) от «venir»:',
             'options': ['no vienes', 'no vengas', 'no venir'], 'correct_answer': 'no vengas', 'explanation': 'Отриц. императив = subjuntivo: no vengas.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Espero que ella ___ (comer) bien.',
             'options': ['come', 'coma', 'comer'], 'correct_answer': 'coma', 'explanation': 'subjuntivo -er → -a: coma.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'No ___ (tú, hablar) tan alto.',
             'options': ['hablas', 'hables', 'habla'], 'correct_answer': 'hables', 'explanation': 'Отриц. императив: no hables.'},
        ],
    },
    {
        'n': 45, 'level': 'B1', 'title': 'Presente de subjuntivo (-er/-ir). Para que',
        'theory': (
            'Subjuntivo глаголов на -er/-ir идёт на -a: beber → beba, escribir → escriba.\n'
            'Глаголы с чередованием сохраняют его: poder → pueda, querer → quiera, pedir → pida.\n\n'
            'Союз para que (чтобы) всегда требует subjuntivo: Te lo digo para que lo sepas. '
            'Так же: a fin de que, sin que.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Te llamo para que ___ (saber) la verdad.',
             'options': ['sabes', 'sepas', 'saber'], 'correct_answer': 'sepas', 'explanation': 'para que → subjuntivo: sepas.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Quiero que él ___ (escribir) la carta.',
             'options': ['escribe', 'escriba', 'escribir'], 'correct_answer': 'escriba', 'explanation': '-ir subjuntivo: escriba.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es raro que no ___ (poder) venir.',
             'options': ['puede', 'pueda', 'podría'], 'correct_answer': 'pueda', 'explanation': 'poder subjuntivo: pueda.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Lo hago para que tú ___ (descansar).',
             'options': ['descansas', 'descanses', 'descansar'], 'correct_answer': 'descanses', 'explanation': 'para que → descanses.'},
        ],
    },
    {
        'n': 46, 'level': 'B1', 'title': 'Subjuntivo неправильных. Безличные обороты',
        'theory': (
            'Неправильный subjuntivo (от неправильного 1 л.):\n'
            '• hacer → haga, decir → diga, ir → vaya, ser → sea, tener → tenga, poner → ponga, '
            'salir → salga, ver → vea, saber → sepa, dar → dé, estar → esté, haber → haya.\n\n'
            'Безличные обороты требуют subjuntivo: es necesario que, es importante que, '
            'es posible que, conviene que. Es necesario que vengas.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Es necesario que tú ___ (venir).',
             'options': ['vienes', 'vengas', 'venir'], 'correct_answer': 'vengas', 'explanation': 'venir subjuntivo: vengas.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es importante que él ___ (ser) puntual.',
             'options': ['es', 'sea', 'será'], 'correct_answer': 'sea', 'explanation': 'ser subjuntivo: sea.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es posible que ___ (haber) huelga.',
             'options': ['hay', 'haya', 'habrá'], 'correct_answer': 'haya', 'explanation': 'haber subjuntivo: haya.'},
            {'exercise_type': 'fill_blank', 'prompt': 'Conviene que ___ (tú, hacer) ejercicio.',
             'options': ['haces', 'hagas', 'hacer'], 'correct_answer': 'hagas', 'explanation': 'hacer subjuntivo: hagas.'},
        ],
    },
    {
        'n': 47, 'level': 'B1', 'title': 'Употребление subjuntivo. Оборот he de',
        'theory': (
            'Subjuntivo в определительных придаточных, когда объект неизвестен/гипотетичен:\n'
            '  Busco a alguien que hable ruso. (не знаю такого) vs Conozco a alguien que habla ruso.\n\n'
            'Оборот he de + инфинитив = долженствование (книжн.): He de terminarlo hoy '
            '(= tengo que / debo).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Busco un piso que ___ (tener) balcón.',
             'options': ['tiene', 'tenga', 'tendrá'], 'correct_answer': 'tenga', 'explanation': 'Неизвестный объект → subjuntivo: tenga.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Conozco a alguien que ___ (hablar) chino.',
             'options': ['hable', 'habla', 'hablara'], 'correct_answer': 'habla', 'explanation': 'Известный/реальный → indicativo: habla.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'He de ___ (terminar) hoy. (должен)',
             'options': ['terminar', 'termine', 'termino'], 'correct_answer': 'terminar', 'explanation': 'he de + инфинитив: terminar.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'No hay nadie que ___ (saber) la respuesta.',
             'options': ['sabe', 'sepa', 'sabrá'], 'correct_answer': 'sepa', 'explanation': 'Отрицание существования → subjuntivo: sepa.'},
        ],
    },
    {
        'n': 48, 'level': 'B1', 'title': 'Subjuntivo: эмоции, сомнение, aunque',
        'theory': (
            'Subjuntivo после:\n'
            '• эмоций: me alegro de que, es una pena que, me molesta que.\n'
            '• сомнения/отрицания мнения: no creo que, dudo que.\n'
            '• уступки с гипотезой: aunque + subjuntivo («даже если»): Aunque llueva, saldré. '
            '(если факт — indicativo: Aunque llueve, salgo.)'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Me alegro de que ___ (tú, estar) aquí.',
             'options': ['estás', 'estés', 'estarás'], 'correct_answer': 'estés', 'explanation': 'Эмоция → subjuntivo: estés.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'No creo que ___ (llover) hoy.',
             'options': ['llueve', 'llueva', 'lloverá'], 'correct_answer': 'llueva', 'explanation': 'Сомнение → subjuntivo: llueva.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Aunque ___ (hacer) frío, saldré. (даже если)',
             'options': ['hace', 'haga', 'hará'], 'correct_answer': 'haga', 'explanation': 'Гипотеза с aunque → subjuntivo: haga.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es una pena que no ___ (poder) venir.',
             'options': ['puedes', 'puedas', 'podrás'], 'correct_answer': 'puedas', 'explanation': 'Эмоция → subjuntivo: puedas.'},
        ],
    },
    {
        'n': 49, 'level': 'B1', 'title': 'Subjuntivo после cuando, mientras, ojalá, quizás',
        'theory': (
            'Subjuntivo о будущем после временных союзов:\n'
            '  Cuando llegues, llámame. Mientras estudies, no veas la tele.\n'
            '  (о факте/привычке — indicativo: Cuando llego, siempre llamo.)\n\n'
            'ojalá + subjuntivo (хоть бы): Ojalá venga. '
            'quizás/tal vez + subjuntivo (может быть): Quizás llueva.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Cuando ___ (tú, llegar), llámame.',
             'options': ['llegas', 'llegues', 'llegarás'], 'correct_answer': 'llegues', 'explanation': 'Будущее после cuando → subjuntivo: llegues.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ojalá ___ (venir) mañana.',
             'options': ['viene', 'venga', 'vendrá'], 'correct_answer': 'venga', 'explanation': 'ojalá → subjuntivo: venga.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Quizás ___ (llover) esta noche.',
             'options': ['llueve', 'llueva', 'llovió'], 'correct_answer': 'llueva', 'explanation': 'quizás → subjuntivo: llueva.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Cuando ___ (yo, llegar) a casa, siempre descanso. (привычка)',
             'options': ['llego', 'llegue', 'llegaré'], 'correct_answer': 'llego', 'explanation': 'Привычка → indicativo: llego.'},
        ],
    },
    {
        'n': 50, 'level': 'B1', 'title': 'Союз sino. Предлог a',
        'theory': (
            'pero vs sino:\n'
            '• pero — «но» (добавление/противопоставление): Es caro, pero bueno.\n'
            '• sino — «а/а наоборот» после отрицания: No es rojo, sino azul. '
            'sino que — если дальше глагол: No trabaja, sino que estudia.\n\n'
            'Предлог a: направление (voy a Madrid), «личное a» перед одушевлённым дополнением '
            '(Veo a María), время (a las tres).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'No es rojo, ___ azul.',
             'options': ['pero', 'sino', 'que'], 'correct_answer': 'sino', 'explanation': 'После отрицания «а» → sino.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Es caro, ___ muy bueno.',
             'options': ['sino', 'pero', 'sino que'], 'correct_answer': 'pero', 'explanation': 'Противопоставление без отрицания → pero.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Veo ___ María en el parque. (личное a)',
             'options': ['a', 'de', 'en'], 'correct_answer': 'a', 'explanation': 'Личное a перед одушевлённым дополнением.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'No canta, ___ baila.',
             'options': ['sino', 'sino que', 'pero'], 'correct_answer': 'sino que', 'explanation': 'Перед глаголом → sino que.'},
        ],
    },
]
