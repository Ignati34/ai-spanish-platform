"""Personal vocabulary knowledge base, built from the owner's study files.

Sources (parsed offline into vocab_bank.json, which is committed):
- "2100 verbs": verb headwords + collocations + real example sentences, ES with RU translations
- "Emotions/conversational": colloquial phrases and reactions for lively dialogue

Used to enrich AI-generated lessons, exercises and role-play dialogues so the platform
speaks with the learner's own growing vocabulary. All entries: {'es': ..., 'ru': ...}.
"""
from __future__ import annotations

import json
import random
from functools import lru_cache
from pathlib import Path

_BANK_PATH = Path(__file__).parent / 'vocab_bank.json'


@lru_cache(maxsize=1)
def load_bank() -> dict:
    try:
        with open(_BANK_PATH, encoding='utf-8') as f:
            data = json.load(f)
    except Exception:
        return {'verbs': [], 'collocations': [], 'examples': [], 'phrases': []}
    for key in ('verbs', 'collocations', 'examples', 'phrases'):
        data.setdefault(key, [])
    return data


def counts() -> dict:
    bank = load_bank()
    return {k: len(v) for k, v in bank.items()}


def sample(kind: str, n: int, rng: random.Random | None = None) -> list[dict]:
    items = load_bank().get(kind, [])
    if not items:
        return []
    r = rng or random
    return r.sample(items, min(n, len(items)))


def search(query: str, kind: str | None = None, limit: int = 50) -> list[dict]:
    q = (query or '').strip().lower()
    bank = load_bank()
    kinds = [kind] if kind in bank else list(bank.keys())
    out = []
    for k in kinds:
        for item in bank[k]:
            if not q or q in item['es'].lower() or q in item['ru'].lower():
                out.append({**item, 'kind': k})
                if len(out) >= limit:
                    return out
    return out


def enrichment_block(n_verbs: int = 8, n_phrases: int = 6, n_examples: int = 3,
                     seed: int | None = None) -> str:
    """A compact prompt block asking the model to weave the learner's own vocabulary in."""
    rng = random.Random(seed) if seed is not None else None
    verbs = sample('verbs', n_verbs, rng)
    phrases = sample('phrases', n_phrases, rng)
    examples = sample('examples', n_examples, rng)
    if not (verbs or phrases or examples):
        return ''
    lines = []
    if verbs:
        lines.append('Verbs: ' + '; '.join(f"{v['es']} ({v['ru']})" for v in verbs))
    if phrases:
        lines.append('Colloquial phrases: ' + '; '.join(f"{p['es']} ({p['ru']})" for p in phrases))
    if examples:
        lines.append('Example sentences: ' + ' | '.join(f"{e['es']} — {e['ru']}" for e in examples))
    return (
        "\nLearner's personal vocabulary bank (Spanish with Russian glosses). "
        'Where natural and level-appropriate, weave a few of these into your Spanish '
        '(dialogue lines, examples, exercises) to reinforce them — do not force all of them:\n'
        + '\n'.join(lines)
    )
