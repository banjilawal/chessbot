# src/chess/owner/owner.py

"""
Module: chess.graph.owner
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from typing import Dict, List

from chess.square import Square
from chess.piece import Piece
from chess.square import Square
from chess.domain import Domain, DomainOrigin
from chess.pawn import ActorPlacementRequiredException

from chess.system import LoggingLevelRouter


class Domain:
    """
    # ROLE:
        Data-Holding, Data Transfer
        Set of; Square instances, Piece objects reachable by Domain owner from their origin
    # RESPONSIBILITIES:
        1. Lists all squares reachable by Domain owner.
        2. Provides data about which friends are .
        3. List Squares within Domain containing enemies the owner can attack or
            might avoid.
    # PROVIDES:
        Domain

    # ATTRIBUTES:
        id (int)
        origin (DomainOrigin): Contains Domain owner and their Square.
        squares: (List[Square]): Set of Square objects the owner can reach.
        enemy_squares: (Dict[Piece: Square]): Places containing enemies
        friendly_squares: (Dict[Piece: Square]): Domain places inside owner is blocked from occupying. 
    """
    _id: int
    _origin: DomainOrigin
    _squares: Dict[Piece: Square]
    _enemies: Dict[Piece: Square]
    _friends: Dict[Piece: Square]
    
    def __init__(
            self, id: int,
            origin: DomainOrigin,
            squares: Dict[Piece: Square],
            enemies: Dict[Piece: Square],
            friends: Dict[Piece: Square],
    ):
        self._id = id
        self._origin = origin
        self._squares = squares
        self._enemy_squares = enemies
        self._friendly_squares = friends
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def origin(self) -> DomainOrigin:
        return self._origin
    
    @property
    def squares(self) -> Dict[Piece: Square]:
        return self._squares
    
    @property
    def enemies(self) -> Dict[Piece, Square]:
        return self._enemies
    
    @property
    def friends(self) -> Dict[Piece, Square]:
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

