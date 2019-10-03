from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.forms.models import model_to_dict
from .models import Page, News
from .utils.api import Api

def pages(request, url=''):
    if url == '':
        composed_url = '/';
    else:
        composed_url = ('' if url[0] == '/' else '/') + url + ('' if url[len(url) - 1] == '/' else '/')
    p = get_object_or_404(Page, url=composed_url, is_visible=True, published=True)
    layout = p.layout.replace("templates/app/","").replace(".html","")
    if layout in globals():
        return globals()[layout](request, p)
    else:
        return render(request, p.layout, model_to_dict(p));

def tournaments(request, page):
    data = model_to_dict(page);
    api = Api()
    competitions = api.get_competitions().list;
    current_competition = competitions[0] if len(competitions) > 0 else {};
    current_competition_ID =  current_competition.competitionFifaId;
    matches_table = api.get_matches_table(current_competition_ID);
    teams = api.get_teams(current_competition_ID);
    data.update({
        "competitions": competitions,
        "matches_table": matches_table.table,
        "teams": teams.list
    })
    return render(request, page.layout, data);

def news(request, slug=''):
    p = get_object_or_404(News, slug=slug);
    return render(request, "app/default.html", model_to_dict(p));

def team(request, id=''):
    api = Api()
    team = api.get_team(id);
    if team.teamFifaId == "":
        return HttpResponseNotFound()
    return render(request, "app/team.html", {'team': team});
