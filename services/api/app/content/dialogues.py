# -*- coding: utf-8 -*-
"""Built-in reading dialogues, graded A1→C2 (simple to complex).

Each dialogue is original, license-clean. Lines carry the Spanish (the practice content)
plus a Russian reference gloss; the custom generator produces translations in the learner's
own language. Titles are localized like the simulation scenarios.
"""

DIALOGUES = [
    # ---------------- A1 ----------------
    {
        'id': 'a1_saludos', 'level': 'A1',
        'title': {'es': 'Saludos', 'ru': 'Приветствие', 'uk': 'Привітання', 'ar': 'تحيات', 'fr': 'Salutations', 'en': 'Greetings'},
        'lines': [
            {'speaker': 'Ana', 'es': '¡Hola! ¿Cómo te llamas?', 'ru': 'Привет! Как тебя зовут?'},
            {'speaker': 'Luis', 'es': 'Me llamo Luis. ¿Y tú?', 'ru': 'Меня зовут Луис. А тебя?'},
            {'speaker': 'Ana', 'es': 'Ana. ¿De dónde eres?', 'ru': 'Ана. Откуда ты?'},
            {'speaker': 'Luis', 'es': 'Soy de México. ¿Y tú?', 'ru': 'Я из Мексики. А ты?'},
            {'speaker': 'Ana', 'es': 'Yo soy de España. ¡Mucho gusto!', 'ru': 'Я из Испании. Очень приятно!'},
        ],
    },
    {
        'id': 'a1_cafe', 'level': 'A1',
        'title': {'es': 'En la cafetería', 'ru': 'В кафе', 'uk': 'У кафе', 'ar': 'في المقهى', 'fr': 'Au café', 'en': 'At the café'},
        'lines': [
            {'speaker': 'Camarero', 'es': 'Buenos días, ¿qué desea?', 'ru': 'Доброе утро, что желаете?'},
            {'speaker': 'Cliente', 'es': 'Un café con leche, por favor.', 'ru': 'Кофе с молоком, пожалуйста.'},
            {'speaker': 'Camarero', 'es': '¿Algo más?', 'ru': 'Что-нибудь ещё?'},
            {'speaker': 'Cliente', 'es': 'Sí, un croissant. ¿Cuánto es?', 'ru': 'Да, круассан. Сколько с меня?'},
            {'speaker': 'Camarero', 'es': 'Tres euros, por favor.', 'ru': 'Три евро, пожалуйста.'},
        ],
    },
    # ---------------- A2 ----------------
    {
        'id': 'a2_planes', 'level': 'A2',
        'title': {'es': 'Planes para el finde', 'ru': 'Планы на выходные', 'uk': 'Плани на вихідні', 'ar': 'خطط نهاية الأسبوع', 'fr': 'Plans du week-end', 'en': 'Weekend plans'},
        'lines': [
            {'speaker': 'Marta', 'es': '¿Qué vas a hacer este fin de semana?', 'ru': 'Что будешь делать в эти выходные?'},
            {'speaker': 'Diego', 'es': 'Voy a ir a la playa con mi hermano.', 'ru': 'Поеду на пляж с братом.'},
            {'speaker': 'Marta', 'es': '¡Qué bien! ¿A qué hora salís?', 'ru': 'Здорово! Во сколько выезжаете?'},
            {'speaker': 'Diego', 'es': 'Temprano, sobre las ocho. ¿Quieres venir?', 'ru': 'Рано, около восьми. Хочешь с нами?'},
            {'speaker': 'Marta', 'es': 'Me encantaría, pero tengo que estudiar.', 'ru': 'С удовольствием, но мне надо заниматься.'},
        ],
    },
    {
        'id': 'a2_tienda', 'level': 'A2',
        'title': {'es': 'En la tienda de ropa', 'ru': 'В магазине одежды', 'uk': 'У магазині одягу', 'ar': 'في متجر الملابس', 'fr': 'Au magasin de vêtements', 'en': 'At the clothes shop'},
        'lines': [
            {'speaker': 'Dependienta', 'es': '¿Puedo ayudarle en algo?', 'ru': 'Могу вам чем-то помочь?'},
            {'speaker': 'Cliente', 'es': 'Sí, busco una camisa azul.', 'ru': 'Да, ищу синюю рубашку.'},
            {'speaker': 'Dependienta', 'es': '¿Qué talla usa?', 'ru': 'Какой у вас размер?'},
            {'speaker': 'Cliente', 'es': 'La mediana. ¿Puedo probármela?', 'ru': 'Средний. Можно примерить?'},
            {'speaker': 'Dependienta', 'es': 'Claro, el probador está al fondo.', 'ru': 'Конечно, примерочная в глубине зала.'},
        ],
    },
    # ---------------- B1 ----------------
    {
        'id': 'b1_alquiler', 'level': 'B1',
        'title': {'es': 'Buscando piso', 'ru': 'Поиск квартиры', 'uk': 'Пошук квартири', 'ar': 'البحث عن شقة', 'fr': 'Chercher un appartement', 'en': 'Flat hunting'},
        'lines': [
            {'speaker': 'Inquilino', 'es': 'Buenas, llamo por el piso que se alquila.', 'ru': 'Здравствуйте, звоню по поводу сдающейся квартиры.'},
            {'speaker': 'Casero', 'es': 'Perfecto. Está disponible desde el mes que viene.', 'ru': 'Отлично. Она свободна со следующего месяца.'},
            {'speaker': 'Inquilino', 'es': '¿Los gastos de comunidad están incluidos?', 'ru': 'Коммунальные платежи включены?'},
            {'speaker': 'Casero', 'es': 'El agua sí, pero la luz va aparte.', 'ru': 'Вода — да, а электричество отдельно.'},
            {'speaker': 'Inquilino', 'es': '¿Podría verlo esta semana sin compromiso?', 'ru': 'Можно посмотреть на этой неделе, ни к чему не обязываясь?'},
            {'speaker': 'Casero', 'es': 'Por supuesto, quedamos el jueves por la tarde.', 'ru': 'Разумеется, договоримся на четверг во второй половине дня.'},
        ],
    },
    {
        'id': 'b1_medico', 'level': 'B1',
        'title': {'es': 'En la consulta', 'ru': 'На приёме у врача', 'uk': 'На прийомі в лікаря', 'ar': 'في العيادة', 'fr': 'Chez le médecin', 'en': 'At the clinic'},
        'lines': [
            {'speaker': 'Médica', 'es': '¿Qué le trae por aquí?', 'ru': 'Что вас привело?'},
            {'speaker': 'Paciente', 'es': 'Llevo dos días con dolor de garganta y fiebre.', 'ru': 'Уже два дня болит горло и температура.'},
            {'speaker': 'Médica', 'es': '¿Le duele al tragar?', 'ru': 'Больно глотать?'},
            {'speaker': 'Paciente', 'es': 'Sí, bastante, y me cuesta dormir.', 'ru': 'Да, довольно сильно, и трудно спать.'},
            {'speaker': 'Médica', 'es': 'Le recetaré algo. Si no mejora, vuelva el lunes.', 'ru': 'Выпишу вам кое-что. Если не станет лучше, приходите в понедельник.'},
        ],
    },
    # ---------------- B2 ----------------
    {
        'id': 'b2_trabajo', 'level': 'B2',
        'title': {'es': 'Malentendido en el trabajo', 'ru': 'Недопонимание на работе', 'uk': 'Непорозуміння на роботі', 'ar': 'سوء تفاهم في العمل', 'fr': 'Malentendu au travail', 'en': 'A mix-up at work'},
        'lines': [
            {'speaker': 'Jefe', 'es': 'Contaba con el informe para hoy. ¿Qué ha pasado?', 'ru': 'Я рассчитывал на отчёт к сегодняшнему дню. Что случилось?'},
            {'speaker': 'Empleado', 'es': 'Disculpe, entendí que el plazo era el viernes.', 'ru': 'Извините, я понял, что срок — пятница.'},
            {'speaker': 'Jefe', 'es': 'Ya veo. Quizá no me expliqué con claridad.', 'ru': 'Понятно. Возможно, я не объяснил ясно.'},
            {'speaker': 'Empleado', 'es': 'De todos modos, puedo tenerlo listo en dos horas.', 'ru': 'В любом случае, я могу подготовить его за два часа.'},
            {'speaker': 'Jefe', 'es': 'Te lo agradezco. Avísame en cuanto lo termines.', 'ru': 'Буду признателен. Дай знать, как закончишь.'},
        ],
    },
    {
        'id': 'b2_viaje', 'level': 'B2',
        'title': {'es': 'Un vuelo cancelado', 'ru': 'Отменённый рейс', 'uk': 'Скасований рейс', 'ar': 'رحلة ملغاة', 'fr': 'Un vol annulé', 'en': 'A cancelled flight'},
        'lines': [
            {'speaker': 'Pasajero', 'es': 'Me acaban de decir que mi vuelo está cancelado.', 'ru': 'Мне только что сказали, что мой рейс отменён.'},
            {'speaker': 'Agente', 'es': 'Lo lamento. Puedo reubicarle en el de las seis.', 'ru': 'Сожалею. Могу пересадить вас на рейс в шесть.'},
            {'speaker': 'Pasajero', 'es': 'Es que perdería la conexión en Madrid.', 'ru': 'Дело в том, что я потеряю стыковку в Мадриде.'},
            {'speaker': 'Agente', 'es': 'En ese caso, le buscaré una ruta alternativa.', 'ru': 'В таком случае найду вам альтернативный маршрут.'},
            {'speaker': 'Pasajero', 'es': '¿Tendría derecho a alguna compensación?', 'ru': 'Мне полагается какая-то компенсация?'},
            {'speaker': 'Agente', 'es': 'Sí, le entrego el formulario ahora mismo.', 'ru': 'Да, сейчас же выдам вам бланк.'},
        ],
    },
    # ---------------- C1 ----------------
    {
        'id': 'c1_debate', 'level': 'C1',
        'title': {'es': 'Debate sobre el teletrabajo', 'ru': 'Спор об удалёнке', 'uk': 'Дискусія про віддалену роботу', 'ar': 'نقاش حول العمل عن بُعد', 'fr': 'Débat sur le télétravail', 'en': 'Debating remote work'},
        'lines': [
            {'speaker': 'Elena', 'es': 'Sostengo que el teletrabajo mejora la productividad.', 'ru': 'Я утверждаю, что удалёнка повышает продуктивность.'},
            {'speaker': 'Raúl', 'es': 'Hasta cierto punto; también diluye el trabajo en equipo.', 'ru': 'До определённой степени; она к тому же размывает командную работу.'},
            {'speaker': 'Elena', 'es': 'Siempre que haya reuniones periódicas, no tiene por qué.', 'ru': 'При условии регулярных встреч — вовсе не обязательно.'},
            {'speaker': 'Raúl', 'es': 'Reconozco que depende de cómo se gestione.', 'ru': 'Признаю, что всё зависит от того, как этим управлять.'},
            {'speaker': 'Elena', 'es': 'Exacto: el problema no es el modelo, sino su aplicación.', 'ru': 'Именно: проблема не в модели, а в её применении.'},
        ],
    },
    {
        'id': 'c1_queja', 'level': 'C1',
        'title': {'es': 'Una reclamación formal', 'ru': 'Официальная жалоба', 'uk': 'Офіційна скарга', 'ar': 'شكوى رسمية', 'fr': 'Une réclamation formelle', 'en': 'A formal complaint'},
        'lines': [
            {'speaker': 'Cliente', 'es': 'Quisiera dejar constancia de mi descontento con el servicio.', 'ru': 'Я хотел бы зафиксировать своё недовольство обслуживанием.'},
            {'speaker': 'Gerente', 'es': 'Le escucho. Lamento que no haya cumplido sus expectativas.', 'ru': 'Слушаю вас. Сожалею, что оно не оправдало ваших ожиданий.'},
            {'speaker': 'Cliente', 'es': 'Se me prometió una reparación que nunca llegó a realizarse.', 'ru': 'Мне обещали ремонт, который так и не был выполнен.'},
            {'speaker': 'Gerente', 'es': 'Asumo la responsabilidad y le propongo una solución inmediata.', 'ru': 'Беру на себя ответственность и предлагаю немедленное решение.'},
            {'speaker': 'Cliente', 'es': 'Le agradecería que lo pusiera por escrito.', 'ru': 'Буду признателен, если вы оформите это письменно.'},
        ],
    },
    # ---------------- C2 ----------------
    {
        'id': 'c2_matiz', 'level': 'C2',
        'title': {'es': 'Matices de una negociación', 'ru': 'Нюансы переговоров', 'uk': 'Нюанси переговорів', 'ar': 'دقائق التفاوض', 'fr': "Nuances d'une négociation", 'en': 'Negotiation nuances'},
        'lines': [
            {'speaker': 'Socio A', 'es': 'No es que rechacemos la oferta, sino que la matizaríamos.', 'ru': 'Дело не в том, что мы отвергаем предложение, — мы бы его уточнили.'},
            {'speaker': 'Socio B', 'es': 'Entiendo la sutileza, pero necesitamos garantías tangibles.', 'ru': 'Понимаю тонкость, но нам нужны осязаемые гарантии.'},
            {'speaker': 'Socio A', 'es': 'Las habrá, siempre y cuando se respeten los plazos acordados.', 'ru': 'Они будут, при условии соблюдения оговорённых сроков.'},
            {'speaker': 'Socio B', 'es': 'De ser así, estaríamos dispuestos a reconsiderar el conjunto.', 'ru': 'Если так, мы были бы готовы пересмотреть пакет в целом.'},
            {'speaker': 'Socio A', 'es': 'Me alegra que hablemos ya el mismo idioma.', 'ru': 'Рад, что мы наконец говорим на одном языке.'},
        ],
    },
    {
        'id': 'c2_ironia', 'level': 'C2',
        'title': {'es': 'Ironía entre amigos', 'ru': 'Ирония между друзьями', 'uk': 'Іронія між друзями', 'ar': 'سخرية بين الأصدقاء', 'fr': 'Ironie entre amis', 'en': 'Irony among friends'},
        'lines': [
            {'speaker': 'Sofía', 'es': '¡Menudo madrugón! Solo son las doce del mediodía.', 'ru': 'Ну и ранняя пташка! Всего-то полдень.'},
            {'speaker': 'Pablo', 'es': 'Ya ves, es que me sobra el tiempo libre…', 'ru': 'Ну да, у меня же уйма свободного времени…'},
            {'speaker': 'Sofía', 'es': 'No me digas. Con lo ocupadísimo que estás siempre.', 'ru': 'Да что ты. При твоей вечной сверхзанятости.'},
            {'speaker': 'Pablo', 'es': 'Tú, en cambio, la puntualidad en persona.', 'ru': 'Зато ты — сама пунктуальность.'},
            {'speaker': 'Sofía', 'es': 'Toquemos otro tema, anda, que nos conocemos.', 'ru': 'Давай сменим тему, мы же друг друга знаем.'},
        ],
    },
]

_BY_LEVEL = {}
for _d in DIALOGUES:
    _BY_LEVEL.setdefault(_d['level'], []).append(_d)


def _title(d: dict, lang: str) -> str:
    t = d['title']
    return t.get((lang or 'ru')[:2].lower()) or t.get('en') or t['es']


def public_list(level: str | None = None, lang: str = 'ru') -> list[dict]:
    """Return built-in dialogues (optionally filtered by level), title localized."""
    items = _BY_LEVEL.get(level.upper(), []) if level else DIALOGUES
    out = []
    for d in items:
        out.append({
            'id': d['id'], 'level': d['level'], 'title': _title(d, lang),
            'lines': [{'speaker': l['speaker'], 'es': l['es'], 'translation': l['ru']} for l in d['lines']],
        })
    return out
