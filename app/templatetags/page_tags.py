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

@register.simple_tag
def compose_page_number(num=""):
    try:
        result = int(num)
        if result > 0:
            return result;
        else:
            return 1;
    except:
        return 1;

@register.simple_tag
def pagination(count=1, current=1, url="?page={0}"):
    offset = 3
    result = [];
    if count > 1:
        if current > 1:
            result.append({
                'url': url.format(current - 1),
                'title': "<",
            });
        dots_added = False;
        for i in range(1, count + 1):
            print(dots_added);
            if i <= offset or i > count - offset or (i > current - offset and i < current + offset):
                dots_added = False;
                result.append({
                    'url': url.format(i),
                    'active': i == current,
                    'title': i,
                });
            elif dots_added == False:
                dots_added = True;
                result.append({
                    'title': ".&nbsp;.&nbsp;.",
                });
        if current < count:
            result.append({
                'url': url.format(current + 1),
                'title': ">",
            });
    return result;
