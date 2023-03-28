from pytest import fixture
from pandas import Series
from .functions.get_dataframe import get_dataframe


@fixture
def dataframe(directory):
    return get_dataframe(directory)


@fixture
def words(dataframe):
    return dataframe["word"]


@fixture
def letters(words):
    return Series([letter for word in words for letter in word])


@fixture
def codepoints(letters):
    return letters.apply(ord)
