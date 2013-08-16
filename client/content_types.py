import json as _json
from client.compose import composable
from client.spec import spec, raises


@composable
@raises("ValueError")
@spec('string', 'dict | list | number | string | None')
def json(data):
    return _json.loads(data)


