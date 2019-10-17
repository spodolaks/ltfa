from django.http import HttpResponse, HttpResponseNotFound
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.forms.models import model_to_dict
from .models import Page, News
from .utils.api import Api
from .utils.api_models import Matches, MatchesTable, Calendar, Facilities, Facility

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

def events(request, page):
    data = model_to_dict(page);
    api = Api()
    seasons = api.get_seasons().list;
    current_season = request.GET.get("season");
    if current_season not in seasons:
        current_season = next(iter(seasons))
    competitions = api.get_competitions(current_season);
    matches = [];
    for comp in competitions.list:
        matches_list = api.get_matches(comp.competitionFifaId).list
        teams = api.get_teams(comp.competitionFifaId);
        for m in matches_list:
            matches.append({
                "match": m,
                "competition": comp,
                "teams":[
                    teams.list[m.matchTeams.getHomeID()],
                    teams.list[m.matchTeams.getAwayID()]
                ],
                "facility": Facility(api.get_facility(m.facilityFifaId))
            })

    complete_matches = [x for x in matches if x["match"].status == "PLAYED"]
    next_matches = [x for x in matches if x["match"].status != "PLAYED"]
    complete_matches.sort(key=lambda x:x["match"].date)
    next_matches.sort(key=lambda x:x["match"].date)
    data.update({
        "current_season": current_season,
        "seasons": seasons,
        "competitions": competitions.list,
        "complete_matches": complete_matches,
        "next_matches": next_matches
    })
    return render(request, page.layout, data);

def tournaments(request, page):
    data = model_to_dict(page);
    api = Api()

    seasons = api.get_seasons().list;
    current_season = request.GET.get("season");
    if current_season not in seasons:
        current_season = next(iter(seasons))

    competitions = api.get_competitions(current_season);
    current_competition = competitions.getById(request.GET.get("competitionFifaId"));
    current_competition_ID = current_competition.competitionFifaId;
    matches = api.get_matches(current_competition_ID);
    teams = api.get_teams(current_competition_ID);
    matches_table = MatchesTable(matches, teams)
    facilities = Facilities()
    for m in matches.list:
        facilities.add(api.get_facility(m.facilityFifaId))
    calendar = Calendar(matches, teams, facilities)

    data.update({
        "current_season": current_season,
        "seasons": seasons,
        "competitions": competitions.list,
        "current_competition": current_competition,
        "current_competition_ID": current_competition_ID,
        "matches_table": matches_table.table,
        "matches": matches.list,
        "calendar": calendar.list
    })
    return render(request, page.layout, data);

def news_item(request, slug=''):
    p = get_object_or_404(News, slug=slug);
    return render(request, "app/default.html", model_to_dict(p));

def team(request, id=''):
    api = Api()
    team = api.get_team(id);
    if team.teamFifaId == "":
        return HttpResponseNotFound()
    return render(request, "app/team.html", {'team': team});
