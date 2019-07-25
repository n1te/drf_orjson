from django.conf import settings

import orjson
from rest_framework.parsers import BaseParser, ParseError
from rest_framework.renderers import JSONRenderer


class ORJSONParser(BaseParser):
    media_type = 'application/json'
    renderer_class = JSONRenderer

    def parse(self, stream, media_type=None, parser_context=None):
        parser_context = parser_context or {}
        encoding = parser_context.get('encoding', settings.DEFAULT_CHARSET)

        try:
            data = stream.read().decode(encoding)
            return orjson.loads(data)
        except ValueError as exc:
            raise ParseError('JSON parse error - %s' % str(exc))
