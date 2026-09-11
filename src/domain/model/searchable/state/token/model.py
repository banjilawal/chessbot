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
    Coord, Formation, HomeSquare, Rank, StateModel, Team, TokenDeployment
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
        deployment: TokenDeployment
        positions: CoordDatabase
        home_square: OpeningSquare
        position: Optional[Coord]
        previous_position: Optional[Coord]
        
        is_ready: bool
        is_not_ready: bool
        
        is_deployed: bool
        is_not_deployed: bool
        
        is_friend: bool
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
    def is_ready(self) -> bool:
       return self._deployment == TokenDeployment.DEPLOYED_TO_HOME_SQUARE
    
    @property
    def is_not_ready(self) -> bool:
       return not self.is_ready
    
    def is_friend(self, token: Token) -> bool:
        return self._team == token.team
    
    def is_enemy(self, token: Token) -> bool:
        return not self.is_friend(token)
    
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
