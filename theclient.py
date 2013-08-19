from client.http.requests_client import get, content
from client.content_types import json
from client.template import template
from client.spec import autodoc
from client.debug import trace
from client.compose import compose_all
from pprint import pprint


get_page = autodoc(
    compose_all(
        json, content, get(), trace("url:"),
        template("http://httpbin.org/get{?slug,page}", required=("slug", ))
   ),
    name="get_page",
    doc="Returns a simulated restful call"
)


print get_page.__doc__
print
pprint(get_page(slug="ericmoritz"))
pprint(get_page(slug="ericmoritz", page=1))
