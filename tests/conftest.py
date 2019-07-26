import uuid
from decimal import Decimal

import pytest

from drf_orjson.parsers import ORJSONParser
from drf_orjson.renderers import ORJSONRenderer


@pytest.fixture
def data():
    return {
        'list': [1, 2, 3],
        'bool': True,
        'float': 1.23,
        'str': 'test',
        'dict': {'foo': 'bar'},
        'decimal': Decimal('95.2'),
        'iter': range(3),
        'uuid': uuid.uuid4(),
    }


@pytest.fixture
def json_data(data):
    jdata = data.copy()
    jdata.update({
        'decimal': 95.2,
        'iter': [0, 1, 2],
        'uuid': str(data['uuid']),
    })
    return jdata


@pytest.fixture
def renderer():
    return ORJSONRenderer()


@pytest.fixture
def parser():
    return ORJSONParser()
