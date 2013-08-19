client
======

experimental rest client with the goal of enabling composable stateless and self documenting RESTful clients.


Example
---------


```python 
from client.http.requests_client import get, content
from client.content_types import json
from client.template import template
from client.spec import autodoc
from client.debug import trace
from client.compose import compose_all, compose

get_json = compose_all(json, content, get(), trace("url:"))

get_page = autodoc(
    compose(get_json, template("http://httpbin.org/get{?slug,page}", required=("slug", ))),
    name="get_page",
    doc="Returns a simulated restful call"
)
```

Usage
~~~~~~~

```python

>>> get_page(slug="test")
url: u'http://httpbin.org/get?slug=test'
{u'url': u'http://httpbin.org/get?slug=test', u'headers': {u'Connection': u'close', u'Host': u'httpbin.org', u'Accept-Encoding': u'gzip, deflate, compress', u'Accept': u'*/*', u'User-Agent': u'python-requests/1.2.3 CPython/2.7.1 Darwin/11.4.2'}, u'args': {u'slug': u'test'}, u'origin': u'159.54.131.7'}
>>> print get_page.__doc__
get_page(slug=string, page=string) -> dict | list | number | string | None

Returns a simulated restful call
>>>
```

You will notice that `get_page` says it returns a `dict | list | number | string | None`.  

This is the return type of the `client.content_types.json` function.  `client` provides a rudimentary type 
documentation system which `compose` and `compose_all` to automatically document the type documentation.
