from django import template
from ..models import Page
register = template.Library()

@register.simple_tag
def pages():
    return Page.objects.all();

@register.simple_tag
def home_page():
    return Page.objects.get(is_home_page=True);

@register.simple_tag
def menu_pages(split=False):
    p = Page.objects.filter(show_in_menu=True);
    if(split):
        l = len(p) // 2;
        return p[:l], p[l:];
    else:
        return p;

@register.simple_tag
def page_by_layout(layout):
    try:
        return Page.objects.get(layout='templates/app/'+layout+'.html')
    except Content.DoesNotExist:
        return None
