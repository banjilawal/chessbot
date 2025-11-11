# src/chess/domain/origin.py

"""
Module: chess.domain.origin
Author: Banji Lawal
Created: 2025-11-11
version: 1.0.0
"""

from chess.piece import Piece
from chess.square import Square


class DomainOrigin:
    """
    # ROLE:
        Data-Holding
    # RESPONSIBILITIES:
        1. Encapsulates information about a Domain owner and their current Square.
    # PROVIDES:
        Domain

    # ATTRIBUTES:
        owner (Piece): Owner of a Domain.
        owner_square (Square):
    """
    _owner: Piece
    _owner_square: Square
    
    def __init__(self, owner: Piece, owner_square: Square):
        
        self._owner = owner
        self._owner_square = owner_square
        
        
    @property
    def owner(self) -> Piece:
        return self._owner
    
    
    @property
    def square(self) -> Square:
        return self._owner_square
    
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other is None: return False
        if isinstance(other, DomainOrigin):
            return self._owner == other._owner
        return False
    
    
    def __hash__(self) -> int:
        return hash(self._owner.id)