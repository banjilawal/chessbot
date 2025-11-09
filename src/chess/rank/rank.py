# src/chess/rank/rank.py

"""
Module: chess.rank.rank
Author: Banji Lawal
Created: 2025-07-25
version: 1.0.0
"""

from abc import ABC, abstractmethod

from chess.coord import Coord
from chess.piece import Piece
from chess.geometry import Quadrant


class Rank(ABC):
    """"""
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
    
    @classmethod
    @abstractmethod
    def compute_span(cls, piece: Piece) -> [Coord]:
        """"""
        pass
    
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
        if isinstance(other, Rank):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)

    def __str__(self):
        return (
            "bounds: {"
            f"id:{self._id}, "
            f"name:{self._name}, "
            f"letter:{self._letter}, "
            f"ransom:{self._ransom}, "
            f"per_side:{self._quota}"
            "}"
        )
