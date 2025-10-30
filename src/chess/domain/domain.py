# src/chess/domain/domain.py
"""
Module: chess.domain.domain
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""


from typing import List, Optional

from chess.coord import Coord
from chess.piece import Piece

class Domain:
    """"""
    _piece: Piece
    _previous_origin: Optional[Coord]
    _points: List[Coord]
    
    def __init__(self, piece: Piece):
        self._points = []
        self._piece = piece
        self._previous_origin = None
        
        
    @property
    def piece(self) -> Piece:
        return self._piece
    
    @property
    def previous_origin(self) -> Optional[Coord]:
        return self._previous_origin
    
    @property
    def points(self) -> List[Coord]:
        return self._points
    
    def __eq__(self, other) -> bool:
        if other is self:
            return True
        if other is None:
            return False
        if isinstance(other, Domain):
            return self._piece == other._piece
        return False
    
    
    
    
    def __str__(self) -> str:
        return f"{self._piece} at {self._points}"


