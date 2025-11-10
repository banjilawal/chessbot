# src/chess/neighbor/table.py

"""
Module: chess.graph.neighbor.record
Author: Banji Lawal
Created: 2025-111-03
version: 1.0.0
"""

from typing import List

from chess.coord import Coord
from chess.domain import Domain
from chess.piece import Piece


class NeighborTuple:
    _id: int
    _domain: Domain
    _neighbor: Piece
    _key_point: Coord
    
    def __init__(self, id: int, domain: Domain, neighbor: Piece, key_point: Coord):
        self._id = id
        self._neighbor = neighbor
        self.key_point = key_point
        
    @property
    def id(self) -> int:
        return self._id
    
    
    @property
    def domain(self) -> Domain:
        return self._domain
    
    
    @property
    def neighbor(self) -> Piece:
        return self._neighbor


    @property
    def key_point(self) -> Coord:
        return self._key_point
    
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, NeighborTuple):
            return (
                self._domain == other.domain and
                self._neighbor == other.neighbor and
                self._key_point == other.key_point
            )
        return False
    
    def __hash__(self):
        return hash(self._id)
        