
from chess.square.service.square_service import SquareService
from chess.team.team_service import TeamService


class FieldController:
    _team_service: TeamService
    _square_service: SquareService

    def __init__(self, team_service: TeamService, square_service: SquareService):
        self._team_service = team_service
        self._square_service = square_service

