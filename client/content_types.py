import json as _json
from client.spec import spec, raises


@raises("ValueError")
@spec('string', 'dict | list | number | string | None')
def json(data):
    return _json.loads(data)


