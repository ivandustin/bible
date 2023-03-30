from pathlib import Path
from pytest import fixture


@fixture(params=["data/new", "data/old"])
def directory(request):
    return Path(request.param)


def test_dtype(dataframe):
    assert dataframe["chapter"].dtype == "int"
    assert dataframe["verse"].dtype == "int"
    assert dataframe["word"].dtype == "string"


def test_no_nulls(dataframe):
    assert dataframe.notnull().values.all()
