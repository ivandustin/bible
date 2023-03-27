from pathlib import Path
from pytest import fixture
from pandas import Series
from .constants.codepoints.greek import ALPHA, OMEGA
from .functions.get_dataframe import get_dataframe
from .constants.alphabets.greek import MAPPING


@fixture
def dataframe():
    return get_dataframe(Path("data/new"))


@fixture
def words(dataframe):
    return dataframe["word"]


@fixture
def letters(words):
    return Series([letter for word in words for letter in word])


@fixture
def codepoints(letters):
    return letters.apply(ord)


@fixture
def mapping():
    return dict(zip(map(ord, MAPPING.keys()), MAPPING.values()))


def test_encoding(codepoints):
    assert codepoints.apply(lambda n: ALPHA <= n <= OMEGA).all()


def test_word_count(words):
    assert len(words) == 137_720


def test_letter_count(letters):
    assert len(letters) == 688_623


def test_total_value(codepoints, mapping):
    assert codepoints.map(mapping).sum() == 79_384_882
