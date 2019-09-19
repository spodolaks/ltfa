from django.conf import settings
import requests
import datetime
from .api_models import Competitions, Matches

class Api:
    def __init__(self, url = settings.API_URL):
        self.url = url

    def request(self, path = "", params = {}):
        try:
            return requests.get(self.url+path, params=params).json();
        except:
            return [];

    def get_competitions(self, from_data=(datetime.datetime.now().year - 1), to_data=(datetime.datetime.now().year)):
        return Competitions(self.request("/competitions", {'from':from_data, 'to':to_data}));

    def get_matches(self, competitionfifaid):
        return Matches(self.request("/matches", {'competitionfifaid':competitionfifaid}));

    def get_matches_table(self, competitionfifaid):
        matches = self.get_matches(competitionfifaid);
        result = {};
        for match in matches:
            home_team_ID = match['matchTeams'][0]['teamFifaId'];
            away_team_ID = match['matchTeams'][1]['teamFifaId'];
            match_phase = match['matchPhases'][1];
            home_score = match_phase['homeScore'] if 'homeScore' in match_phase else 0;
            away_score = match_phase['awayScore'] if 'awayScore' in match_phase else 0;
            home_points = 3 if home_score > away_score else 1 if home_score == away_score else 0;
            away_points = 3 if home_points == 0 else 1 if home_points == 1 else 0;
            if home_team_ID not in result:
                result[home_team_ID] = {
                    "id": home_team_ID,
                    "points": 0,
                    "matches": []
                }
            if away_team_ID not in result:
                result[away_team_ID] = {
                    "id": away_team_ID,
                    "points": 0,
                    "matches": []
                }
            result[home_team_ID]["matches"].append({
                "id": away_team_ID,
                "score": [home_score, away_score],
                "points": home_points
            });
            result[home_team_ID]["points"] += home_points;

            result[away_team_ID]["matches"].append({
                "id": home_team_ID,
                "score": [away_score, home_score],
                "points": away_points
            });
            result[away_team_ID]["points"] += away_points;
            resultarr = [];

            for r in result:
                resultarr.append(result[r]);

            resultarr.sort(key=lambda o: o["points"], reverse=True)


        return resultarr;

    def get_matchevents(self, matchfifaid):
        return self.request("/matchevents", {'matchfifaid':matchfifaid});

    def get_person(self, personfifaid):
        return self.request("/matchevents", {'personfifaid':personfifaid});
