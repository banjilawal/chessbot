
from abc import ABC, abstractmethod
from typing import Dict, Optional

from chess.board.board import Board
from chess.common.geometry import Coordinate
from chess.common.piece import Piece
from chess.motion.logic.diagonal_pattern import GeometryPattern
from chess.team.home import TeamHome

# if TYPE_CHECKING:
#     from chess.board.board import Board


class MovementStrategy(ABC):
    _motion_definitions: {}
    """ A MovementStrategy is a collection of MoveRules that logic how a piece can move."""

    def __init__(self, motion_definitions: list[GeometryPattern]):
        self._motion_definitions = {}
        for definition in motion_definitions:
            if definition.id not in self._motion_definitions:
                self._motion_definitions[definition.id] = definition


    @property
    def motion_definitions(self) -> Dict[int, GeometryPattern]:
        return self._motion_definitions.copy()


    def check_basic_conditions(self, chess_piece: Piece, board: Board, destination: 'Coordinate') -> bool:
        if chess_piece is None:
            print("[Warning] Mover cannot be None. It cannot move.")
            return False
        if board is None:
            print("[Warning] PodBoard cannot be None. Cannot move.")
            return False
        if chess_piece.coordinate is None:
            print("[Warning] chess_piece has not coordinate. Cannot move.")
            return False
        if destination is None:
            print("[Warning] Destination coordinate cannot be None. Cannot move.")
            return False
        return True

    @abstractmethod
    def move(self, chess_piece: Piece, board: Board, destination: Coordinate) -> bool:
        """Perform the move if valid. Return True if successful, False otherwise."""
        pass

    @abstractmethod
    def path_exists(self, origin: Coordinate, destination: Coordinate) -> bool:
        pass

    @abstractmethod
    def possible_destinations(self, origin: Coordinate, board: Board, team_home: Optional[TeamHome] = None) -> list[Coordinate]:
        """Return a list of valid destinations from the given origin."""
        pass



