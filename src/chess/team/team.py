from dataclasses import field
from typing import Dict, Optional, List

from chess.board.board import Board
from chess.common.config import ChessPieceConfig
from chess.common.constant import GameColor
from chess.common.geometry import Quadrant, Coordinate
from chess.common.piece import Piece

class Team:
    _id: int
    _home_quadrant: Quadrant
    _members: List[Piece]

    def __init__(self, team_id: int, home_quadrant: Quadrant, members: List[Piece]):
        self._id = team_id
        self._home_quadrant = home_quadrant
        for member in members:
            self._members.append(member)


    @property
    def id(self) -> int:
        return self._id


    @property
    def quadrant(self):
        return self._home_quadrant


    @property
    def members(self) -> List[Piece]:
        return self._members.copy()


    @property
    def piece_registry(self) -> Dict[int, Optional[Piece]]:
        return Dict(self._piece_registry)


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Team):
            return False
        return self._id == other.id


    @staticmethod
    def occupy_destination(self, piece: Piece, destination: Coordinate, board: Board):
       if piece is None:
           print("Bishop is None")
           return None
       if piece.current_position() is None:
           print("Bishop current position is None.")

           return None
       if board is None:
           print("Board is None")
           return None
       if not board.coordinate_is_valid(destination):
           print("Destination is not valid")
           return None
       if not DiagonalPattern.points_match_pattern(piece.current_position(), destination):
           print("points are not in diagonal pattern")
           return
       board.capture_square(piece, destination)