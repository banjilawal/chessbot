
from chess.square.service.square_service import SquareService
from chess.team.team_service import TeamService


class BoardController:
    _team_service: TeamService
    _square_service: SquareService

    def __init__(self, team_service: TeamService, square_service: SquareService):
        self._team_service = team_service
        self._square_service = square_service

    @property
    def team_service(self) -> TeamService:
        return self._team_service

    @property
    def square_service(self) -> SquareService:
        return self._square_service

