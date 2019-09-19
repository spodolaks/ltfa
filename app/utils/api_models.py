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

    def getFirstPhase(self):
        return self.getPhase("FIRST_HALF");

    def getSecondPhase(self):
        return self.getPhase("SECOND_HALF");

    def getPhase(self, half="FIRST_HALF"):
        for l in self.list:
            if l.phase == half:
                return l
        return None;

class MatchPhase:
    def __init__(self, props):
        self.awayScore = props['awayScore'] if 'awayScore' in props else 0
        self.homeScore = props['homeScore'] if 'homeScore' in props else 0
        self.matchFifaId = props['matchFifaId'] if 'matchFifaId' in props else None
        self.phase = props['phase'] if 'phase' in props else ""
        self.phaseLength = props['phaseLength'] if 'phaseLength' in props else 0
        self.startDateTime = props['startDateTime'] if 'startDateTime' in props else "";

class MatchTeams:
    list = []
    def __init__(self, props):
        self.list = []
        if type(props) == list:
            for pr in props:
                self.list.append(MatchTeam(pr))

    def getHomeID(self):
        return self.getID("HOME")

    def getAwayID(self):
        return self.getID("AWAY")

    def getID(self, nature = "HOME"):
        for l in self.list:
            if l.teamNature == nature:
                return l.matchFifaId
        return "";

class MatchTeam:
    def __init__(self, props):
        self.matchFifaId = props['matchFifaId'] if 'matchFifaId' in props else None
        self.organisationFifaId = props['organisationFifaId'] if 'organisationFifaId' in props else ''
        self.teamFifaId = props['teamFifaId'] if 'teamFifaId' in props else ''
        self.teamNature = props['teamNature'] if 'teamNature' in props else ''

class MatchesTable:
    def __init__(self, props):
        matches = Matches(props);
        result = {};
        for match in matches.list:
            home_team_ID = match.matchTeams.getHomeID()
            away_team_ID = match.matchTeams.getAwayID();
            phase = match.matchPhases.getSecondPhase()
            home_score = phase.homeScore;
            away_score = phase.awayScore;
            home_points = self.ponts(home_score, away_score)
            away_points = self.ponts(away_score, home_score)

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

    def ponts(self, a = 0, b = 0):
        return 3 if a > b else 1 if a == b else 0

class Teams:
    pass

class Team:
    pass
