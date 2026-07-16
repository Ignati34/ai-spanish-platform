"""Original role-play scenarios (license-clean). Each is a mini-mission: the AI plays
a role, the learner must reach a goal, with hint phrases and a completion judgement.

Aligned with the brief's real-life situations (clinic, bank, interview, rental, town hall).
Titles/goals are localized; role/hints/setup are Spanish (that's the practice content).
"""

SCENARIOS = [
    {
        'id': 'doctor',
        'title': {'es': 'Cita médica', 'ru': 'Приём у врача', 'uk': 'Прийом у лікаря', 'ar': 'موعد طبي', 'fr': 'Rendez-vous médical', 'en': 'Doctor appointment'},
        'role': 'recepcionista de un centro de salud',
        'goal': {'es': 'Conseguir una cita para la próxima semana por la mañana',
                 'ru': 'Записаться на приём на следующей неделе утром',
                 'uk': 'Записатися на прийом наступного тижня вранці',
                 'ar': 'الحصول على موعد الأسبوع القادم صباحًا',
                 'fr': 'Obtenir un rendez-vous la semaine prochaine le matin',
                 'en': 'Get an appointment for next week in the morning'},
        'goal_es': 'El estudiante debe conseguir una cita médica para la próxima semana por la mañana (día y hora).',
        'setup_es': 'Llamas al centro de salud para pedir cita con tu médico de cabecera.',
        'hints': ['Buenos días, quería pedir una cita.', '¿Tiene algo para la próxima semana?', 'Por la mañana, si es posible.'],
    },
    {
        'id': 'bank',
        'title': {'es': 'Reclamar en el banco', 'ru': 'Спор в банке', 'uk': 'Суперечка в банку', 'ar': 'شكوى في البنك', 'fr': 'Réclamation à la banque', 'en': 'Bank complaint'},
        'role': 'empleado de atención al cliente de un banco',
        'goal': {'es': 'Reclamar una comisión cobrada por error y pedir su devolución',
                 'ru': 'Оспорить ошибочную комиссию и добиться возврата',
                 'uk': 'Оскаржити помилкову комісію та домогтися повернення',
                 'ar': 'الاعتراض على رسوم بالخطأ وطلب استردادها',
                 'fr': 'Contester des frais prélevés par erreur et demander un remboursement',
                 'en': 'Dispute a wrongly charged fee and get it refunded'},
        'goal_es': 'El estudiante debe explicar el problema y conseguir que el banco acepte devolver la comisión.',
        'setup_es': 'Vas al banco porque te han cobrado una comisión que no reconoces.',
        'hints': ['Me han cobrado una comisión que no reconozco.', '¿Podrían revisarlo, por favor?', 'Me gustaría que me la devolvieran.'],
    },
    {
        'id': 'interview',
        'title': {'es': 'Entrevista de trabajo', 'ru': 'Собеседование', 'uk': 'Співбесіда', 'ar': 'مقابلة عمل', 'fr': "Entretien d'embauche", 'en': 'Job interview'},
        'role': 'responsable de recursos humanos',
        'goal': {'es': 'Presentarte y explicar por qué eres buen candidato',
                 'ru': 'Представить себя и объяснить, почему вы хороший кандидат',
                 'uk': 'Представити себе і пояснити, чому ви хороший кандидат',
                 'ar': 'التعريف بنفسك وشرح لماذا أنت مرشح مناسب',
                 'fr': 'Te présenter et expliquer pourquoi tu es un bon candidat',
                 'en': 'Introduce yourself and explain why you are a good candidate'},
        'goal_es': 'El estudiante debe presentarse, hablar de su experiencia y dar al menos dos razones para ser contratado.',
        'setup_es': 'Tienes una entrevista para un puesto que te interesa.',
        'hints': ['Tengo experiencia en...', 'Mis puntos fuertes son...', 'Me interesa este puesto porque...'],
    },
    {
        'id': 'rental',
        'title': {'es': 'Alquilar un piso', 'ru': 'Аренда квартиры', 'uk': 'Оренда квартири', 'ar': 'استئجار شقة', 'fr': 'Louer un appartement', 'en': 'Rent a flat'},
        'role': 'propietario que alquila un piso',
        'goal': {'es': 'Preguntar por el piso y acordar una visita',
                 'ru': 'Расспросить о квартире и договориться о просмотре',
                 'uk': 'Розпитати про квартиру і домовитися про перегляд',
                 'ar': 'الاستفسار عن الشقة والاتفاق على معاينة',
                 'fr': 'Te renseigner sur l’appartement et convenir d’une visite',
                 'en': 'Ask about the flat and arrange a viewing'},
        'goal_es': 'El estudiante debe preguntar precio y condiciones y acordar día y hora para ver el piso.',
        'setup_es': 'Llamas por un anuncio de alquiler que te ha gustado.',
        'hints': ['Llamo por el anuncio del piso.', '¿Cuánto es el alquiler al mes?', '¿Podría verlo esta semana?'],
    },
    {
        'id': 'city_hall',
        'title': {'es': 'Empadronamiento', 'ru': 'Прописка (empadronamiento)', 'uk': 'Реєстрація (empadronamiento)', 'ar': 'التسجيل البلدي', 'fr': 'Inscription à la mairie', 'en': 'Town hall registration'},
        'role': 'funcionario del ayuntamiento',
        'goal': {'es': 'Pedir cita para empadronarte y saber qué documentos llevar',
                 'ru': 'Записаться на empadronamiento и узнать, какие документы нужны',
                 'uk': 'Записатися на empadronamiento і дізнатися, які документи потрібні',
                 'ar': 'حجز موعد للتسجيل ومعرفة الوثائق المطلوبة',
                 'fr': 'Prendre rendez-vous pour t’inscrire et savoir quels documents apporter',
                 'en': 'Book an appointment to register and learn which documents to bring'},
        'goal_es': 'El estudiante debe conseguir una cita para el padrón y una lista de los documentos necesarios.',
        'setup_es': 'Acabas de mudarte y necesitas empadronarte en el ayuntamiento.',
        'hints': ['Quería empadronarme.', '¿Qué documentos necesito?', '¿Me puede dar cita?'],
    },
]

_BY_ID = {s['id']: s for s in SCENARIOS}


def get(scenario_id: str) -> dict | None:
    return _BY_ID.get(scenario_id)


def public_list(native_language: str) -> list[dict]:
    lang = (native_language or 'ru')[:2]
    out = []
    for s in SCENARIOS:
        out.append({
            'id': s['id'],
            'title': s['title'].get(lang, s['title']['en']),
            'role': s['role'],
            'goal': s['goal'].get(lang, s['goal']['en']),
            'setup': s['setup_es'],
            'hints': s['hints'],
        })
    return out
