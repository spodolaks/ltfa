from django import template
from ..utils.api import Api
from ..utils.api_models import Facility
register = template.Library()

@register.simple_tag
def nextmatch():
    api = Api()
    match = api.get_nextmatch();
    facility = Facility(api.get_facility(match.facilityFifaId))
    competition = api.get_competition(match.competitionFifaId)
    result = {
        "match": match,
        "teams": [
            api.get_team(match.matchTeams.getHomeID()),
            api.get_team(match.matchTeams.getAwayID())
        ],
        "facility": facility,
        "competition": competition
    }
    return result;
