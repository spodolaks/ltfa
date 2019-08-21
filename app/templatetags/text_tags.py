from django import template
from ..models import Text
register = template.Library()

@register.simple_tag
def texts(slug=''):
    if(slug == ''):
        return Text.objects.all();
    else:
        return  Text.objects.filter(slug=slug);

@register.simple_tag
def text(slug):
    try:
        return  Text.objects.get(slug=slug);
    except Text.DoesNotExist:
        return None
