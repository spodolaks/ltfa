class Competitions:
    list = []
    def __init__(self, props):
        self.list = []
        if type(props) == list:
            for pr in props:
                self.list.append(Competition(pr))

class Competition:
    def __init__(self, props = {}):
        self.ageCategory = props['ageCategory'] if 'ageCategory' in props else ''
        self.ageCategoryName = props['ageCategoryName'] if 'ageCategoryName' in props else ''
        self.competitionFifaId = props['competitionFifaId'] if 'competitionFifaId' in props else ''
        self.dateTo = props['dateTo'] if 'dateTo' in props else ''
        self.discipline = props['discipline'] if 'discipline' in props else ''
        self.gender = props['gender'] if 'gender' in props else ''
        self.imageId = props['imageId'] if 'imageId' in props else None
        self.internationalName = props['internationalName'] if 'internationalName' in props else ''
        self.internationalShortName = props['internationalShortName'] if 'internationalShortName' in props else ''
        self.matchType: props['matchType'] if 'matchType' in props else ''
        self.multiplier = props['multiplier'] if 'multiplier' in props else 1
        self.nature = props['nature'] if 'nature' in props else ''
        self.numberOfParticipants = props['numberOfParticipants'] if 'numberOfParticipants' in props else 1
        self.organisationFifaId: props['organisationFifaId'] if 'organisationFifaId' in props else None
        self.season = props['season'] if 'season' in props else None
        self.status = props['status'] if 'status' in props else ''
        self.superiorCompetitionFifaId = props['superiorCompetitionFifaId'] if 'superiorCompetitionFifaId' in props else None
        self.teamCharacter = props['teamCharacter'] if 'teamCharacter' in props else ''

class Matches:
    list = []
    def __init__(self, props):
        self.list = []
        if type(props) == list:
            for pr in props:
                self.list.append(Match(pr))

class Match:
    def __init__(self, props = {}):
        self.competitionFifaId =  props['competitionFifaId'] if 'competitionFifaId' in props else ''
        self.dateTimeLocal =  props['dateTimeLocal'] if 'dateTimeLocal' in props else ''
        self.facilityFifaId =  props['facilityFifaId'] if 'facilityFifaId' in props else ''
        self.matchDay =  props['matchDay'] if 'matchDay' in props else None
        self.matchFifaId =  props['matchFifaId'] if 'matchFifaId' in props else ''
        self.matchOrderNumber =  props['matchOrderNumber'] if 'matchOrderNumber' in props else None
        self.matchPhases = MatchPhases(props['matchPhases']);
        self.matchTeams = MatchTeams(props['matchTeams'])
        self.resultSupplement = props['resultSupplement'] if 'resultSupplement' in props else ''
        self.resultSupplementHome = props['resultSupplementHome'] if 'resultSupplementHome' in props else None
        self.status =  props['status'] if 'status' in props else ''

class MatchPhases:
    list = []
    def __init__(self, props):
        self.list = []
        if type(props) == list:
            for pr in props:
                self.list.append(MatchPhase(pr))

class MatchPhase:
    def __init__(self, props):
        self.awayScore = props['awayScore'] if 'awayScore' in props else 0
        self.homeScore = props['homeScore'] if 'homeScore' in props else 0
        self.matchFifaId = props['matchFifaId'] if 'matchFifaId' in props else None
        self.phase = props['phase'] if 'phase' in props else ""
        self.phaseLength = props['phaseLength'] if 'phaseLength' in props else 0
        self.startDateTime = props['startDateTime'] if 'startDateTime' in props else ""

class MatchTeams:
    list = []
    def __init__(self, props):
        self.list = []
        if type(props) == list:
            for pr in props:
                self.list.append(MatchTeam(pr))

class MatchTeam:
    def __init__(self, props):
        self.matchFifaId = props['matchFifaId'] if 'matchFifaId' in props else None
        self.organisationFifaId = props['organisationFifaId'] if 'organisationFifaId' in props else ''
        self.teamFifaId = props['teamFifaId'] if 'teamFifaId' in props else ''
        self.teamNature = props['teamNature'] if 'teamNature' in props else ''

class Teams:
    pass

class Team:
    pass
