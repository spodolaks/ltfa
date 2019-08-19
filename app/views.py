from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render({}, request))

def news(request):
    template = loader.get_template('app/news.html')
    return HttpResponse(template.render({}, request))

def tournaments(request):
    template = loader.get_template('app/tournaments.html')
    return HttpResponse(template.render({}, request))

def events(request):
    template = loader.get_template('app/events.html')
    return HttpResponse(template.render({}, request))

def documents(request):
    template = loader.get_template('app/documents.html')
    return HttpResponse(template.render({}, request))

def aboutus(request):
    template = loader.get_template('app/aboutus.html')
    return HttpResponse(template.render({}, request))

def eshop(request):
    template = loader.get_template('app/eshop.html')
    return HttpResponse(template.render({}, request))
