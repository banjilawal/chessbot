# src/chess/domain/domain.py

"""
Module: chess.domain.domain
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from typing import Dict, List

from chess.piece import Piece
from chess.square import Square
from chess.domain import Domain, DomainOrigin


class Domain:
    """
    # ROLE: Data-Holding

    # RESPONSIBILITIES:
    Immutable data structure that:
        1. Lists all squares reachable by Domain owner in a walk from its current position.
        2. Indicate which Squares are blocked by a friendly Piece.
        3. Indicate which Squares contain an enemy Piece which might be attacked or avoided.
        
    # PROVIDES:
        Domain

    # ATTRIBUTES:
        * id (int)
        * origin (DomainOrigin): Contains Domain owner and their Square.
        * squares: (List[Square]): Set of Square objects the owner can reach.
        * enemies: (Dict[Piece: Square]): Map of enemies to their Squares.
        * friends: (Dict[Piece: Square]): Map of friendly to their Squares.
    """
    _id: int
    _origin: DomainOrigin
    _squares: [Square]
    _enemies: {Piece: Square}
    _friends: {Piece: Square}
    
    def __init__(
            self, id: int,
            origin: DomainOrigin,
    ):
        """
        # Action:
        Construct a Domain object.

        # Parameters:
            * id (int)
            * origin (DomainOrigin)
        # Returns:
        None
        
        # Raises:
        None
        """
        method = "Domain.__init__"
        
        self._id = id
        self._origin = origin
        self._squares = [Square]
        self._enemies = {Piece: Square}
        self._friends = {Piece: Square}
        
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def origin(self) -> DomainOrigin:
        return self._origin
    
    @property
    def squares(self) -> [Square]:
        return self._squares
    
    @property
    def enemies(self) -> {Piece, Square}:
        return self._enemies
    
    @property
    def friends(self) -> {Piece, Square}:
        return self._friends
    
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
