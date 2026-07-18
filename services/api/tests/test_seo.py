"""Public AI-SEO surface: robots, sitemap, llms, lesson pages."""


def test_robots_txt(client):
    r = client.get('/robots.txt')
    assert r.status_code == 200
    assert 'Sitemap:' in r.text
    assert 'GPTBot' in r.text  # AI crawlers welcomed


def test_sitemap_xml(client):
    r = client.get('/sitemap.xml')
    assert r.status_code == 200
    assert '<urlset' in r.text
    assert '/learn' in r.text


def test_llms_txt(client):
    r = client.get('/llms.txt')
    assert r.status_code == 200
    assert r.text.startswith('#')


def test_learn_index(client):
    r = client.get('/learn')
    assert r.status_code == 200
    assert 'schema.org' in r.text  # JSON-LD present
    assert '<h1>' in r.text
