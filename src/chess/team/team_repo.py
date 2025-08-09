from typing import List, Optional

from chess.team.element.team import Team


class TeamRepo:
    _teams: List[Team]

    def __init__(self,):
        self._chess_pieces = []


    def add(self, team: Team):
        if team not in self._teams and team is not None:
            self._teams.append(team)


    def find(self, team_id: int) -> Optional[Team]:
        for team in self._teams:
            if team.id == team_id:
                return team
        return None


    def filter_by_owner_id(self, owner_id: int) -> List[Team]:
        matches: List[Team] = []

        for team in self._teams:
            if team.owner.id == owner_id and team not in matches:
                matches.append(team)
        return matches

