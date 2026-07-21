# -*- coding: utf-8 -*-
"""Built-in reading dialogues, graded A1→C2 (simple to complex).

Each dialogue is original, license-clean. Every line carries the Spanish (the practice
content) plus a reference gloss in each supported interface language (ru/uk/ar/fr/en),
pre-translated so a learner reads the dialogue in their own language with no AI call.
The custom generator still produces on-the-fly dialogues in the learner's language.
Titles are localized like the simulation scenarios.
"""

DIALOGUES = [

    {
        'id': 'a1_saludos', 'level': 'A1',
        'title': {'es': 'Saludos', 'ru': 'Приветствие', 'uk': 'Привітання', 'ar': 'تحيات', 'fr': 'Salutations', 'en': 'Greetings'},
        'lines': [
            {'speaker': 'Ana', 'es': '¡Hola! ¿Cómo te llamas?', 'ru': 'Привет! Как тебя зовут?', 'uk': 'Привіт! Як тебе звати?', 'ar': 'مرحبًا! ما اسمك؟', 'fr': "Salut ! Comment tu t'appelles ?", 'en': "Hi! What's your name?"},
            {'speaker': 'Luis', 'es': 'Me llamo Luis. ¿Y tú?', 'ru': 'Меня зовут Луис. А тебя?', 'uk': 'Мене звати Луїс. А тебе?', 'ar': 'اسمي لويس. وأنت؟', 'fr': "Je m'appelle Luis. Et toi ?", 'en': 'My name is Luis. And you?'},
            {'speaker': 'Ana', 'es': 'Ana. ¿De dónde eres?', 'ru': 'Ана. Откуда ты?', 'uk': 'Ана. Звідки ти?', 'ar': 'أنا. من أين أنت؟', 'fr': "Ana. D'où viens-tu ?", 'en': 'Ana. Where are you from?'},
            {'speaker': 'Luis', 'es': 'Soy de México. ¿Y tú?', 'ru': 'Я из Мексики. А ты?', 'uk': 'Я з Мексики. А ти?', 'ar': 'أنا من المكسيك. وأنت؟', 'fr': 'Je suis du Mexique. Et toi ?', 'en': "I'm from Mexico. And you?"},
            {'speaker': 'Ana', 'es': 'Yo soy de España. ¡Mucho gusto!', 'ru': 'Я из Испании. Очень приятно!', 'uk': 'Я з Іспанії. Дуже приємно!', 'ar': 'أنا من إسبانيا. تشرّفت!', 'fr': "Je suis d'Espagne. Enchantée !", 'en': "I'm from Spain. Nice to meet you!"},
        ],
    },
    {
        'id': 'a1_cafe', 'level': 'A1',
        'title': {'es': 'En la cafetería', 'ru': 'В кафе', 'uk': 'У кафе', 'ar': 'في المقهى', 'fr': 'Au café', 'en': 'At the café'},
        'lines': [
            {'speaker': 'Camarero', 'es': 'Buenos días, ¿qué desea?', 'ru': 'Доброе утро, что желаете?', 'uk': 'Доброго ранку, що бажаєте?', 'ar': 'صباح الخير، ماذا تريد؟', 'fr': 'Bonjour, que désirez-vous ?', 'en': 'Good morning, what would you like?'},
            {'speaker': 'Cliente', 'es': 'Un café con leche, por favor.', 'ru': 'Кофе с молоком, пожалуйста.', 'uk': 'Кава з молоком, будь ласка.', 'ar': 'قهوة بالحليب، من فضلك.', 'fr': "Un café au lait, s'il vous plaît.", 'en': 'A coffee with milk, please.'},
            {'speaker': 'Camarero', 'es': '¿Algo más?', 'ru': 'Что-нибудь ещё?', 'uk': 'Щось іще?', 'ar': 'أي شيء آخر؟', 'fr': 'Autre chose ?', 'en': 'Anything else?'},
            {'speaker': 'Cliente', 'es': 'Sí, un croissant. ¿Cuánto es?', 'ru': 'Да, круассан. Сколько с меня?', 'uk': 'Так, круасан. Скільки з мене?', 'ar': 'نعم، كرواسون. كم الحساب؟', 'fr': 'Oui, un croissant. Ça fait combien ?', 'en': 'Yes, a croissant. How much is it?'},
            {'speaker': 'Camarero', 'es': 'Tres euros, por favor.', 'ru': 'Три евро, пожалуйста.', 'uk': 'Три євро, будь ласка.', 'ar': 'ثلاثة يورو، من فضلك.', 'fr': "Trois euros, s'il vous plaît.", 'en': 'Three euros, please.'},
        ],
    },
    {
        'id': 'a2_planes', 'level': 'A2',
        'title': {'es': 'Planes para el finde', 'ru': 'Планы на выходные', 'uk': 'Плани на вихідні', 'ar': 'خطط نهاية الأسبوع', 'fr': 'Plans du week-end', 'en': 'Weekend plans'},
        'lines': [
            {'speaker': 'Marta', 'es': '¿Qué vas a hacer este fin de semana?', 'ru': 'Что будешь делать в эти выходные?', 'uk': 'Що робитимеш ці вихідні?', 'ar': 'ماذا ستفعل نهاية هذا الأسبوع؟', 'fr': "Qu'est-ce que tu vas faire ce week-end ?", 'en': 'What are you going to do this weekend?'},
            {'speaker': 'Diego', 'es': 'Voy a ir a la playa con mi hermano.', 'ru': 'Поеду на пляж с братом.', 'uk': 'Поїду на пляж із братом.', 'ar': 'سأذهب إلى الشاطئ مع أخي.', 'fr': 'Je vais aller à la plage avec mon frère.', 'en': "I'm going to the beach with my brother."},
            {'speaker': 'Marta', 'es': '¡Qué bien! ¿A qué hora salís?', 'ru': 'Здорово! Во сколько выезжаете?', 'uk': 'Як добре! О котрій виїжджаєте?', 'ar': 'رائع! في أي ساعة تنطلقون؟', 'fr': 'Super ! À quelle heure partez-vous ?', 'en': 'Great! What time are you leaving?'},
            {'speaker': 'Diego', 'es': 'Temprano, sobre las ocho. ¿Quieres venir?', 'ru': 'Рано, около восьми. Хочешь с нами?', 'uk': 'Рано, близько восьмої. Хочеш із нами?', 'ar': 'مبكرًا، حوالي الثامنة. أتريد أن تأتي؟', 'fr': 'Tôt, vers huit heures. Tu veux venir ?', 'en': 'Early, around eight. Do you want to come?'},
            {'speaker': 'Marta', 'es': 'Me encantaría, pero tengo que estudiar.', 'ru': 'С удовольствием, но мне надо заниматься.', 'uk': 'Залюбки, але мені треба вчитися.', 'ar': 'يسعدني ذلك، لكن عليّ أن أدرس.', 'fr': "J'adorerais, mais je dois étudier.", 'en': "I'd love to, but I have to study."},
        ],
    },
    {
        'id': 'a2_tienda', 'level': 'A2',
        'title': {'es': 'En la tienda de ropa', 'ru': 'В магазине одежды', 'uk': 'У магазині одягу', 'ar': 'في متجر الملابس', 'fr': 'Au magasin de vêtements', 'en': 'At the clothes shop'},
        'lines': [
            {'speaker': 'Dependienta', 'es': '¿Puedo ayudarle en algo?', 'ru': 'Могу вам чем-то помочь?', 'uk': 'Чим можу вам допомогти?', 'ar': 'هل يمكنني مساعدتك بشيء؟', 'fr': 'Puis-je vous aider ?', 'en': 'Can I help you with something?'},
            {'speaker': 'Cliente', 'es': 'Sí, busco una camisa azul.', 'ru': 'Да, ищу синюю рубашку.', 'uk': 'Так, шукаю синю сорочку.', 'ar': 'نعم، أبحث عن قميص أزرق.', 'fr': 'Oui, je cherche une chemise bleue.', 'en': "Yes, I'm looking for a blue shirt."},
            {'speaker': 'Dependienta', 'es': '¿Qué talla usa?', 'ru': 'Какой у вас размер?', 'uk': 'Який у вас розмір?', 'ar': 'ما مقاسك؟', 'fr': 'Quelle taille faites-vous ?', 'en': 'What size do you wear?'},
            {'speaker': 'Cliente', 'es': 'La mediana. ¿Puedo probármela?', 'ru': 'Средний. Можно примерить?', 'uk': 'Середній. Можна приміряти?', 'ar': 'المتوسط. هل يمكنني تجربته؟', 'fr': "La taille moyenne. Je peux l'essayer ?", 'en': 'Medium. Can I try it on?'},
            {'speaker': 'Dependienta', 'es': 'Claro, el probador está al fondo.', 'ru': 'Конечно, примерочная в глубине зала.', 'uk': 'Звичайно, примірочна в глибині залу.', 'ar': 'بالطبع، غرفة القياس في الخلف.', 'fr': 'Bien sûr, la cabine est au fond.', 'en': 'Of course, the fitting room is at the back.'},
        ],
    },
    {
        'id': 'b1_alquiler', 'level': 'B1',
        'title': {'es': 'Buscando piso', 'ru': 'Поиск квартиры', 'uk': 'Пошук квартири', 'ar': 'البحث عن شقة', 'fr': 'Chercher un appartement', 'en': 'Flat hunting'},
        'lines': [
            {'speaker': 'Inquilino', 'es': 'Buenas, llamo por el piso que se alquila.', 'ru': 'Здравствуйте, звоню по поводу сдающейся квартиры.', 'uk': 'Доброго дня, телефоную щодо квартири, яку здають.', 'ar': 'مرحبًا، أتصل بخصوص الشقة المعروضة للإيجار.', 'fr': "Bonjour, j'appelle au sujet de l'appartement à louer.", 'en': "Hello, I'm calling about the flat for rent."},
            {'speaker': 'Casero', 'es': 'Perfecto. Está disponible desde el mes que viene.', 'ru': 'Отлично. Она свободна со следующего месяца.', 'uk': 'Чудово. Вона вільна з наступного місяця.', 'ar': 'ممتاز. إنها متاحة من الشهر القادم.', 'fr': 'Parfait. Il est disponible dès le mois prochain.', 'en': "Perfect. It's available from next month."},
            {'speaker': 'Inquilino', 'es': '¿Los gastos de comunidad están incluidos?', 'ru': 'Коммунальные платежи включены?', 'uk': 'Комунальні внески включені?', 'ar': 'هل رسوم الخدمات المشتركة مشمولة؟', 'fr': 'Les charges de copropriété sont-elles comprises ?', 'en': 'Are the community fees included?'},
            {'speaker': 'Casero', 'es': 'El agua sí, pero la luz va aparte.', 'ru': 'Вода — да, а электричество отдельно.', 'uk': 'Вода — так, а електрика окремо.', 'ar': 'الماء نعم، أما الكهرباء فمنفصلة.', 'fr': "L'eau oui, mais l'électricité est à part.", 'en': 'Water yes, but electricity is separate.'},
            {'speaker': 'Inquilino', 'es': '¿Podría verlo esta semana sin compromiso?', 'ru': 'Можно посмотреть на этой неделе, ни к чему не обязываясь?', 'uk': "Чи можу подивитися цього тижня, ні до чого не зобов'язуючись?", 'ar': 'هل يمكنني معاينتها هذا الأسبوع دون التزام؟', 'fr': 'Pourrais-je le voir cette semaine sans engagement ?', 'en': 'Could I see it this week with no obligation?'},
            {'speaker': 'Casero', 'es': 'Por supuesto, quedamos el jueves por la tarde.', 'ru': 'Разумеется, договоримся на четверг во второй половине дня.', 'uk': 'Звісно, домовмося на четвер по обіді.', 'ar': 'بالطبع، لنتفق على يوم الخميس بعد الظهر.', 'fr': 'Bien sûr, disons jeudi après-midi.', 'en': "Of course, let's meet Thursday afternoon."},
        ],
    },
    {
        'id': 'b1_medico', 'level': 'B1',
        'title': {'es': 'En la consulta', 'ru': 'На приёме у врача', 'uk': 'На прийомі в лікаря', 'ar': 'في العيادة', 'fr': 'Chez le médecin', 'en': 'At the clinic'},
        'lines': [
            {'speaker': 'Médica', 'es': '¿Qué le trae por aquí?', 'ru': 'Что вас привело?', 'uk': 'Що вас привело?', 'ar': 'ما الذي أتى بك إلى هنا؟', 'fr': "Qu'est-ce qui vous amène ?", 'en': 'What brings you here?'},
            {'speaker': 'Paciente', 'es': 'Llevo dos días con dolor de garganta y fiebre.', 'ru': 'Уже два дня болит горло и температура.', 'uk': 'Уже два дні болить горло і температура.', 'ar': 'منذ يومين أعاني من ألم في الحلق وحُمّى.', 'fr': "Depuis deux jours, j'ai mal à la gorge et de la fièvre.", 'en': "I've had a sore throat and a fever for two days."},
            {'speaker': 'Médica', 'es': '¿Le duele al tragar?', 'ru': 'Больно глотать?', 'uk': 'Боляче ковтати?', 'ar': 'هل تشعر بألم عند البلع؟', 'fr': 'Ça vous fait mal quand vous avalez ?', 'en': 'Does it hurt when you swallow?'},
            {'speaker': 'Paciente', 'es': 'Sí, bastante, y me cuesta dormir.', 'ru': 'Да, довольно сильно, и трудно спать.', 'uk': 'Так, доволі сильно, і важко спати.', 'ar': 'نعم، كثيرًا، وأجد صعوبة في النوم.', 'fr': "Oui, assez, et j'ai du mal à dormir.", 'en': 'Yes, quite a lot, and I find it hard to sleep.'},
            {'speaker': 'Médica', 'es': 'Le recetaré algo. Si no mejora, vuelva el lunes.', 'ru': 'Выпишу вам кое-что. Если не станет лучше, приходите в понедельник.', 'uk': 'Випишу вам дещо. Якщо не покращає, приходьте в понеділок.', 'ar': 'سأصف لك دواءً. إن لم تتحسّن، عُد يوم الاثنين.', 'fr': "Je vais vous prescrire quelque chose. Si ça ne s'améliore pas, revenez lundi.", 'en': "I'll prescribe you something. If it doesn't improve, come back Monday."},
        ],
    },
    {
        'id': 'b2_trabajo', 'level': 'B2',
        'title': {'es': 'Malentendido en el trabajo', 'ru': 'Недопонимание на работе', 'uk': 'Непорозуміння на роботі', 'ar': 'سوء تفاهم في العمل', 'fr': 'Malentendu au travail', 'en': 'A mix-up at work'},
        'lines': [
            {'speaker': 'Jefe', 'es': 'Contaba con el informe para hoy. ¿Qué ha pasado?', 'ru': 'Я рассчитывал на отчёт к сегодняшнему дню. Что случилось?', 'uk': 'Я розраховував на звіт до сьогодні. Що сталося?', 'ar': 'كنت أعوّل على التقرير لهذا اليوم. ماذا حدث؟', 'fr': "Je comptais sur le rapport pour aujourd'hui. Que s'est-il passé ?", 'en': 'I was counting on the report for today. What happened?'},
            {'speaker': 'Empleado', 'es': 'Disculpe, entendí que el plazo era el viernes.', 'ru': 'Извините, я понял, что срок — пятница.', 'uk': "Перепрошую, я зрозумів, що термін — п'ятниця.", 'ar': 'عذرًا، فهمت أن الموعد النهائي هو الجمعة.', 'fr': "Excusez-moi, j'avais compris que l'échéance était vendredi.", 'en': 'Sorry, I understood the deadline was Friday.'},
            {'speaker': 'Jefe', 'es': 'Ya veo. Quizá no me expliqué con claridad.', 'ru': 'Понятно. Возможно, я не объяснил ясно.', 'uk': 'Розумію. Можливо, я пояснив недостатньо чітко.', 'ar': 'أرى. ربما لم أوضّح بما يكفي.', 'fr': 'Je vois. Je ne me suis peut-être pas exprimé clairement.', 'en': "I see. Perhaps I didn't explain clearly."},
            {'speaker': 'Empleado', 'es': 'De todos modos, puedo tenerlo listo en dos horas.', 'ru': 'В любом случае, я могу подготовить его за два часа.', 'uk': 'У будь-якому разі, я можу підготувати його за дві години.', 'ar': 'على أي حال، يمكنني إنجازه خلال ساعتين.', 'fr': "De toute façon, je peux l'avoir prêt dans deux heures.", 'en': 'In any case, I can have it ready in two hours.'},
            {'speaker': 'Jefe', 'es': 'Te lo agradezco. Avísame en cuanto lo termines.', 'ru': 'Буду признателен. Дай знать, как закончишь.', 'uk': 'Дякую. Повідом, щойно закінчиш.', 'ar': 'أشكرك. أعلمني حالما تنتهي.', 'fr': "Je t'en remercie. Préviens-moi dès que tu as fini.", 'en': 'I appreciate it. Let me know as soon as you finish.'},
        ],
    },
    {
        'id': 'b2_viaje', 'level': 'B2',
        'title': {'es': 'Un vuelo cancelado', 'ru': 'Отменённый рейс', 'uk': 'Скасований рейс', 'ar': 'رحلة ملغاة', 'fr': 'Un vol annulé', 'en': 'A cancelled flight'},
        'lines': [
            {'speaker': 'Pasajero', 'es': 'Me acaban de decir que mi vuelo está cancelado.', 'ru': 'Мне только что сказали, что мой рейс отменён.', 'uk': 'Мені щойно сказали, що мій рейс скасовано.', 'ar': 'قيل لي للتوّ إن رحلتي أُلغيت.', 'fr': 'On vient de me dire que mon vol est annulé.', 'en': "I've just been told my flight is cancelled."},
            {'speaker': 'Agente', 'es': 'Lo lamento. Puedo reubicarle en el de las seis.', 'ru': 'Сожалею. Могу пересадить вас на рейс в шесть.', 'uk': 'Співчуваю. Можу пересадити вас на рейс о шостій.', 'ar': 'يؤسفني ذلك. يمكنني نقلك إلى رحلة الساعة السادسة.', 'fr': 'Je suis désolé. Je peux vous replacer sur celui de six heures.', 'en': "I'm sorry. I can rebook you on the six o'clock one."},
            {'speaker': 'Pasajero', 'es': 'Es que perdería la conexión en Madrid.', 'ru': 'Дело в том, что я потеряю стыковку в Мадриде.', 'uk': 'Річ у тім, що я втрачу пересадку в Мадриді.', 'ar': 'لكنني سأفوّت الرحلة المتّصلة في مدريد.', 'fr': "C'est que je raterais la correspondance à Madrid.", 'en': "The thing is, I'd miss my connection in Madrid."},
            {'speaker': 'Agente', 'es': 'En ese caso, le buscaré una ruta alternativa.', 'ru': 'В таком случае найду вам альтернативный маршрут.', 'uk': 'У такому разі знайду вам альтернативний маршрут.', 'ar': 'في هذه الحالة، سأبحث لك عن مسار بديل.', 'fr': 'Dans ce cas, je vais vous chercher un autre itinéraire.', 'en': "In that case, I'll find you an alternative route."},
            {'speaker': 'Pasajero', 'es': '¿Tendría derecho a alguna compensación?', 'ru': 'Мне полагается какая-то компенсация?', 'uk': 'Чи маю я право на якусь компенсацію?', 'ar': 'هل يحق لي أي تعويض؟', 'fr': 'Aurais-je droit à une compensation ?', 'en': 'Would I be entitled to any compensation?'},
            {'speaker': 'Agente', 'es': 'Sí, le entrego el formulario ahora mismo.', 'ru': 'Да, сейчас же выдам вам бланк.', 'uk': 'Так, зараз же видам вам бланк.', 'ar': 'نعم، سأسلّمك الاستمارة الآن.', 'fr': 'Oui, je vous remets le formulaire tout de suite.', 'en': "Yes, I'll give you the form right now."},
        ],
    },
    {
        'id': 'c1_debate', 'level': 'C1',
        'title': {'es': 'Debate sobre el teletrabajo', 'ru': 'Спор об удалёнке', 'uk': 'Дискусія про віддалену роботу', 'ar': 'نقاش حول العمل عن بُعد', 'fr': 'Débat sur le télétravail', 'en': 'Debating remote work'},
        'lines': [
            {'speaker': 'Elena', 'es': 'Sostengo que el teletrabajo mejora la productividad.', 'ru': 'Я утверждаю, что удалёнка повышает продуктивность.', 'uk': 'Я стверджую, що віддалена робота підвищує продуктивність.', 'ar': 'أرى أن العمل عن بُعد يحسّن الإنتاجية.', 'fr': 'Je soutiens que le télétravail améliore la productivité.', 'en': 'I maintain that remote work improves productivity.'},
            {'speaker': 'Raúl', 'es': 'Hasta cierto punto; también diluye el trabajo en equipo.', 'ru': 'До определённой степени; она к тому же размывает командную работу.', 'uk': 'До певної міри; вона також розмиває командну роботу.', 'ar': 'إلى حدٍّ ما؛ لكنه أيضًا يُضعف العمل الجماعي.', 'fr': "Jusqu'à un certain point ; il dilue aussi le travail d'équipe.", 'en': 'Up to a point; it also dilutes teamwork.'},
            {'speaker': 'Elena', 'es': 'Siempre que haya reuniones periódicas, no tiene por qué.', 'ru': 'При условии регулярных встреч — вовсе не обязательно.', 'uk': "За умови регулярних зустрічей — зовсім не обов'язково.", 'ar': 'ما دامت هناك اجتماعات دورية، فليس بالضرورة كذلك.', 'fr': "À condition qu'il y ait des réunions régulières, pas forcément.", 'en': 'As long as there are regular meetings, not necessarily.'},
            {'speaker': 'Raúl', 'es': 'Reconozco que depende de cómo se gestione.', 'ru': 'Признаю, что всё зависит от того, как этим управлять.', 'uk': 'Визнаю, що все залежить від того, як цим керувати.', 'ar': 'أعترف أن الأمر يعتمد على كيفية إدارته.', 'fr': 'Je reconnais que cela dépend de la gestion.', 'en': "I admit it depends on how it's managed."},
            {'speaker': 'Elena', 'es': 'Exacto: el problema no es el modelo, sino su aplicación.', 'ru': 'Именно: проблема не в модели, а в её применении.', 'uk': 'Саме так: проблема не в моделі, а в її застосуванні.', 'ar': 'بالضبط: المشكلة ليست في النموذج بل في تطبيقه.', 'fr': "Exactement : le problème n'est pas le modèle, mais son application.", 'en': "Exactly: the problem isn't the model, but its application."},
        ],
    },
    {
        'id': 'c1_queja', 'level': 'C1',
        'title': {'es': 'Una reclamación formal', 'ru': 'Официальная жалоба', 'uk': 'Офіційна скарга', 'ar': 'شكوى رسمية', 'fr': 'Une réclamation formelle', 'en': 'A formal complaint'},
        'lines': [
            {'speaker': 'Cliente', 'es': 'Quisiera dejar constancia de mi descontento con el servicio.', 'ru': 'Я хотел бы зафиксировать своё недовольство обслуживанием.', 'uk': 'Я хотів би офіційно зафіксувати своє незадоволення обслуговуванням.', 'ar': 'أودّ أن أسجّل استيائي من الخدمة.', 'fr': 'Je voudrais faire consigner mon mécontentement quant au service.', 'en': "I'd like to formally register my dissatisfaction with the service."},
            {'speaker': 'Gerente', 'es': 'Le escucho. Lamento que no haya cumplido sus expectativas.', 'ru': 'Слушаю вас. Сожалею, что оно не оправдало ваших ожиданий.', 'uk': 'Слухаю вас. Шкодую, що воно не виправдало ваших очікувань.', 'ar': 'أنا أستمع إليك. يؤسفني أنها لم تلبِّ توقعاتك.', 'fr': "Je vous écoute. Je regrette qu'il n'ait pas répondu à vos attentes.", 'en': "I'm listening. I'm sorry it didn't meet your expectations."},
            {'speaker': 'Cliente', 'es': 'Se me prometió una reparación que nunca llegó a realizarse.', 'ru': 'Мне обещали ремонт, который так и не был выполнен.', 'uk': 'Мені пообіцяли ремонт, який так і не було виконано.', 'ar': 'وُعدت بإصلاح لم يُنفَّذ قط.', 'fr': "On m'a promis une réparation qui n'a jamais été effectuée.", 'en': 'I was promised a repair that was never carried out.'},
            {'speaker': 'Gerente', 'es': 'Asumo la responsabilidad y le propongo una solución inmediata.', 'ru': 'Беру на себя ответственность и предлагаю немедленное решение.', 'uk': 'Беру на себе відповідальність і пропоную вам негайне рішення.', 'ar': 'أتحمّل المسؤولية وأقترح عليك حلًّا فوريًّا.', 'fr': "J'assume la responsabilité et je vous propose une solution immédiate.", 'en': 'I take responsibility and offer you an immediate solution.'},
            {'speaker': 'Cliente', 'es': 'Le agradecería que lo pusiera por escrito.', 'ru': 'Буду признателен, если вы оформите это письменно.', 'uk': 'Буду вдячний, якщо ви оформите це письмово.', 'ar': 'سأكون ممتنًّا لو وضعت ذلك كتابةً.', 'fr': 'Je vous saurais gré de le mettre par écrit.', 'en': "I'd be grateful if you put it in writing."},
        ],
    },
    {
        'id': 'c2_matiz', 'level': 'C2',
        'title': {'es': 'Matices de una negociación', 'ru': 'Нюансы переговоров', 'uk': 'Нюанси переговорів', 'ar': 'دقائق التفاوض', 'fr': "Nuances d'une négociation", 'en': 'Negotiation nuances'},
        'lines': [
            {'speaker': 'Socio A', 'es': 'No es que rechacemos la oferta, sino que la matizaríamos.', 'ru': 'Дело не в том, что мы отвергаем предложение, — мы бы его уточнили.', 'uk': 'Річ не в тому, що ми відхиляємо пропозицію, — ми б її уточнили.', 'ar': 'ليس أننا نرفض العرض، بل إننا سنُضيف إليه بعض التحفّظات.', 'fr': "Ce n'est pas que nous rejetions l'offre, mais nous la nuancerions.", 'en': "It's not that we reject the offer; we'd rather qualify it."},
            {'speaker': 'Socio B', 'es': 'Entiendo la sutileza, pero necesitamos garantías tangibles.', 'ru': 'Понимаю тонкость, но нам нужны осязаемые гарантии.', 'uk': 'Розумію тонкість, але нам потрібні відчутні гарантії.', 'ar': 'أفهم الفارق الدقيق، لكننا نحتاج إلى ضمانات ملموسة.', 'fr': 'Je comprends la nuance, mais il nous faut des garanties tangibles.', 'en': 'I understand the subtlety, but we need tangible guarantees.'},
            {'speaker': 'Socio A', 'es': 'Las habrá, siempre y cuando se respeten los plazos acordados.', 'ru': 'Они будут, при условии соблюдения оговорённых сроков.', 'uk': 'Вони будуть, за умови дотримання узгоджених термінів.', 'ar': 'ستكون هناك ضمانات، شريطة احترام المواعيد المتّفق عليها.', 'fr': 'Il y en aura, à condition que les délais convenus soient respectés.', 'en': 'There will be, provided the agreed deadlines are respected.'},
            {'speaker': 'Socio B', 'es': 'De ser así, estaríamos dispuestos a reconsiderar el conjunto.', 'ru': 'Если так, мы были бы готовы пересмотреть пакет в целом.', 'uk': 'Якщо так, ми були б готові переглянути пакет у цілому.', 'ar': 'إن كان الأمر كذلك، فسنكون مستعدّين لإعادة النظر في الحزمة ككل.', 'fr': "Si tel est le cas, nous serions prêts à reconsidérer l'ensemble.", 'en': "If so, we'd be willing to reconsider the whole package."},
            {'speaker': 'Socio A', 'es': 'Me alegra que hablemos ya el mismo idioma.', 'ru': 'Рад, что мы наконец говорим на одном языке.', 'uk': 'Радий, що ми нарешті говоримо однією мовою.', 'ar': 'يسعدني أننا صرنا نتحدث اللغة نفسها.', 'fr': 'Je suis heureux que nous parlions enfin le même langage.', 'en': "I'm glad we're finally speaking the same language."},
        ],
    },
    {
        'id': 'c2_ironia', 'level': 'C2',
        'title': {'es': 'Ironía entre amigos', 'ru': 'Ирония между друзьями', 'uk': 'Іронія між друзями', 'ar': 'سخرية بين الأصدقاء', 'fr': 'Ironie entre amis', 'en': 'Irony among friends'},
        'lines': [
            {'speaker': 'Sofía', 'es': '¡Menudo madrugón! Solo son las doce del mediodía.', 'ru': 'Ну и ранняя пташка! Всего-то полдень.', 'uk': 'Оце так ранній підйом! Усього-на-всього полудень.', 'ar': 'يا له من استيقاظ مبكّر! إنها الثانية عشرة ظهرًا فقط.', 'fr': "Quel réveil matinal ! Il n'est que midi.", 'en': "What an early start! It's only noon."},
            {'speaker': 'Pablo', 'es': 'Ya ves, es que me sobra el tiempo libre…', 'ru': 'Ну да, у меня же уйма свободного времени…', 'uk': 'Та ж бачиш, у мене ж повно вільного часу…', 'ar': 'كما ترى، لديّ فائض من وقت الفراغ…', 'fr': "Tu vois, c'est que j'ai trop de temps libre…", 'en': "You see, I've just got too much free time…"},
            {'speaker': 'Sofía', 'es': 'No me digas. Con lo ocupadísimo que estás siempre.', 'ru': 'Да что ты. При твоей вечной сверхзанятости.', 'uk': 'Та невже. При твоїй вічній надзайнятості.', 'ar': 'لا تقل لي! مع أنك مشغول جدًّا دائمًا.', 'fr': 'Sans blague. Toi qui es toujours si occupé.', 'en': "You don't say. With how terribly busy you always are."},
            {'speaker': 'Pablo', 'es': 'Tú, en cambio, la puntualidad en persona.', 'ru': 'Зато ты — сама пунктуальность.', 'uk': 'Зате ти — сама пунктуальність.', 'ar': 'أما أنت، فأنت الانضباط في المواعيد بذاته.', 'fr': 'Toi, en revanche, la ponctualité incarnée.', 'en': 'You, on the other hand, are punctuality itself.'},
            {'speaker': 'Sofía', 'es': 'Toquemos otro tema, anda, que nos conocemos.', 'ru': 'Давай сменим тему, мы же друг друга знаем.', 'uk': 'Змінімо тему, годі, ми ж одне одного знаємо.', 'ar': 'لنغيّر الموضوع، هيا، فنحن نعرف بعضنا جيدًا.', 'fr': 'Changeons de sujet, allez, on se connaît.', 'en': "Let's change the subject — come on, we know each other."},
        ],
    },
]

_BY_LEVEL = {}
for _d in DIALOGUES:
    _BY_LEVEL.setdefault(_d['level'], []).append(_d)

_GLOSS_LANGS = ('ru', 'uk', 'ar', 'fr', 'en')


def _pick(d: dict, lang: str) -> str:
    """Best available value from a per-language dict: requested → ru → en → es."""
    code = (lang or 'ru')[:2].lower()
    return d.get(code) or d.get('ru') or d.get('en') or d.get('es') or ''


def _title(d: dict, lang: str) -> str:
    return _pick(d['title'], lang)


def public_list(level: str | None = None, lang: str = 'ru') -> list[dict]:
    """Return built-in dialogues (optionally filtered by level), title + line glosses
    localized to `lang` with graceful fallback to ru/en/es."""
    items = _BY_LEVEL.get(level.upper(), []) if level else DIALOGUES
    out = []
    for d in items:
        out.append({
            'id': d['id'], 'level': d['level'], 'title': _title(d, lang),
            'lines': [{'speaker': l['speaker'], 'es': l['es'],
                       'translation': _pick(l, lang)} for l in d['lines']],
        })
    return out
