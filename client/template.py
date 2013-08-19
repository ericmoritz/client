from client.spec import spec
from purl import Template
from purl import template as ptemplate

##====================================================================
## Public
##====================================================================
@spec('string', 'string')
def template(tpl_str, required=None):
    """Creates a uri_template function"""
    tpl = Template(tpl_str)
    spec_kwargs = {k:"string" for k in template_vars(tpl_str)}

    @spec("url", **spec_kwargs)
    def uri_template(**kwargs):
        validate_required_keys(required, kwargs.keys())

        return tpl.expand(kwargs).as_string()
    return uri_template


##====================================================================
## Internal
##====================================================================
def validate_required_keys(required, provided):
    required_set = set(required)
    provided_set = set(provided)
    missing      = required_set - provided_set
    if missing:
        raise TypeError("Required Keyword args not provided: {kwargs}".format(
                kwargs=", ".join(missing)))


def template_vars(templ):
    matches = ptemplate.patterns.finditer(templ)
    keys = []

    for match in matches:
        expression = match.group(1)
        _, _, split_fn, _, _ = ptemplate.operator_map.get(
            expression[0], ptemplate.defaults)
        keys.extend(key for key, _, _ in split_fn(expression))
    return keys


