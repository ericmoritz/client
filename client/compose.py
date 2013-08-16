from client.spec import (
    get_spec, return_type, arg_types, kwarg_types, specdoc)

##====================================================================
## Public
##====================================================================

def composable(f):
    return Composable(f)


##====================================================================
## Internal
##====================================================================
def compose(f, g):
    def inner(*args, **kwargs):
        return f(g(*args, **kwargs))
    docs = (d for d in [g.__doc__, f.__doc__] if d)
    inner.__doc__ = "\n--\n\n".join(docs)
    inner._spec = compose_specs(f, g)
    validate_composition(f, g)
    inner.__name__ = "{1}+{0}".format(f.__name__, g.__name__)
    return inner


def validate_composition(f, g):
    f_spec = get_spec(f)
    g_spec = get_spec(g)

    if f_spec and g_spec:
        g_ret = return_type(g_spec)
        f_in  = arg_types(f_spec)
        arity = len(f_in)
        is_any = g_ret == 'any' or f_in[0] == 'any'
        types_match = (arity == 1 or f_in[0] == g_ret)
        if not (is_any or types_match):
            raise TypeError("Can not compose {gdoc} with {fdoc}".format(
                    gdoc=specdoc(g),
                    fdoc=specdoc(f)))

def compose_specs(f, g):
    f_spec = get_spec(f)
    g_spec = get_spec(g)

    if f_spec and g_spec:
        # take the return type of f
        f_ret = return_type(f_spec)

        # and the input args of g without its return type
        g_in  = arg_types(g_spec)
        # splice the g_in with the return of f
        return (
            arg_types(g_spec) + (return_type(f_spec), ),
        # and the kwargs of g
            kwarg_types(g_spec)
        )


class Composable(object):
    def __init__(self, f):
        self.f = f
        self.__name__ = f.__name__
        self._patch_spec(self.f)

    def __add__(self, g):
        return Composable(compose(self.f, g))

    def __call__(self, *args, **kwargs):
        return self.f(*args, **kwargs)

    def __repr__(self):
        return ""

    def _patch_spec(self, f):
        self._spec = getattr(f, "_spec", None)
