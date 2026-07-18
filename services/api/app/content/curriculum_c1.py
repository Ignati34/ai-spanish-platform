"""Full hand-authored C1 curriculum (syllabus Lessons 62–73), aligned to syllabus numbers.

Original, license-clean advanced grammar (periphrases, passive nuance, complex reported speech,
subjunctive in relatives, concession, verbs of change, orthographic changes, verb government,
ser/estar nuances). Cloze / multiple-choice practice. Each correct_answer matches an option.
"""

C1_LESSONS = [
    {
        'n': 62, 'level': 'C1', 'title': 'Продвинутые глагольные перифразы',
        'theory': (
            'Перифразы с герундием передают оттенки протекания:\n'
            '• llevar + gerundio — длительность до сих пор: Llevo dos años estudiando español.\n'
            '• seguir/continuar + gerundio — продолжение: Sigue lloviendo.\n'
            '• ir + gerundio — постепенность: Va mejorando poco a poco.\n'
            '• andar + gerundio — «всё время»: Anda buscando trabajo.\n'
            '• acabar por + инфинитив — «в итоге»: Acabó por aceptar.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '___ dos años estudiando aquí. (длительность до сих пор)',
             'options': ['Llevo', 'Acabo', 'Vuelvo'], 'correct_answer': 'Llevo', 'explanation': 'llevar + gerundio — длительность.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Todavía ___ lloviendo. (продолжается)',
             'options': ['va', 'sigue', 'anda'], 'correct_answer': 'sigue', 'explanation': 'seguir + gerundio — продолжение.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'La situación ___ mejorando poco a poco. (постепенно)',
             'options': ['va', 'lleva', 'acaba'], 'correct_answer': 'va', 'explanation': 'ir + gerundio — постепенность.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Al final ___ por aceptar. (в итоге)',
             'options': ['acabó', 'llevó', 'siguió'], 'correct_answer': 'acabó', 'explanation': 'acabar por + инфинитив.'},
        ],
    },
    {
        'n': 63, 'level': 'C1', 'title': 'Пассив: ser против пассива-рефлексива',
        'theory': (
            'Два способа выразить страдательность:\n'
            '• Пассив с ser (+ por + деятель) — книжно, деятель важен: La ley fue aprobada por el '
            'parlamento.\n'
            '• Пассив-рефлексив (se) — деятель не важен/обобщён, естественнее в речи: '
            'Se aprobó la ley. Se venden pisos.\n\n'
            'Причастие в пассиве ser согласуется: fue aprobada, fueron construidos.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'La ley ___ aprobada por el parlamento.',
             'options': ['se', 'fue', 'está'], 'correct_answer': 'fue', 'explanation': 'Пассив ser + деятель por: fue aprobada.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Aquí ___ venden pisos. (обобщённо)',
             'options': ['son', 'se', 'están'], 'correct_answer': 'se', 'explanation': 'Пассив-рефлексив: se venden.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Los puentes ___ construidos en 1990.',
             'options': ['fue', 'fueron', 'se'], 'correct_answer': 'fueron', 'explanation': 'Согласование мн.: fueron construidos.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ dice que habrá cambios. (говорят)',
             'options': ['Es', 'Se', 'Está'], 'correct_answer': 'Se', 'explanation': 'Безличное se: se dice.'},
        ],
    },
    {
        'n': 64, 'level': 'C1', 'title': 'Сложная косвенная речь',
        'theory': (
            'При передаче в прошлом сдвигаются времена и наклонения:\n'
            '• presente → imperfecto: «Vengo» → Dijo que venía.\n'
            '• futuro → condicional: «Vendré» → Dijo que vendría.\n'
            '• imperativo → imperfecto de subjuntivo: «¡Ven!» → Me dijo que viniera.\n'
            '• perfecto/indefinido → pluscuamperfecto: «He llegado» → Dijo que había llegado.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': '«Ven aquí» → Me dijo que ___ allí.',
             'options': ['vengo', 'viniera', 'vendría'], 'correct_answer': 'viniera', 'explanation': 'Приказ → imperfecto de subjuntivo: viniera.'},
            {'exercise_type': 'multiple_choice', 'prompt': '«Vendré» → Dijo que ___.',
             'options': ['viene', 'vendría', 'vino'], 'correct_answer': 'vendría', 'explanation': 'futuro → condicional: vendría.'},
            {'exercise_type': 'multiple_choice', 'prompt': '«Estoy cansado» → Dijo que ___ cansado.',
             'options': ['está', 'estaba', 'estaría'], 'correct_answer': 'estaba', 'explanation': 'presente → imperfecto: estaba.'},
            {'exercise_type': 'multiple_choice', 'prompt': '«He terminado» → Dijo que ___ terminado.',
             'options': ['ha', 'había', 'habría'], 'correct_answer': 'había', 'explanation': 'perfecto → pluscuamperfecto: había.'},
        ],
    },
    {
        'n': 65, 'level': 'C1', 'title': 'Subjuntivo в определительных придаточных',
        'theory': (
            'Наклонение в определительном придаточном зависит от того, известен ли антецедент:\n'
            '• известный/реальный → indicativo: Tengo un amigo que habla ruso.\n'
            '• неизвестный/искомый → subjuntivo: Busco un amigo que hable ruso.\n'
            '• отрицаемый → subjuntivo: No hay nadie que sepa la respuesta.\n\n'
            'Также после «el que + subjuntivo» в значении «кто бы ни»: El que quiera, que venga.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Busco una casa que ___ (tener) jardín.',
             'options': ['tiene', 'tenga', 'tendrá'], 'correct_answer': 'tenga', 'explanation': 'Неизвестный объект → subjuntivo: tenga.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Tengo un vecino que ___ (hablar) chino.',
             'options': ['hable', 'habla', 'hablara'], 'correct_answer': 'habla', 'explanation': 'Реальный → indicativo: habla.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'No conozco a nadie que ___ (saber) eso.',
             'options': ['sabe', 'sepa', 'sabrá'], 'correct_answer': 'sepa', 'explanation': 'Отрицание существования → subjuntivo: sepa.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El que ___ (querer) venir, que venga.',
             'options': ['quiere', 'quiera', 'querrá'], 'correct_answer': 'quiera', 'explanation': '«Кто бы ни» → subjuntivo: quiera.'},
        ],
    },
    {
        'n': 66, 'level': 'C1', 'title': 'Сложные уступительные конструкции',
        'theory': (
            'Уступка («хотя / несмотря на»):\n'
            '• aunque + indicativo (факт) / + subjuntivo (гипотеза или уступка признанному): '
            'Aunque llueve, salgo. Aunque llueva, saldré.\n'
            '• por más que / por mucho que + subjuntivo: Por más que lo intente, no puedo.\n'
            '• a pesar de que, aun cuando: A pesar de que sea difícil, lo haré.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Aunque ___ (llover) mañana, iré. (гипотеза)',
             'options': ['llueve', 'llueva', 'lloverá'], 'correct_answer': 'llueva', 'explanation': 'Гипотеза → subjuntivo: llueva.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Por más que lo ___ (intentar), no lo logro.',
             'options': ['intento', 'intente', 'intentaré'], 'correct_answer': 'intente', 'explanation': 'por más que → subjuntivo: intente.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Aunque ___ (hacer) frío, salgo a correr. (факт)',
             'options': ['hace', 'haga', 'hará'], 'correct_answer': 'hace', 'explanation': 'Признанный факт → indicativo: hace.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'A pesar de que ___ (ser) tarde, seguimos. (уступка)',
             'options': ['es', 'sea', 'será'], 'correct_answer': 'sea', 'explanation': 'Уступка гипотезе → subjuntivo: sea.'},
        ],
    },
    {
        'n': 67, 'level': 'C1', 'title': 'Формальные коннекторы дискурса',
        'theory': (
            'Связки для письменной и официальной речи:\n'
            '• противопоставление: sin embargo, no obstante, ahora bien.\n'
            '• следствие: por consiguiente, por (lo) tanto, así pues.\n'
            '• причина: dado que, puesto que, ya que.\n'
            '• тема/добавление: en cuanto a, cabe destacar, asimismo, además.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'El plan es bueno; ___, tiene riesgos. (однако)',
             'options': ['por tanto', 'no obstante', 'dado que'], 'correct_answer': 'no obstante', 'explanation': 'Противопоставление → no obstante.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Llovió mucho; ___, se canceló el evento. (поэтому)',
             'options': ['sin embargo', 'por consiguiente', 'en cuanto a'], 'correct_answer': 'por consiguiente', 'explanation': 'Следствие → por consiguiente.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ que no hay fondos, aplazamos el proyecto. (поскольку)',
             'options': ['Dado', 'Aunque', 'Sino'], 'correct_answer': 'Dado', 'explanation': 'Причина → dado que.'},
            {'exercise_type': 'multiple_choice', 'prompt': '___ al presupuesto, hablaremos mañana. (что касается)',
             'options': ['Sin embargo', 'En cuanto', 'Por tanto'], 'correct_answer': 'En cuanto', 'explanation': 'Тема → en cuanto a.'},
        ],
    },
    {
        'n': 68, 'level': 'C1', 'title': 'Глаголы становления',
        'theory': (
            'Русское «стать» передаётся разными глаголами:\n'
            '• ponerse + прилагательное — быстрое (эмоц./физич.) изменение: Se puso rojo.\n'
            '• volverse + прилагательное — резкая/стойкая перемена: Se volvió muy serio.\n'
            '• hacerse — постепенно/усилием (профессия, идеология): Se hizo médico.\n'
            '• llegar a ser — достижение через путь: Llegó a ser director.\n'
            '• quedarse + прилагательное — результат/состояние: Se quedó sordo.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Al oír la noticia, ___ pálido. (быстро)',
             'options': ['se hizo', 'se puso', 'llegó a ser'], 'correct_answer': 'se puso', 'explanation': 'Быстрая перемена → ponerse.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Estudió mucho y ___ médico. (усилием)',
             'options': ['se puso', 'se hizo', 'se quedó'], 'correct_answer': 'se hizo', 'explanation': 'Профессия усилием → hacerse.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Con los años ___ director de la empresa. (достижение)',
             'options': ['se puso', 'llegó a ser', 'se quedó'], 'correct_answer': 'llegó a ser', 'explanation': 'Достижение → llegar a ser.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Tras el accidente ___ sordo. (результат)',
             'options': ['se hizo', 'se quedó', 'se puso'], 'correct_answer': 'se quedó', 'explanation': 'Результат-состояние → quedarse.'},
        ],
    },
    {
        'n': 69, 'level': 'C1', 'title': 'Орфографические замены при спряжении',
        'theory': (
            'Чтобы сохранить звук, буквы меняются:\n'
            '• -car → qu перед e: buscar → busqué; -gar → gu: llegar → llegué; -zar → c: empezar → empecé.\n'
            '• -cer/-cir → z перед a/o: vencer → venzo; -ger/-gir → j: proteger → protejo, dirigir → dirijo.\n\n'
            'Это чисто орфография — произношение сохраняется.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer yo ___ (buscar) las llaves.',
             'options': ['busqué', 'buscé', 'buské'], 'correct_answer': 'busqué', 'explanation': '-car → qu перед e: busqué.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer yo ___ (llegar) tarde.',
             'options': ['llegé', 'llegué', 'yegué'], 'correct_answer': 'llegué', 'explanation': '-gar → gu: llegué.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Yo ___ (proteger) a mi familia. (presente)',
             'options': ['protego', 'protejo', 'proteco'], 'correct_answer': 'protejo', 'explanation': '-ger → j перед o: protejo.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Ayer yo ___ (empezar) el curso.',
             'options': ['empezé', 'empecé', 'empezí'], 'correct_answer': 'empecé', 'explanation': '-zar → c: empecé.'},
        ],
    },
    {
        'n': 70, 'level': 'C1', 'title': 'Управление глаголов предлогами (I): con, en',
        'theory': (
            'Предлог — часть значения глагола, менять его нельзя:\n'
            '• contar con — рассчитывать на: Cuento con tu ayuda.\n'
            '• soñar con — мечтать о: Sueña con viajar.\n'
            '• casarse con — жениться на; quedar con — договориться встретиться.\n'
            '• pensar en — думать о; insistir en — настаивать на; consistir en — состоять в.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Cuento ___ tu apoyo.',
             'options': ['en', 'con', 'de'], 'correct_answer': 'con', 'explanation': 'contar con.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Sueña ___ ser actor.',
             'options': ['con', 'de', 'en'], 'correct_answer': 'con', 'explanation': 'soñar con.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Siempre pienso ___ ti.',
             'options': ['de', 'en', 'con'], 'correct_answer': 'en', 'explanation': 'pensar en.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Insiste ___ pagar él.',
             'options': ['en', 'de', 'con'], 'correct_answer': 'en', 'explanation': 'insistir en.'},
        ],
    },
    {
        'n': 71, 'level': 'C1', 'title': 'Управление глаголов предлогами (II): de, a',
        'theory': (
            'Предлог de:\n'
            '• depender de — зависеть от; acordarse de — помнить о; quejarse de — жаловаться на; '
            'darse cuenta de — осознавать; tratar de — пытаться.\n\n'
            'Предлог a:\n'
            '• atreverse a — осмеливаться; negarse a — отказываться; aprender a — учиться; '
            'empezar a — начинать.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Todo depende ___ ti.',
             'options': ['de', 'en', 'a'], 'correct_answer': 'de', 'explanation': 'depender de.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Me di cuenta ___ mi error.',
             'options': ['en', 'de', 'a'], 'correct_answer': 'de', 'explanation': 'darse cuenta de.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'No se atreve ___ hablar.',
             'options': ['de', 'a', 'en'], 'correct_answer': 'a', 'explanation': 'atreverse a.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Empezó ___ llover.',
             'options': ['de', 'a', 'con'], 'correct_answer': 'a', 'explanation': 'empezar a.'},
        ],
    },
    {
        'n': 72, 'level': 'C1', 'title': 'Ser и estar: продвинутые нюансы',
        'theory': (
            'С рядом прилагательных выбор ser/estar меняет смысл:\n'
            '• ser listo (умный) / estar listo (готов)\n'
            '• ser rico (богатый) / estar rico (вкусный)\n'
            '• ser aburrido (скучный) / estar aburrido (скучающий)\n'
            '• ser vivo (бойкий) / estar vivo (живой)\n\n'
            'ser — о событиях (La fiesta es en mi casa), estar — о местоположении предметов '
            '(Las llaves están en la mesa).'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'La sopa ___ muy rica. (вкусная)',
             'options': ['es', 'está', 'hay'], 'correct_answer': 'está', 'explanation': 'estar rico — вкусный.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Este libro ___ aburrido. (скучный по сути)',
             'options': ['es', 'está', 'hay'], 'correct_answer': 'es', 'explanation': 'ser aburrido — скучный.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'La conferencia ___ en el aula 5. (событие)',
             'options': ['es', 'está', 'hay'], 'correct_answer': 'es', 'explanation': 'Событие → ser: es en el aula 5.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Las llaves ___ en la mesa. (местоположение)',
             'options': ['son', 'están', 'hay'], 'correct_answer': 'están', 'explanation': 'Местоположение предмета → estar.'},
        ],
    },
    {
        'n': 73, 'level': 'C1', 'title': 'Estar para vs estar por',
        'theory': (
            'Обе конструкции с estar, но смысл разный:\n'
            '• estar para + инфинитив — готовность/вот-вот: Estoy para salir. El tren está para llegar.\n'
            '• estar por + инфинитив — склонность/колебание или «ещё не сделано»: '
            'Estoy por llamarlo. La carta está por escribir.'
        ),
        'exercises': [
            {'exercise_type': 'multiple_choice', 'prompt': 'Ya estoy ___ salir, dame un minuto.',
             'options': ['para', 'por', 'de'], 'correct_answer': 'para', 'explanation': 'Готовность вот-вот → estar para.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'Estoy ___ llamarlo, aún lo dudo.',
             'options': ['para', 'por', 'a'], 'correct_answer': 'por', 'explanation': 'Колебание/склонность → estar por.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'La cena está ___ preparar todavía. (ещё не сделано)',
             'options': ['para', 'por', 'en'], 'correct_answer': 'por', 'explanation': '«Ещё не сделано» → estar por.'},
            {'exercise_type': 'multiple_choice', 'prompt': 'El avión está ___ despegar.',
             'options': ['para', 'por', 'de'], 'correct_answer': 'para', 'explanation': 'Вот-вот произойдёт → estar para.'},
        ],
    },
]
