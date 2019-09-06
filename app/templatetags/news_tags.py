from django import template
from django.urls import reverse
from ..models import News
register = template.Library()

@register.simple_tag
def news(count=10, start=0):
    return News.objects.order_by('-date')[start:start+count];

@register.simple_tag
def news_count():
    return News.objects.count();

@register.simple_tag
def compose_news(data):
    result = [];
    for d in data:
        result.append({
            'title': d.title,
            'datpublished': d.datpublished(),
            'url': reverse('news', kwargs={'slug': d.slug}),
            'image': d.image
        });
    return result;
