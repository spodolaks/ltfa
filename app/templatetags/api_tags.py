from django import template
register = template.Library()
import requests
import json
from django.conf import settings
import datetime

@register.simple_tag
def get_competitions(from_data=2000, to_data=(datetime.datetime.now().year + 1)):
    try:
        return requests.get(settings.API_URL+"/competitions", params={'from':from_data, 'to':to_data}).json();
    except:
        return [];

@register.simple_tag
def get_matches(competitionfifaid):
    try:
        return requests.get(settings.API_URL+"/matches", params={'competitionfifaid':competitionfifaid}).json();
    except:
        return [];

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
        # team1 = m['matchTeams'][0]['teamFifaId'];
        # team2 = m['matchTeams'][1]['teamFifaId'];
        # if team1 not in teams:
        #     teams.append(team1);
        # if team2 not in teams:
        #     teams.append(team2);
    # return matches;

@register.simple_tag
def get_matchevents(matchfifaid):
    try:
        return requests.get(settings.API_URL+"/matchevents", params={'matchfifaid':matchfifaid}).json();
    except:
        return [];

@register.simple_tag
def get_person(matchfifaid):
    try:
        return requests.get(settings.API_URL+"/person", params={'personfifaid':personfifaid}).json();
    except:
        return [];
