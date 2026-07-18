"""The built-in curriculum is well-formed: every level covered, >=4 valid exercises each."""
from collections import Counter

from app.content.curriculum import CURRICULUM


def test_all_levels_covered():
    by_level = Counter(l['level'] for l in CURRICULUM)
    for lvl in ['A1', 'A2', 'B1', 'B2', 'C1', 'C2']:
        assert by_level.get(lvl, 0) >= 3, f'{lvl} under-populated'


def test_each_lesson_has_theory_and_4_exercises():
    for l in CURRICULUM:
        assert l.get('theory'), l['title']
        assert len(l.get('exercises', [])) >= 4, l['title']


def test_exercise_answers_match_options():
    for l in CURRICULUM:
        for ex in l['exercises']:
            opts = ex.get('options')
            if opts:
                assert ex['correct_answer'] in opts, (l['title'], ex['correct_answer'])
