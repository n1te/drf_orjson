import io
import json


def test_parser(parser, json_data):
    value = json.dumps(json_data, default=float)
    parsed = parser.parse(io.BytesIO(value.encode()))
    assert parsed == json_data
