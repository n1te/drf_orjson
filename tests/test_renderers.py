import orjson


def test_render(renderer, data, json_data):
    rendered = renderer.render(data)
    assert orjson.loads(rendered) == json_data
