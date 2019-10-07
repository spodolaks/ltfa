from django.conf import settings
import requests
import datetime
from .api_models import Competitions, Matches, MatchesTable, Teams, Team, Picture, Seasons

class Api:
    def __init__(self, url = settings.API_URL):
        self.url = url

    def request(self, path = "", params = {}):
        try:
            return requests.get(self.url+path, params=params).json();
        except:
            return [];

    def get_competitions(self, season=(datetime.datetime.now().year + 1)):
        return Competitions(self.request("/competitions", {'season': season}));

    def get_matches(self, competitionfifaid):
        return Matches(self.request("/matches", {'competitionfifaid': competitionfifaid}));

    def get_matches_table(self, competitionfifaid):
        return MatchesTable(
            self.request("/matches", {'competitionfifaid': competitionfifaid}),
            self.get_teams(competitionfifaid)
        )

    def get_matchevents(self, matchfifaid):
        return self.request("/matchevents", {'matchfifaid': matchfifaid});

    def get_person(self, personfifaid):
        return self.request("/matchevents", {'personfifaid': personfifaid});

    def get_teams(self, competitionfifaid):
        teams = self.request("/competitionteams", {'competitionfifaid': competitionfifaid})
        for t in teams:
            t['picture'] = self.get_picture(t['organisationFifaId']);
        return Teams(teams);

    def get_team(self, id):
        team = self.request("/team", {'id': id});
        team['picture'] = self.get_picture(team['organisationFifaId']);
        return Team(team);

    def get_picture(self, id, entity='organization'):
        return Picture(self.request("/picture", {'id': id, 'entity': entity}));

    def get_seasons(self):
        return Seasons(self.request("/seasons"));
