client
======

experimental rest client with the goal of enabling composable stateless and self documenting RESTful clients.


Example
---------


```python 

get_json = compose_all(json, content, get(), trace("url:"))

get_page = autodoc(
    compose(get_json, template("http://httpbin.org/get{?slug,page}", required=("slug", ))),
    name="get_page",
    doc="Returns a simulated restful call"
)
```
