import uuid
from decimal import Decimal

import orjson
from rest_framework.renderers import JSONRenderer


def default_serializer(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    if isinstance(obj, str):
        return str(obj)
    if isinstance(obj, dict):
        return dict(obj)
    elif hasattr(obj, '__iter__'):
        return list(item for item in obj)
    elif isinstance(obj, uuid.UUID):
        return str(obj)
    elif hasattr(obj, 'tolist'):
        return obj.tolist()
    elif hasattr(obj, '__getitem__'):
        cls = list if isinstance(obj, (list, tuple)) else dict
        try:
            return cls(obj)
        except:
            pass
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
