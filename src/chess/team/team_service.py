from typing import List, Optional

from chess.common.game_color import GameColor
from chess.geometry.quadrant import Quadrant
from chess.owner.owner import Owner
from chess.team.team_repo import TeamRepo
from chess.team.team import Team

# if TYPE_CHECKING:
#     from chess.team.square.team import Team


class TeamService:
    _repo: TeamRepo

    def __init__(self, team_repo: TeamRepo):
        self._repo = team_repo


    def size(self) -> int:
        return self._repo.__len__()


    def add_team(self, team: Team):
        self._repo.add(team)


    def find_team_by_id(self, team_id: int) -> Optional[Team]:
        return self._repo.team_by_id(team_id)


    def filter_teams_by_owner(self, owner: Owner) -> List[Team]:
        return self._repo.teams_by_owner(owner)


    def filter_teams_by_color(self, color: GameColor) -> List[Team]:
        return self._repo.teams_by_color(color)


    def filter_teams_by_quadrant(self, quadrant: Quadrant) -> List[Team]:
        return self._repo.teams_by_quadrant(quadrant)
