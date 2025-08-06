
from chess.grid.service.grid_service import GridService
from chess.team.team_service import TeamService


class BoardController:
    _team_service: TeamService
    _square_service: GridService

    def __init__(self, team_service: TeamService, square_service: GridService):
        self._team_service = team_service
        self._square_service = square_service

    @property
    def team_service(self) -> TeamService:
        return self._team_service

    @property
    def square_service(self) -> GridService:
        return self._square_service

