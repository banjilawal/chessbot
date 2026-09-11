# src/domain/model/searchable/state/token/.py.py

"""
Module: domain.model.searchable.state.token.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional

from collection import CoordDatabase
from domain import (
    Coord, Formation, HomeSquare, Rank, StateModel, Team, TokenDeployment, TokenReadiness
)


class Token(StateModel):
    """
    Role:
        - Stateful Data Holder
        
    Responsibilities:
        1. Abstract representation of a chess piece.
        
    Attributes:
        id: int
        team: Team
        formation: Formation
        readiness: TokenReadiness
        deployment: TokenDeployment
        positions: CoordDatabase
        home_square: OpeningSquare
        position: Optional[Coord]
        previous_position: Optional[Coord]

        is_not_deployed: bool
        is_active(self): bool
        is_disabled: bool
        is_enemy: bool
        
    Provides:

    Super Class:
        StateModel
    """
    _id: int
    _team: Team
    _formation: Formation
    _home_square: HomeSquare
    _deployment: TokenDeployment
    _readiness: TokenReadiness
    _positions: CoordDatabase
    _position: Optional[Coord]
    _previous_position: Optional[Coord]

    def __init__(
            self,
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
            positions: Optional[CoordDatabase] | None = None,
    ):
        """
        Args:
            id: int
            team: Team
            formation: Formation
            home_square: OpeningSquare
        """
        super().__init__(id=id)
        self._team = team
        self._formation = formation
        self._home_square = home_square
        self._deployment = TokenDeployment.NOT_DEPLOYED
        self._readiness = TokenReadiness.NOT_INITIALIZED
        
        self._position = None
        self._previous_position = None
        self._positions = positions or CoordDatabase()
    
    @property
    def formation(self) -> Formation:
        return self._formation
    
    @property
    def name(self) -> str:
        return self._formation.designation
    
    @property
    def roster_number(self) -> int:
        return self._formation.roster_number
    
    @property
    def team(self) -> Team:
        return self._team
    
    @property
    def rank(self) -> Rank:
        return self._formation.rank
    
    @property
    def home_square(self) -> HomeSquare:
        return self._home_square
    
    @property
    def readiness(self) -> TokenReadiness:
        return self._readiness
    
    @readiness.setter
    def readiness(self, other: TokenReadiness):
        self._readiness = other
    
    @property
    def deployment(self) -> TokenDeployment:
        return self._deployment
    
    @deployment.setter
    def deployment(
            self,
            other: TokenDeployment = TokenDeployment.DEPLOYED_TO_HOME_SQUARE
    ):
        self._deployment = other
    
    @property
    def positions(self) -> CoordDatabase:
        return self._positions
    
    @property
    def position(self) -> Optional[Coord]:
        return self._position
    
    @position.setter
    def position(self, other: Coord):
        self._position = other
    
    @property
    def previous_position(self) -> Optional[Coord]:
        return self._previous_position
    
    @previous_position.setter
    def previous_position(self, other: Coord):
        self._previous_position = other
     
    @property
    def is_not_deployed(self) -> bool:
        return (
                self._position is None and 
                self._deployment == TokenDeployment.NOT_DEPLOYED
        )
    
    @property
    def is_deployed(self) -> bool:
        return (
                self._position == self._home_square.coord and 
                self._deployment == TokenDeployment.DEPLOYED_TO_HOME_SQUARE
        )
    
    @property
    def is_ready(self) -> bool:
       return self.is_deployed and self._readiness == TokenReadiness.READY
    
    @property
    def is_not_ready(self) -> bool:
       return not self.is_ready
    
    def is_friend(self, token: Token) -> bool:
        return self._team == token.team
    
    def is_enemy(self, token: Token) -> bool:
        return not self.is_friend(token)
    
    def has_checked_enemy_king(self) -> bool:
        return (
                self._checked_enemy_king is not None and
                self.is_enemy(self._checked_enemy_king)
        )
    
    def is_no_enemy_checked(self) -> bool:
        return not self.has_checked_enemy_king
    
    def __eq__(self, other: object) -> bool:
        if other is self: return True
        if other in None: return False
        if isinstance(other, Token):
            return self._id == other.id
        return False

    def __hash__(self) -> int:
        return hash(self._id)
    
    def __str__(self) -> str:
        return (
            f"Token[id:{self._id} "
            f"name:{self.name} "
        )
