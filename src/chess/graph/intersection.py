# src/chess/graph/intersection.py

"""
Module: chess.graph.intersection
Author: Banji Lawal
Created: 2025-10-31
version: 1.0.0
"""

from chess.coord import Coord
from chess.graph import Domain
from chess.piece import Piece


class Intersection:
    _id: int
    _domain: Domain
    _capital: Piece
    _shared_point: Coord
    
    def __init__(self, id: int, domain: Domain, capital: Piece, shared_point: Coord):
        self._id = id
        self._domain = domain
        self._capital = capital
        self._shared_point = shared_point
        
    @property
    def id(self):
        return self._id
    
    @property
    def domain(self):
        return self._domain
    
    @property
    def capital(self):
        return self._capital
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Intersection):
            return self._id == other._id
        return False
        
    