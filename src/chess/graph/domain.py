# src/chess/graph/domain.py

"""
Module: chess.graph.domain
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from typing import Optional

from chess.coord import Coord
from chess.piece import Piece


class Domain:
    """"""
    _id: int
    _capital: Piece
    _tree: [Coord]
    _capital_origin: Coord
    _previous_origin: Optional[Coord]
    
    def __init__(self, id: int, piece: Piece):
        self._id = id
        self._capital = piece
        self._previous_origin = None
        self._origin = piece.current_position
        self._tree = self._capital.rank.compute_span(self._capital)
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def capital(self) -> Piece:
        return self._capital
    
    @property
    def origin(self) -> Coord:
        return self._capital_origin
    
    @property
    def previous_origin(self) -> Optional[Coord]:
        return self._previous_origin
    
    @property
    def tree(self) -> [Coord]:
        return self._tree
    
    def __eq__(self, other) -> bool:
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Domain):
            return self._id == other._id
        return False
    
    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:
        return f"{self._capital} at {self._tree}"
