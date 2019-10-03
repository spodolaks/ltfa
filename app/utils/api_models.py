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
                return l.teamFifaId
        return "";

class MatchTeam:
    def __init__(self, props):
        self.matchFifaId = props['matchFifaId'] if 'matchFifaId' in props else None
        self.organisationFifaId = props['organisationFifaId'] if 'organisationFifaId' in props else ''
        self.teamFifaId = props['teamFifaId'] if 'teamFifaId' in props else ''
        self.teamNature = props['teamNature'] if 'teamNature' in props else ''

class MatchesTable:
    table = [];
    def __init__(self, props):
        matches = Matches(props);
        self.__table = {};
        for match in matches.list:
            home_team_ID = match.matchTeams.getHomeID()
            away_team_ID = match.matchTeams.getAwayID()
            phase = match.matchPhases.getSecondPhase()
            self.__append_match(home_team_ID, away_team_ID, [phase.homeScore, phase.awayScore])
        self.__points_percents();
        self.__sort_table();
        self.__append_teams();

    def __init_team(self, id = 0):
        if id not in self.__table:
            self.__table[id] = {
                "id": id,
                "points": 0,
                "total_score": [0,0],
                "opponents": {}
            }
        return self.__table;

    def __init_opponent(self, id = 0, parent_id=0):
        self.__init_team(parent_id);
        if id not in self.__table[parent_id]["opponents"]:
            self.__table[parent_id]["opponents"][id] = {
                "id": id,
                "matches": []
            }
        return self.__table;

    def __append_match(self, id = 0, opponent_id = 0, score= [0,0]):
        away_score = [score[1], score[0]]
        home_points = self.__points(score[0], score[1])
        away_points = self.__points(score[1], score[0])
        self.__init_opponent(opponent_id, id);
        self.__init_opponent(id, opponent_id);
        self.__table[id]["opponents"][opponent_id]["matches"].append({
            "score": score,
            "points": home_points
        });
        self.__table[opponent_id]["opponents"][id]["matches"].append({
            "score": away_score,
            "points": away_points
        });
        self.__table[id]["points"] += home_points;
        self.__table[id]["total_score"][0] += score[0];
        self.__table[id]["total_score"][1] += score[1];
        self.__table[opponent_id]["points"] += away_points;
        self.__table[opponent_id]["total_score"][0] += away_score[0];
        self.__table[opponent_id]["total_score"][1] += away_score[1];
        return self.__table

    def __points(self, a = 0, b = 0):
        return 3 if a > b else 1 if a == b else 0

    def __sort_table(self):
        self.table = [];
        for t in self.__table:
            self.table.append(self.__table[t]);
        self.table.sort(key=lambda o: o["points"], reverse=True)
        ids = [];
        for t in self.table:
            ids.append(t["id"]);
        for t in self.table:
            opponents = [];
            for id in ids:
                if id in t["opponents"]:
                    opponents.append(t["opponents"][id]);
            t["opponents"] = opponents;
        return self.table

    def __points_percents(self):
        print(self.__table)
        pass
    def __append_teams(self):
        pass

class Teams:
    list = {}
    def __init__(self, props):
        self.list = {}
        if type(props) == list:
            for pr in props:
                team = Team(pr);
                self.list[team.teamFifaId] = team;

class Team:
    def __init__(self, props):
        self.competitionFifaId = props['competitionFifaId'] if 'competitionFifaId' in props else ""
        self.country = props['country'] if 'country' in props else ""
        self.internationalName = props['internationalName'] if 'internationalName' in props else ""
        self.internationalShortName = props['internationalShortName'] if 'internationalShortName' in props else ""
        self.organisationFifaId = props['organisationFifaId'] if 'organisationFifaId' in props else ""
        self.organisationName = props['organisationName'] if 'organisationName' in props else ""
        self.organisationNature = props['organisationNature'] if 'organisationNature' in props else ""
        self.organisationShortName = props['organisationShortName'] if 'organisationShortName' in props else ""
        self.status = props['status'] if 'status' in props else ""
        self.teamFifaId = props['teamFifaId'] if 'teamFifaId' in props else ""
