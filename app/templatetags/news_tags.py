from django import template
from ..models import News
register = template.Library()

@register.simple_tag
def news(count=10, start=0):
    return News.objects.order_by('-date')[start:start+count];

@register.simple_tag
def news_count():
    return News.objects.count();
\
