
from abc import ABC, abstractmethod
from typing import Dict, List

from chess.geometry.board import Board
from chess.geometry.coordinate import Coordinate
from chess.piece.piece import Piece

# if TYPE_CHECKING:
#     from chess.board.board import Board


class SearchPattern(ABC):
    _motion_definitions: {}
    """ A SearchPattern is a collection of MoveRules that logic how a piece can move."""

    def __init__(self):
        pass


    def search(self, piece: Piece, board: Board) -> list[Coordinate]:
        if not self.validate_search_parameters(piece, board):
            return []
        return self._perform_search(piece, board)


    def validate_search_parameters(self, piece: Piece, board: Board) -> bool:
        if piece is None:
            raise ValueError("[Warning] Cannot search for places with a null piece. Destination search is impossible.")
        if piece.current_position() is None:
            raise ValueError("Cannot search for destinations if the piece does not have coordinate on the board.")
        if board is None:
            raise ValueError("Cannot search for destinations when the board is null.")
        return True

    @abstractmethod
    def _perform_search(self, piece: Piece, board: Board) -> List[Coordinate]:
        """Concrete classes implement the actual search logic."""
        pass





