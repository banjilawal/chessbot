# src/chess/domain/domain.py

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
    _owner: Piece
    _tree: [Coord]
    _owner_address: Optional[Coord]
    _owner_previous_address: Coord

    
    def __init__(self, id: int, piece: Piece):
        self._id = id
        self._owner = piece
        self._owner_previous_address = None
        self._owner_address = piece.current_position
        self._tree = self._owner.rank.compute_span(self._owner)
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def owner(self) -> Piece:
        return self._owner
    
    @property
    def owner_address(self) -> Coord:
        return self._owner_previous_address
    
    @property
    def owner_previous_address(self) -> Optional[Coord]:
        return self._owner_previous_address
    
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
        return f"{self._owner} at {self._tree}"
