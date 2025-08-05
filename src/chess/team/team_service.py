from typing import List, Optional

from chess.common.game_color import GameColor
from chess.team.model.team import Team


class TeamService:
    _teams: List[Team]

    def __init__(self, teams: List[Team]):
        self._teams = teams

    @property
    def teams(self) -> List[Team]:
        return self._teams


    def size(self) -> int:
        return len(self._teams)


    def find_team_by_id(self, team_id: int) -> Optional[Team]:
        for team in self._teams:
            if team.id == team_id:
                return team
        return None


    def find_team_by_color(self, color: GameColor) -> Optional[Team]:
        for team in self._teams:
            if team.color == color:
                return team
        return None