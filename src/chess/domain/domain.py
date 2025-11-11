# src/chess/owner/owner.py

"""
Module: chess.graph.owner
Author: Banji Lawal
Created: 2025-10-28
version: 1.0.0
"""

from typing import List

from chess.coord import Coord
from chess.square import Square
from chess.domain import Domain, DomainOrigin
from chess.pawn import ActorPlacementRequiredException

from chess.system import LoggingLevelRouter


class Domain:
    """
    # ROLE:
        Data-Holding, Data Transfer
    # RESPONSIBILITIES:
        1. Lists all possible points the Domain owner can reach.
        2. List squares the Domain owner is blocked from by friends.
        3. List Squares within Domain containing enemies the owner can attack or
            might avoid.
    # PROVIDES:
        Domain

    # ATTRIBUTES:
        id (int)
        origin (DomainOrigin): Contains Domain owner and their Square.
        points: (List[Coord]): Set of Coord objects the owner can reach.. 
        enemy_squares: (List[Square]): Places containing enemies.
        friendly_squares: (List[Square]): Domain places inside owner is blocked from occupying. 
    """
    _id: int
    _origin: DomainOrigin
    _points: List[Coord]
    _enemy_squares: List[Square]
    _friendly_squares: List[Square]
    
    def __init__(
            self, id: int,
            origin: DomainOrigin,
            points: List[Coord],
            _enemy_squares: List[Square],
            friendly_squares: List[Square],
    ):
        self._id = id
        self._origin = origin
        self._points = points
        self._enemy_squares = _enemy_squares
        self._friendly_squares = friendly_squares
    
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def origin(self) -> DomainOrigin:
        return self._origin
    
    @property
    def points(self) -> List[Coord]:
        return self._points
    
    @property
    def enemy_squares(self) -> List[Square]:
        return self._enemy_squares
    
    @property
    def friendly_squares(self) -> List[Square]:
        return self._friendly_squares
    
    @LoggingLevelRouter.monitor
    def update(self, points: List[Coord], enemy_squares: List[Square], friendly_squares: List[Square]) -> Domain:
        """
        # ACTION:
            Factory for updating datasets when the Domain owner changes their position

        # PARAMETERS:
            * points: (List[Coord]): Updated points within range of the Domain owner.
            * enemy_squares: (List[Square]): Updated set of enemy-held squares the owner might
                attack or avoid.
            * friendly_squares: (List[Square]): Updated set of friendly squares the owner is
                blocked from occupying.
            
        # RETURNS:
            Domain: Recycling Domain.id and Domain.origin makes searches easier.

        # RAISES:
            None
        """
        
        method = "Domain.update"
        return Domain(
            id=self._id,
            origin=self._origin,
            points=points,
            enemy_squares=enemy_squares,
            friendly_squares=friendly_squares,
        )
    
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

