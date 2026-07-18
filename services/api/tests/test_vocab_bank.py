"""The personal vocabulary bank loads and is well-formed."""
from app.content.vocab_bank import counts, enrichment_block, load_bank, sample, search


def test_bank_loads_with_content():
    c = counts()
    assert c['verbs'] >= 300 and c['phrases'] >= 1500 and c['examples'] >= 500


def test_entries_have_both_languages():
    bank = load_bank()
    for kind, items in bank.items():
        for item in items[:200]:
            assert item.get('es') and item.get('ru'), (kind, item)


def test_enrichment_block_and_helpers():
    assert 'personal vocabulary bank' in enrichment_block(seed=42)
    assert len(sample('verbs', 5)) == 5
    assert search('gracias', limit=5)
