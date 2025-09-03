from abc import ABC, abstractmethod
from typing import List

from chess.board.board import Board
from chess.geometry.coord import Coordinate
from chess.geometry.quadrant import Quadrant
from chess.token.model import Piece


class Rank(ABC):
    _name: str
    _letter: str
    _value: int
    _per_team: int
    _territories: List[Quadrant]

    def __init__(self, name: str, letter: str, value: int, per_team: int, territories: List[Quadrant]):
        self._name = name
        self._letter = letter
        self._value = value
        self._per_team = per_team
        self._territories = territories


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
    def territories(self) -> List[Quadrant]:
        return self._territories.copy()


    @property
    def per_team(self) -> int:
        return self._per_team


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
    def walk(self, piece: Piece, coordinate: Coordinate, board: Board):
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
        return (f"{self._name}, value:{self._letter}, {self.value} "
                f"num_per_player:{self._per_team} num_territories:{len(self._territories)}")

