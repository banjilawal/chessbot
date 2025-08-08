from typing import List

from chess.geometry.coordinate.coordinate import Coordinate
from chess.map.element.square import Square
from chess.map.map_service import MapService
from engine.explorer import Explorer
from chess.team.element.piece import ChessPiece
from chess.team.team_service import TeamService


class Arena:
    _id: int
    _team_service: TeamService
    _map_service: MapService

    def __init__(self, arena_id: int, team_service: TeamService, map_service: MapService):
        self._id = arena_id
        self._team_service = team_service
        self._map_service = map_service

    @property
    def id(self) -> int:
        return self._id


    @property
    def team_service(self) -> TeamService:
        return self._team_service


    @property
    def map_service(self) -> MapService:
        return self._map_service


    def execute_move(self, chess_piece_id: int, destination: Coordinate):
        chess_piece = self._team_service.find_chess_piece_by_id(chess_piece_id)

        if chess_piece is  None:
            raise ValueError(f"ChessPiece with ID {chess_piece_id} not found.")
        origin = chess_piece.coordinate_stack.current_coordinate()

        if not chess_piece.rank.walk.is_walkable(origin, destination):
            raise ValueError(
                f"Destination {destination} is not reachable from {origin} by a "
                f"{chess_piece.rank.walk.__class__.__name__}"
            )
        self._map_service.capture_square(chess_piece, destination)



