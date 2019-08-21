from django import template
register = template.Library()
import re

@register.simple_tag(takes_context=True)
def active(context, url):
    path = context['request'].path
    if re.search(url, path):
        return 'active'
    return ''
