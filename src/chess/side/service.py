from typing import List, Optional

from chess.common.color import GameColor
from chess.geometry.quadrant import Quadrant
from chess.competitor.model import Competitor
from chess.side.repo import TeamRepo
from chess.side.team import Side

# if TYPE_CHECKING:
#     from chess.side.square.side import Team


class TeamService:
    _repo: TeamRepo

    def __init__(self, team_repo: TeamRepo):
        self._repo = team_repo


    def size(self) -> int:
        return self._repo.__len__()


    def add_team(self, team: Side):
        self._repo.add(team)


    def find_team_by_id(self, team_id: int) -> Optional[Side]:
        return self._repo.team_by_id(team_id)


    def filter_teams_by_owner(self, owner: Competitor) -> List[Side]:
        return self._repo.teams_by_owner(owner)


    def filter_teams_by_color(self, color: GameColor) -> List[Side]:
        return self._repo.teams_by_color(color)


    def filter_teams_by_quadrant(self, quadrant: Quadrant) -> List[Side]:
        return self._repo.teams_by_quadrant(quadrant)
