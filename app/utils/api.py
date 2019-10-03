from django.conf import settings
import requests
import datetime
from .api_models import Competitions, Matches, MatchesTable, Teams, Team

class Api:
    def __init__(self, url = settings.API_URL):
        self.url = url

    def request(self, path = "", params = {}):
        try:
            return requests.get(self.url+path, params=params).json();
        except:
            return [];

    def get_competitions(self, from_data=(datetime.datetime.now().year - 1), to_data=(datetime.datetime.now().year)):
        return Competitions(self.request("/competitions", {'from': from_data, 'to': to_data}));

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
        return Teams(self.request("/competitionteams", {'competitionfifaid': competitionfifaid}));

    def get_team(self, id):
        return Team(self.request("/team", {'id': id}));
