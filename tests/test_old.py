from pathlib import Path
from pytest import fixture
from .constants.codepoints.hebrew import ALEF, TAV
from .constants.alphabets.hebrew import MAPPING
from .functions.ord_keys import ord_keys


@fixture
def directory():
    return Path("data/old")


def test_encoding(codepoints):
    assert codepoints.apply(lambda n: ALEF <= n <= TAV).all()


def test_word_count(words):
    assert len(words) == 305_496


def test_letter_count(letters):
    assert len(letters) == 1_197_042


def test_total_value(codepoints):
    assert codepoints.map(ord_keys(MAPPING)).sum() == 78_091_408
