from django import template
register = template.Library()

@register.simple_tag(name='range')
def num_range(start=0, stop=0, step=1):
    return range(start, stop + 1, step);
