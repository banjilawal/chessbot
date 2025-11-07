# src/chess/visitation/table.py

"""
Module: chess.graph.visitation.record
Author: Banji Lawal
Created: 2025-111-03
version: 1.0.0
"""

from typing import List

from chess.coord import Coord
from chess.domain import Domain
from chess.piece import Piece


class VisitRecord:
    _id: int
    _domain: Domain
    _visitor: Piece
    _owner_address: Coord
    _shared_site: Coord
    
    def __init__(self, id: int, domain: Domain, visitor: Piece):
        self._id = id
        self._visitor = visitor
        self._domain_owner = domain.owner
        self._owner_address = domain.owner_address
        self._shared_site = visitor.current_position
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def domain(self) -> Domain:
        return self._domain
    
    @property
    def visitor(self) -> Piece:
        return self._visitor
    
    @property
    def owner_address(self) -> Coord:
        return self._owner_address
    
    @property
    def shared_site(self) -> Coord:
        return self._shared_site
    
    def __eq__(self, other):
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, VisitRecord):
            return self._id == other.id
        return False
    
    def __hash__(self):
        return hash(self._id)
        