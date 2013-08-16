from client.http.requests_client import get, content
from client.content_types import json
from client.template import template
from client.compose import composable
from client.spec import specdoc, name, spec
from pprint import pprint



uri_templates = {
    'frontmodules': template(
        "http://{host}:{port}/UxServices/UxFronts.svc/frontmodule/name/{site_id}/{front}",
        required=("host", "port", "front", "site_id")
    )
}

@composable
@spec("any", "any")
def trace(val):
    pprint(val)
    return val

get_frontmodules = name("get_frontmodules")(
    json + content + get() + trace + uri_templates['frontmodules']
)


print "ok."

print specdoc(get_frontmodules)
get_frontmodules(host="relaunch-web-dev.usatoday.com", port="2088", front="home", site_id=1)
