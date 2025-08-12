from abc import ABC, abstractmethod
from typing import Optional

from chess.board.board import ChessBoard
from chess.exception.exception import ChessException
from chess.geometry.coordinate.coordinate import Coordinate
from chess.token.chess_piece import ChessPiece

class DestinationUnreachableException(ChessException):
    default_message = "The destination coordinate is not reachable"


class Walk(ABC):

    """
    Interface for implementing ChessRank movement strategy.

    Attributes:
        No attributes
    """

    @staticmethod
    @abstractmethod
    def is_walkable(
        chess_piece: ChessPiece,
        destination: Coordinate,
        chess_board: Optional[ChessBoard] = None
    ) -> bool:
        method = "Walk.is_walkable"

        """
        Validates a ChessPiece can reach a destination with its movement constraints. Must be instantiated by
        Walk implementors.

        Args:
            chess_piece (ChessPiece): Source of truth for origin of motion
            destination (Coordinate): terminus of ChessPiece movement

        Returns:
            True if the move from origin to destination fits ChessRank movement rule.

        Raise:
            NullChessPieceException: If chess_piece is null.
            NullCoordinateException: If destination is null.
            CoordinateException: If destination properties are invalid.
        """
        pass


    def __str__(self):
        return f"{self.__class__.__name__}"