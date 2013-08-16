from client.compose import composable
from spec import spec, name
from pprint import pformat

def trace(msg):
    @composable
    @name("trace")
    @spec("any", "any")
    def inner(val):
        print msg, pformat(val)
        return val
    return inner
