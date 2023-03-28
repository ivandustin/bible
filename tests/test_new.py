from pathlib import Path
from pytest import fixture
from .constants.codepoints.greek import ALPHA, OMEGA
from .constants.alphabets.greek import MAPPING
from .functions.ord_keys import ord_keys


@fixture
def directory():
    return Path("data/new")


def test_encoding(codepoints):
    assert codepoints.apply(lambda n: ALPHA <= n <= OMEGA).all()


def test_word_count(words):
    assert len(words) == 137_720


def test_letter_count(letters):
    assert len(letters) == 688_623


def test_total_value(codepoints):
    assert codepoints.map(ord_keys(MAPPING)).sum() == 79_384_882
