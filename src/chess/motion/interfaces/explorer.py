
from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

from chess.geometry.coordinate.coordinate import Coordinate
from chess.map.map_service import MapService

if TYPE_CHECKING:
    from chess.team.model.piece import ChessPiece


class Explorer(ABC):
    _motion_definitions: {}
    """ A MoveGenerator is a collection of MoveRules that walk how a chess_piece can move."""

    def __init__(self):
        pass

    @abstractmethod
    def discover_destinations(self, chess_piece: ChessPiece,  map_service: MapService) -> List[Coordinate]:
        pass
        """Returns a list of coordinates that the chess_piece can reach from its current position."""

    #
    # def search(self, chess_piece: 'ChessPiece', board: 'ChessBoard') -> list[Coordinate]:
    #     if not self.validate_search_parameters(chess_piece, board):
    #         return []
    #     return self._perform_search(chess_piece, board)
    #
    #
    # def validate_search_parameters(self, chess_piece: 'ChessPiece', board: 'ChessBoard') -> bool:
    #     if chess_piece is None:
    #         raise ValueError("[Warning] Cannot search for places with a null chess_piece. Destination search is impossible.")
    #     if chess_piece.current_coordinate() is None:
    #         raise ValueError(f"{chess_piece.label} has a null coordinate. The chess_piece must be on the chess_board to do a search.")
    #     if board is None:
    #         raise ValueError("Cannot search for destinations when the chess_board is null.")
    #     return True
    #
    # @abstractmethod
    # def _perform_search(self, chess_piece: 'ChessPiece', board: 'ChessBoard') -> List[Coordinate]:
    #     """Concrete classes implement the actual search walk."""
    #     pass
    #
    #



