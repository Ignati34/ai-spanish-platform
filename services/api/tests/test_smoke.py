"""End-to-end smoke tests over the full app (stub AI, SQLite)."""


def test_health(client):
    r = client.get('/api/health')
    assert r.status_code == 200


def test_root(client):
    r = client.get('/')
    assert r.status_code == 200
    assert r.json()['status'] == 'running'


def test_auth_and_me(client, auth):
    r = client.get('/api/users/me', headers=auth)
    assert r.status_code == 200, r.text
    body = r.json()
    assert body['current_cefr_level'] == 'A1'
    assert body['native_language'] == 'ru'


def test_login_wrong_password(client):
    email = 'wrongpw@example.com'
    client.post('/api/auth/register', json={'email': email, 'password': 'password123', 'native_language': 'ru'})
    r = client.post('/api/auth/login', json={'email': email, 'password': 'nope-nope-1'})
    assert r.status_code == 401


def test_diagnostic_flow(client, auth):
    q = client.get('/api/diagnostic/questions?native_language=ru', headers=auth)
    assert q.status_code == 200, q.text
    questions = q.json()['questions']
    assert len(questions) >= 4
    answers = [{'id': item['id'], 'answer': 0} for item in questions]
    r = client.post('/api/diagnostic/submit', headers=auth,
                    json={'answers': answers, 'writing_sample': 'Hola, me llamo Ana.', 'native_language': 'ru'})
    assert r.status_code == 200, r.text
    body = r.json()
    assert body['recommended_level'] in {'A1', 'A2', 'B1', 'B2', 'C1', 'C2'}
    # placement is written back to the profile
    me = client.get('/api/users/me', headers=auth).json()
    assert me['current_cefr_level'] == body['recommended_level']


def test_upload_text_builds_lesson(client, auth):
    r = client.post('/api/uploads/text', headers=auth,
                    json={'text': 'Hola. Me llamo Ana. Vivo en Madrid y trabajo en un banco.',
                          'native_language': 'ru', 'cefr_level': 'A1'})
    assert r.status_code == 200, r.text
    body = r.json()
    assert body['lesson_id']
    assert 'analysis' in body
    assert isinstance(body['cards'], list)


def test_srs_and_motivation(client, auth):
    # building a lesson creates flashcards -> they become due for review
    client.post('/api/uploads/text', headers=auth,
                json={'text': 'hola gracias por favor buenos dias hasta luego', 'native_language': 'ru', 'cefr_level': 'A1'})
    due = client.get('/api/srs/due', headers=auth)
    assert due.status_code == 200, due.text
    cards = due.json()['cards']
    assert len(cards) >= 1
    rv = client.post('/api/srs/review', headers=auth, json={'card_id': cards[0]['id'], 'grade': 'good'})
    assert rv.status_code == 200, rv.text
    assert rv.json()['interval_days'] >= 1
    # the review counts toward the daily goal / motivation
    mot = client.get('/api/motivation/overview', headers=auth)
    assert mot.status_code == 200
    assert mot.json()['today_count'] >= 1


def test_simulation_flow(client, auth):
    scen = client.get('/api/simulations/scenarios?native_language=ru', headers=auth)
    assert scen.status_code == 200
    sid = scen.json()['scenarios'][0]['id']
    start = client.post('/api/simulations/start', headers=auth,
                        json={'scenario_id': sid, 'cefr_level': 'A1', 'native_language': 'ru'})
    assert start.status_code == 200, start.text
    session_id = start.json()['session_id']
    msg = client.post(f'/api/simulations/{session_id}/message', headers=auth, data={'text': 'Hola, quiero una cita.'})
    assert msg.status_code == 200, msg.text
    body = msg.json()
    assert 'reply_es' in body and 'goal_met' in body


def test_billing_providers_country(client, auth):
    r = client.get('/api/billing/providers?country=ES', headers=auth)
    assert r.status_code == 200
    providers = r.json()['providers']
    # Bizum should be flagged recommended for Spain when Stripe is enabled
    flat = [m for p in providers for m in p['methods']]
    assert any(m.get('recommended') for m in flat) or providers == []


def test_update_native_language(client, auth):
    # default from registration is 'ru' here; switch to Spanish explanations
    r = client.patch('/api/users/me', headers=auth, json={'native_language': 'es'})
    assert r.status_code == 200, r.text
    assert r.json()['native_language'] == 'es'
    # persisted
    me = client.get('/api/users/me', headers=auth).json()
    assert me['native_language'] == 'es'


def test_update_language_rejects_unknown(client, auth):
    r = client.patch('/api/users/me', headers=auth, json={'native_language': 'zz'})
    assert r.status_code == 422


def test_progress_record_shows_in_overview(client, auth):
    r = client.post('/api/progress/record', headers=auth,
                    json={'original': 'Yo tengo hambre', 'corrected': 'Yo tengo hambre (ok)',
                          'explanation': 'ser vs estar', 'topic': 'ser/estar'})
    assert r.status_code == 200, r.text
    ov = client.get('/api/progress/overview', headers=auth).json()
    assert ov['total_mistakes'] >= 1
    assert any(s['topic'] == 'ser/estar' for s in ov['weak_spots'])
