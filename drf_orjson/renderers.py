from decimal import Decimal

import orjson
from rest_framework.renderers import JSONRenderer


def default_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError


class ORJSONRenderer(JSONRenderer):
    """
    Renderer which serializes to JSON using orjson library.
    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Render `data` into JSON, returning a bytestring.
        """
        if data is None:
            return b''

        return orjson.dumps(data, default=default_serializer)
