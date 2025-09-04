from typing import List, Optional

from chess.common.color import GameColor
from chess.geometry.quadrant import Quadrant
from chess.competitor.model import Competitor
from chess.side.model import Side


class TeamRepo:
    _teams: List[Side]

    def __init__(self,):
        self._teams = []


    def __len__(self):
        return len(self._teams)


    def add(self, team: Side):
        if team not in self._teams and team is not None:
            self._teams.append(team)


    def team_by_id(self, team_id: int) -> Optional[Side]:
        for team in self._teams:
            if team.id == team_id:
                return team
        return None


    def teams_by_owner(self, owner: Competitor) -> List[Side]:
        matches: List[Side] = []

        for team in self._teams:
            if team.controller == owner and team not in matches:
                matches.append(team)
        return matches


    def teams_by_color(self, color: GameColor) -> List[Side]:
        matches: List[Side] = []

        for team in self._teams:
            if team.color == color and team not in matches:
                matches.append(team)
        return matches


    def teams_by_quadrant(self, quadrant: Quadrant) -> List[Side]:
        matches: List[Side] = []

        for team in self._teams:
            if team.home_quadrant == quadrant and team not in matches:
                matches.append(team)
        return matches

