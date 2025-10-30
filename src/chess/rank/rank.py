from abc import ABC, abstractmethod
from typing import List

from chess.board.board import Board
from chess.coord import Coord
from chess.geometry.quadrant import Quadrant
from chess.piece.model.piece import Piece


class Rank(ABC):
    LOWER_BOUND = 1
    UPPER_BOUND = 8
    
    _id: int
    _name: str
    _letter: str
    _ransom: int
    _quota: int
    _quadrants: list[Quadrant]
    
    def __init__(self, id: int, name: str, letter: str, ransom: int, quota: int, quadrants: list[Quadrant]):
        self._id = id
        self._name = name
        self._letter = letter
        self._ransom = ransom
        self._quota = quota
        self._quadrants = quadrants
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def name(self) -> str:
        return self._name
    
    @property
    def letter(self) -> str:
        return self._letter
    
    @property
    def ransom(self) -> int:
        return self._ransom
    
    @property
    def quadrants(self) -> list[Quadrant]:
        return self._quadrants
    
    @property
    def quota(self) -> int:
        return self._quota
    
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
    

    @classmethod
    @abstractmethod
    def compute_span(cls, origin: Coord) -> [Coord]:
        """"""
        pass
    
    @abstractmethod
    def walk(self, piece: Piece, destination: Coord, board: Board):
        """
        Validates team ChessPiece can reach team destination with its movement constraints. Must be instantiated by
        Walk implementors.
    
        Args:
          piece (ChessPiece):Source of truth for origin of motion
          destination (Coord):terminus of ChessPiece movement
    
        Returns:
          True if the move from origin to destination fits ChessRank movement rule.
    
        Raise:
          NullChessPieceException:If discover is null.
          NullCoordException:If destination is null.
          CoordException:If destination properties are invalid.
        """
        
        pass
    
    def __str__(self):
        return (
            f"{self._name} "
            f"{self._letter} "
            f"value:{self.ransom} "
            f"per_side:{self._quota} "
            f"quadrants:{len(self._quadrants)}")
