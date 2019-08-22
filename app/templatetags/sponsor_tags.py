from django import template
from ..models import Sponsor
register = template.Library()

@register.simple_tag
def sponsors():
    return Sponsor.objects.all();
