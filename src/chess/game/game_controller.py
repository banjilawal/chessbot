from typing import Optional

from chess.geometry.coordinate.coordinate import Coordinate
from chess.square.service.square_service import SquareService
from chess.team.model.piece import ChessPiece
from chess.team.team_service import TeamService


class GameController:
    _team_service: TeamService
    _square_service: SquareService

    def __init__(self, team_service: TeamService, square_service: SquareService):
        self._team_service = team_service
        self._square_service = square_service


    def find_chess_piece_at_coordinate(self, coordinate: Coordinate) -> Optional[ChessPiece]:
        return self._square_service.squares[][]

