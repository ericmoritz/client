from itertools import chain


def spec(*arg_types, **kwarg_types):
    """
    Annotate what types the function accepts
    """
    def dec(f):
        f._spec = (arg_types, kwarg_types)
        return f
    return dec


@spec("function", "(tuple, dict) | None")
def get_spec(f):
    return getattr(f, "_spec", None)


@spec("spec", "anything")
def return_type(spec):
    (args, _) = spec
    return args[-1]


@spec("spec", "tuple")
def arg_types(spec):
    return spec[0][:-1]


@spec("spec", "dict")
def kwarg_types(spec):
    return spec[1]


def raises(*exceptions):
    """
    Annotate what exceptions are raised by the function
    """
    def dec(f):
        f._raises = exceptions
        return f
    return dec

def name(name_):
    def dec(f):
        f.__name__ = name_
        return f
    return dec


def specdoc(f):
    spec = getattr(f, "_spec", None)
    raises = getattr(f, "_raises", None)

    name = f.__name__
    
    if spec:
        ret = spec[0][-1]
        args = ", ".join(
            chain(
                (a for a in spec[0][:-1]), 
                ("{0}={1}".format(k,v) for k,v in spec[1].iteritems())
            )
        )

        return "{name}({args}) -> {ret}".format(**locals())
    else:
        return "{name}(*args, **kwargs) -> ???"
