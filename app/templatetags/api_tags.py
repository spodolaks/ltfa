from django import template
register = template.Library()
import datetime
from ..utils.api import Api

api = Api();

@register.simple_tag
def get_competitions(from_data=(datetime.datetime.now().year), to_data=(datetime.datetime.now().year + 1)):
    return api.get_competitions(from_data, to_data);

@register.simple_tag
def get_matches(competitionfifaid):
    return api.get_matches(competitionfifaid)

@register.simple_tag
def get_matches_table(competitionfifaid):
    matches = get_matches(competitionfifaid);
    teams = [];
    for m in matches:
        team1 = m['matchTeams'][0];
        team2 = m['matchTeams'][1];
        if len(list(filter(lambda o: o['teamFifaId'] == team1['teamFifaId'], teams))) == 0:
            teams.append({'teamFifaId':team1['teamFifaId']});
        if len(list(filter(lambda o: o['teamFifaId'] == team2['teamFifaId'], teams))) == 0:
            teams.append({'teamFifaId':team2['teamFifaId']});

    return teams;

@register.simple_tag
def get_matchevents(matchfifaid):
    return api.get_matchevents(matchfifaid);

@register.simple_tag
def get_person(personfifaid):
    return get_person(personfifaid);
