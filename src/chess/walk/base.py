from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from chess.exception.id import ChessException
from chess.geometry.coord import Coordinate



if TYPE_CHECKING:
    from chess.token.model import Piece


class Walk(ABC):

    """
    Interface for implementing ChessRank movement strategy.

    Attributes:
        No attributes
    """

    @staticmethod
    @abstractmethod
    def is_walkable(
        piece: 'Piece',
        destination: Coordinate,
        board: ChessException
    ) -> bool:
        method = "Walk.is_walkable"

        """
        Validates a ChessPiece can reach a destination with its movement constraints. Must be instantiated by
        Walk implementors.

        Args:
            piece (ChessPiece): Source of truth for origin of motion
            destination (Coordinate): terminus of ChessPiece movement

        Returns:
            True if the move from origin to destination fits ChessRank movement rule.

        Raise:
            NullChessPieceException: If piece is null.
            NullCoordinateException: If destination is null.
            CoordinateException: If destination properties are invalid.
        """
        pass


    def __str__(self):
        return f"{self.__class__.__name__}"