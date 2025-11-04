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
    _domain_owner: Piece
    _owner_address: Coord
    _visitor: Piece
    _shared_site: Coord
    
    def __init__(self, id: int, domain: Domain, visitor: Piece):
        self._id = id
        self._domain_owner = domain.owner
        self._owner_address = domain.owner_address
        self._visitor = visitor
        self._shared_site = visitor.current_position
        