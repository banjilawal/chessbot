from abc import ABC, abstractmethod

from chess.board.board import Board
from chess.coord import Coord
from chess.geometry.quadrant import Quadrant
from chess.piece.piece import Piece


class Rank(ABC):
    _name:str
    _letter:str
    _value:int
    _per_side:int
    _quadrants:list[Quadrant]

    def __init__(self, name:str, letter:str, value:int, per_side:int, quadrants:list[Quadrant]):
        self._name = name
        self._letter = letter
        self._value = value
        self._per_side = per_side
        self._quadrants = quadrants


    @property
    def name(self) -> str:
        return self._name


    @property
    def letter(self) -> str:
        return self._letter


    @property
    def value(self) -> int:
        return self._value


    @property
    def quadrants(self) -> list[Quadrant]:
        return self._quadrants


    @property
    def per_side(self) -> int:
        return self._per_side


    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if not isinstance(other, Rank):
            return False
        return self._name.upper() == other.name.upper()


    def __hash__(self):
        return hash(self._name)


    @abstractmethod
    def walk(self, piece:Piece, destination:Coord, board:Board):
        """
        Validates a ChessPiece can reach a destination with its movement constraints. Must be instantiated by
        Walk implementors.

        Args:
            piece (ChessPiece):Source of truth for origin of motion
            destination (Coord):terminus of ChessPiece movement

        Returns:
            True if the move from origin to destination fits ChessRank movement rule.

        Raise:
            NullChessPieceException:If piece is null.
            NullCoordException:If destination is null.
            CoordException:If destination properties are invalid.
        """

        pass


    def __str__(self):
        return (
            f"{self._name} "
            f"{self._letter} "
            f"value:{self.value} "
            f"per_side:{self._per_side} "
            f"quadrants:{len(self._quadrants)}")

