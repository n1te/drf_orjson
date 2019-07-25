import io
import json


def test_parser(parser, data, json_data):
    value = json.dumps(data, default=float)
    parsed = parser.parse(io.BytesIO(value.encode()))
    assert parsed == json_data
