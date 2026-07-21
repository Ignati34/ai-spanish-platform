# -*- coding: utf-8 -*-
"""Voice-tutor role-play scenarios, 4 per CEFR level (A1→C2), graded simple→complex.

Each entry has a localized label and a Spanish `prompt` that tells the AI who to be and
what the situation is; the tutor speaks Spanish at the chosen level. Original content.
"""

VOICE_SCENARIOS = [
    # -------- A1 --------
    {'id': 'a1_cafe', 'level': 'A1', 'prompt': 'Eres camarero en una cafetería. El estudiante pide algo de beber y comer.',
     'label': {'es': 'En la cafetería', 'ru': 'В кафе', 'uk': 'У кафе', 'ar': 'في المقهى', 'fr': 'Au café', 'en': 'At the café'}},
    {'id': 'a1_presentarse', 'level': 'A1', 'prompt': 'Conoces al estudiante por primera vez. Preséntate y pregúntale su nombre, de dónde es y qué hace.',
     'label': {'es': 'Presentarse', 'ru': 'Знакомство', 'uk': 'Знайомство', 'ar': 'التعارف', 'fr': 'Se présenter', 'en': 'Introductions'}},
    {'id': 'a1_tienda', 'level': 'A1', 'prompt': 'Eres dependiente de una tienda pequeña. El estudiante compra fruta y pan.',
     'label': {'es': 'En la tienda', 'ru': 'В магазине', 'uk': 'У магазині', 'ar': 'في المتجر', 'fr': 'Au magasin', 'en': 'At the shop'}},
    {'id': 'a1_direcciones', 'level': 'A1', 'prompt': 'Eres un vecino amable. El estudiante te pregunta cómo llegar a la estación.',
     'label': {'es': 'Pedir direcciones', 'ru': 'Спросить дорогу', 'uk': 'Запитати дорогу', 'ar': 'السؤال عن الطريق', 'fr': 'Demander son chemin', 'en': 'Asking directions'}},
    # -------- A2 --------
    {'id': 'a2_restaurante', 'level': 'A2', 'prompt': 'Eres camarero en un restaurante. El estudiante pide el menú, comida y bebida, y luego la cuenta.',
     'label': {'es': 'En el restaurante', 'ru': 'В ресторане', 'uk': 'У ресторані', 'ar': 'في المطعم', 'fr': 'Au restaurant', 'en': 'At the restaurant'}},
    {'id': 'a2_hotel', 'level': 'A2', 'prompt': 'Eres recepcionista de un hotel. El estudiante quiere reservar una habitación para dos noches.',
     'label': {'es': 'Reservar hotel', 'ru': 'Бронь отеля', 'uk': 'Бронювання готелю', 'ar': 'حجز فندق', 'fr': 'Réserver un hôtel', 'en': 'Booking a hotel'}},
    {'id': 'a2_farmacia', 'level': 'A2', 'prompt': 'Eres farmacéutico. El estudiante no se encuentra bien y describe sus síntomas.',
     'label': {'es': 'En la farmacia', 'ru': 'В аптеке', 'uk': 'В аптеці', 'ar': 'في الصيدلية', 'fr': 'À la pharmacie', 'en': 'At the pharmacy'}},
    {'id': 'a2_tren', 'level': 'A2', 'prompt': 'Eres taquillero en una estación. El estudiante compra un billete de tren y pregunta horarios.',
     'label': {'es': 'Comprar un billete', 'ru': 'Купить билет', 'uk': 'Купити квиток', 'ar': 'شراء تذكرة', 'fr': 'Acheter un billet', 'en': 'Buying a ticket'}},
    # -------- B1 --------
    {'id': 'b1_piso', 'level': 'B1', 'prompt': 'Eres el propietario de un piso en alquiler. El estudiante te llama para pedir información y concertar una visita.',
     'label': {'es': 'Alquilar un piso', 'ru': 'Аренда квартиры', 'uk': 'Оренда квартири', 'ar': 'استئجار شقة', 'fr': 'Louer un appartement', 'en': 'Renting a flat'}},
    {'id': 'b1_medico', 'level': 'B1', 'prompt': 'Eres médico de cabecera. El estudiante te cuenta un problema de salud y tú le haces preguntas y le aconsejas.',
     'label': {'es': 'En la consulta', 'ru': 'На приёме у врача', 'uk': 'На прийомі лікаря', 'ar': 'في العيادة', 'fr': 'Chez le médecin', 'en': 'At the clinic'}},
    {'id': 'b1_devolucion', 'level': 'B1', 'prompt': 'Eres dependiente de una tienda. El estudiante quiere devolver un producto defectuoso sin ticket.',
     'label': {'es': 'Devolver un producto', 'ru': 'Вернуть товар', 'uk': 'Повернути товар', 'ar': 'إرجاع منتج', 'fr': 'Rendre un produit', 'en': 'Returning an item'}},
    {'id': 'b1_planes', 'level': 'B1', 'prompt': 'Eres un amigo del estudiante. Estáis organizando un viaje de fin de semana y debéis poneros de acuerdo.',
     'label': {'es': 'Planear un viaje', 'ru': 'Планы на поездку', 'uk': 'Плани на подорож', 'ar': 'التخطيط لرحلة', 'fr': 'Planifier un voyage', 'en': 'Planning a trip'}},
    # -------- B2 --------
    {'id': 'b2_reclamacion', 'level': 'B2', 'prompt': 'Eres empleado de atención al cliente. El estudiante presenta una reclamación por un servicio que no cumplió lo prometido.',
     'label': {'es': 'Una reclamación', 'ru': 'Жалоба/претензия', 'uk': 'Скарга', 'ar': 'شكوى', 'fr': 'Une réclamation', 'en': 'A complaint'}},
    {'id': 'b2_negociar', 'level': 'B2', 'prompt': 'Eres vendedor en un mercado de segunda mano. El estudiante quiere negociar el precio de un objeto.',
     'label': {'es': 'Negociar un precio', 'ru': 'Торговаться о цене', 'uk': 'Торгуватися', 'ar': 'التفاوض على السعر', 'fr': 'Négocier un prix', 'en': 'Haggling a price'}},
    {'id': 'b2_entrevista', 'level': 'B2', 'prompt': 'Eres responsable de recursos humanos en una entrevista de trabajo. Haz preguntas sobre la experiencia y las motivaciones del estudiante.',
     'label': {'es': 'Entrevista de trabajo', 'ru': 'Собеседование', 'uk': 'Співбесіда', 'ar': 'مقابلة عمل', 'fr': "Entretien d'embauche", 'en': 'Job interview'}},
    {'id': 'b2_agencia', 'level': 'B2', 'prompt': 'Eres agente de viajes. El estudiante quiere organizar unas vacaciones con un presupuesto limitado y varias condiciones.',
     'label': {'es': 'En la agencia de viajes', 'ru': 'В турагентстве', 'uk': 'У турагенції', 'ar': 'في وكالة السفر', 'fr': "À l'agence de voyages", 'en': 'At the travel agency'}},
    # -------- C1 --------
    {'id': 'c1_debate', 'level': 'C1', 'prompt': 'Eres un interlocutor con opiniones firmes. Debatid sobre el teletrabajo; defiende una postura y pide argumentos al estudiante.',
     'label': {'es': 'Debate de opinión', 'ru': 'Дискуссия-мнение', 'uk': 'Дискусія', 'ar': 'نقاش رأي', 'fr': "Débat d'opinion", 'en': 'Opinion debate'}},
    {'id': 'c1_reunion', 'level': 'C1', 'prompt': 'Eres un colega en una reunión de trabajo. Discutid cómo repartir tareas de un proyecto con plazos ajustados.',
     'label': {'es': 'Reunión de trabajo', 'ru': 'Рабочая встреча', 'uk': 'Робоча нарада', 'ar': 'اجتماع عمل', 'fr': 'Réunion de travail', 'en': 'Work meeting'}},
    {'id': 'c1_queja_formal', 'level': 'C1', 'prompt': 'Eres el gerente de un hotel. El estudiante presenta una queja formal y espera una solución y una disculpa.',
     'label': {'es': 'Queja formal', 'ru': 'Официальная жалоба', 'uk': 'Офіційна скарга', 'ar': 'شكوى رسمية', 'fr': 'Réclamation formelle', 'en': 'Formal complaint'}},
    {'id': 'c1_banco', 'level': 'C1', 'prompt': 'Eres asesor bancario. El estudiante quiere entender las condiciones de un préstamo y hace preguntas detalladas.',
     'label': {'es': 'Asesoría bancaria', 'ru': 'Консультация в банке', 'uk': 'Консультація в банку', 'ar': 'استشارة مصرفية', 'fr': 'Conseil bancaire', 'en': 'Bank advice'}},
    # -------- C2 --------
    {'id': 'c2_negociacion', 'level': 'C2', 'prompt': 'Eres un socio comercial en una negociación compleja. Defiende los intereses de tu empresa con matices y contrapropuestas.',
     'label': {'es': 'Negociación compleja', 'ru': 'Сложные переговоры', 'uk': 'Складні перемовини', 'ar': 'تفاوض معقّد', 'fr': 'Négociation complexe', 'en': 'Complex negotiation'}},
    {'id': 'c2_mediacion', 'level': 'C2', 'prompt': 'Eres mediador en un conflicto entre dos partes. Ayuda al estudiante a exponer su postura y busca un acuerdo.',
     'label': {'es': 'Mediar un conflicto', 'ru': 'Медиация конфликта', 'uk': 'Медіація конфлікту', 'ar': 'الوساطة في نزاع', 'fr': 'Médiation de conflit', 'en': 'Conflict mediation'}},
    {'id': 'c2_entrevista_dir', 'level': 'C2', 'prompt': 'Eres un periodista que entrevista al estudiante como si fuera un experto. Haz preguntas incisivas y de seguimiento.',
     'label': {'es': 'Entrevista periodística', 'ru': 'Интервью для прессы', 'uk': 'Інтервʼю для преси', 'ar': 'مقابلة صحفية', 'fr': 'Interview de presse', 'en': 'Press interview'}},
    {'id': 'c2_academico', 'level': 'C2', 'prompt': 'Eres un profesor universitario. Discutid con matices un tema abstracto (por ejemplo, la libertad y la tecnología).',
     'label': {'es': 'Debate académico', 'ru': 'Академический спор', 'uk': 'Академічна дискусія', 'ar': 'نقاش أكاديمي', 'fr': 'Débat académique', 'en': 'Academic debate'}},
]

_BY_LEVEL: dict[str, list[dict]] = {}
for _s in VOICE_SCENARIOS:
    _BY_LEVEL.setdefault(_s['level'], []).append(_s)


def public_list(level: str | None = None, native_language: str = 'ru') -> list[dict]:
    lang = (native_language or 'ru')[:2].lower()
    items = _BY_LEVEL.get((level or '').upper(), []) if level else VOICE_SCENARIOS
    return [{
        'id': s['id'], 'level': s['level'], 'prompt': s['prompt'],
        'label': s['label'].get(lang) or s['label']['en'],
    } for s in items]
