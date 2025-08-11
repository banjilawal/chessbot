from abc import ABC, abstractmethod

from chess.geometry.coordinate.coordinate import Coordinate
from chess.token.chess_piece import ChessPiece


class Walk(ABC):

    @staticmethod
    @abstractmethod
    def is_walkable(chess_piece: ChessPiece, destination: Coordinate) -> bool:
        """Returns True if the move from origin to destination fits this pattern."""
        pass

    def __str__(self):
        return f"{self.__class__.__name__}"