from client.http.requests_client import get, content
from client.content_types import json
from client.template import template
from client.compose import composable
from client.spec import specdoc, name, spec
from client.debug import trace
from pprint import pprint



get_page = name("get_page")(
    trace("data: ") + json + content + get() + trace("url:") + template("http://httpbin.org/get{?slug,page}",
                                                      required=("slug", ))
)


print specdoc(get_page)
get_page(slug="ericmoritz")
get_page(slug="ericmoritz", page=1)
