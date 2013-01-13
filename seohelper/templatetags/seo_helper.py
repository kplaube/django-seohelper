import re
from django import template
from seohelper.models import Document

register = template.Library()


class SeoHelperNode(template.Node):
    def __init__(self, url, var_name):
        self.url = template.Variable(url)
        self.var_name = var_name

    def render(self, context):
        url = self.url.resolve(context)
        m = re.search('^(?P<url>[\w_\-\.\:\/]+)\?(.*)', url)
        if m:
            url = m.groups()[0]

        try:
            meta = Document.objects.get(url=url)
        except Document.DoesNotExist:
            meta = ''

        context[self.var_name] = meta
        return ''


@register.tag('seo_helper')
def do_seo_helper(parser, token):
    """
    Gets the metadata (description, keywords, robots, etc) stored in the
    database using an url as parameter.

    Usage::

        {% load seo_helper %}
        {% seo_helper request.path as meta %}

        <title>{{ meta.title }}</title>
        <meta name="description" content="{{ meta.description }}" />
        <meta name="keywords" content="{{ meta.keywords }}" />
        <meta name="robots" content="{{ meta.robot_tags }}" />
    """
    try:
        tag_name, arg = token.contents.split(None, 1)
    except ValueError:
        raise (template.TemplateSyntaxError("%r tag requires arguments" \
            % token.contents.split()[0]))

    m = re.search(r'(.*?) as (\w+)', arg)
    if not m:
        raise template.TemplateSyntaxError("%r tag had invalid arguments" \
            % tag_name)

    format_string, var_name = m.groups()
    return SeoHelperNode(format_string, var_name)
