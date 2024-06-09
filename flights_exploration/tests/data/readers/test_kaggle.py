import types
from pathlib import Path

import pytest

from flights_exploration.data.readers.kaggle import KaggleFlightsReader
from flights_exploration.tests.utils import get_static_test_file


@pytest.fixture
def kaggle_dataset():
    return get_static_test_file("kaggle.csv")


def test_kaggle_read_file(kaggle_dataset: Path):
    reader = KaggleFlightsReader()
    with open(kaggle_dataset, "r", encoding="utf8") as kaggle_io:
        data = reader.read_file(kaggle_io)
        line = next(data)
        assert sorted(list(line.keys())) == sorted(KaggleFlightsReader().file_headers)


def test_kaggle_get_flights(kaggle_dataset: Path):
    reader = KaggleFlightsReader()
    with open(kaggle_dataset, "r", encoding="utf8") as kaggle_io:
        data = reader.get_flights(kaggle_io)
        assert isinstance(data, list)
        assert len(data) == 2
        for line in data:
            assert sorted(list(line.keys())) == sorted(
                KaggleFlightsReader().file_headers
            )


def test_kaggle_iter_flights(kaggle_dataset: Path):
    reader = KaggleFlightsReader()
    with open(kaggle_dataset, "r", encoding="utf8") as kaggle_io:
        data = reader.iter_flights(kaggle_io)
        assert isinstance(data, types.GeneratorType)
        for line in data:
            assert sorted(list(line.keys())) == sorted(
                KaggleFlightsReader().file_headers
            )
