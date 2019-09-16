from django.conf import settings
import requests
import datetime

class Api:
    def __init__(self, url = settings.API_URL):
        self.url = url

    def request(self, path = "", params = {}):
        try:
            return requests.get(self.url+path, params=params).json();
        except:
            return [];

    def get_competitions(self, from_data=(datetime.datetime.now().year - 1), to_data=(datetime.datetime.now().year)):
        print(from_data)
        print(to_data)
        return self.request("/competitions", {'from':from_data, 'to':to_data});

    def get_matches(self, competitionfifaid):
        return self.request("/matches", {'competitionfifaid':competitionfifaid});

    def get_matchevents(self, matchfifaid):
        return self.request("/matchevents", {'matchfifaid':matchfifaid});

    def get_person(self, personfifaid):
        return self.request("/matchevents", {'personfifaid':personfifaid});
