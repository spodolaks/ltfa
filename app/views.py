from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.forms.models import model_to_dict
from .models import Page, News

def pages(request, slug=''):
    p = get_object_or_404(Page, slug=slug);
    return render(request, p.layout, model_to_dict(p));

def news(request, slug=''):
    p = get_object_or_404(News, slug=slug);
    return render(request, "app/default.html", model_to_dict(p));
