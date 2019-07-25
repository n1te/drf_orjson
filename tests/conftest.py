from decimal import Decimal

import pytest

from drf_orjson.parsers import ORJSONParser
from drf_orjson.renderers import ORJSONRenderer


@pytest.fixture
def data():
    return {
        'a': [1, 2, 3],
        'b': True,
        'c': 1.23,
        'd': 'test',
        'e': {'foo': 'bar'},
        'f': Decimal('95.2'),
    }


@pytest.fixture
def json_data(data):
    jdata = data.copy()
    jdata['f'] = 95.2
    return jdata


@pytest.fixture
def renderer():
    return ORJSONRenderer()


@pytest.fixture
def parser():
    return ORJSONParser()
