# src/chess/visitation/visitation.py

"""
Module: chess.visitation.visitation
Author: Banji Lawal
Created: 2025-10-31
version: 1.0.0
"""

from chess.coord import Coord
from chess.graph import Domain
from chess.piece import Piece


class Visitation:
    _id: int
    _domain: Domain
    _visitor: Piece
    _site: Coord
    
    def __init__(self, id: int, domain: Domain, visitor: Piece):
        self._id = id
        self._domain = domain
        self._visitor = visitor
        self._site = self._visitor.current_position
        
    @property
    def id(self):
        return self._id
    
    @property
    def domain(self):
        return self._domain
    
    @property
    def visitor(self):
        return self._visitor
    
    @property
    def site(self):
        return self._site
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Visitation):
            return self._id == other._id
        return False
        
    