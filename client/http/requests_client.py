from client.compose import composable
from client.spec import spec, raises, name
import requests


class HTTPError(Exception):
    def __init__(self, resp):
        self.resp = resp

    def __repr__(self):
        return "<HTTPError {0!r}>".format(self.resp)

def request_fun(method, **kwargs):
    @composable
    @raises('HttpError')
    @name("requests." + method)
    @spec('url', 'requests.Response')
    def request(url):
        resp = requests.request(method, url, **kwargs)
        status_code = resp.status_code
        if status_code >= 400 and status_code < 600:
            raise HTTPError(resp)
        else:
            return resp
    return request


@composable
@name("requests.content")
@spec('requests.Response', 'string')
def content(resp):
    """Return the response content"""
    return resp.content


def get(**kwargs):
    """Returns a partially applied GET request"""
    return request_fun('get', **kwargs)


def put(**kwargs):
    """Returns a partially applied PUT request"""
    return request_fun('put', **kwargs)


def post(**kwargs):
    """Returns a partially applied POST request"""
    return request_fun('post', **kwargs)


def delete(**kwargs):
    """Returns a partially applied DELETE request"""
    return request_fun('delete', **kwargs)


def head(**kwargs):
    """Returns a partially applied HEAD request"""
    return request_fun('head', **kwargs)

def options(**kwargs):
    """Returns a partially applied OPTIONS request"""
    return request_fun('options', **kwargs)

