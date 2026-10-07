# src/domain/model/searchable/state/token/.py.py

"""
Module: domain.model.searchable.state.token.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import abstractmethod
from typing import Optional

from domain import (
    Coord, Formation, HomeSquare, Rank, StateModel, Team, TokenDeployment, Walk
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
        home_square: OpeningSquare
        position: Optional[Coord]
        previous_position: Optional[Coord]
        
        is_ready: bool
        is_not_ready: bool
        
    Provides:
        -   def mark_as_deployed() -> Void
        -   def is_friend(token: Token) -> bool
        -   def is_enemy(token: Token) -> bool

    Super Class:
        StateModel
    """
    _id: int
    _team: Team
    _formation: Formation
    _home_square: HomeSquare
    _deployment: TokenDeployment
    _walk: Walk

    def __init__(
            self,
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
            walk: Optional[Walk] | None = None,
    ):
        """
        Args:
            id: int
            team: Team
            formation: Formation
            home_square: OpeningSquare
            walk: Optional[Walk]
        """
        super().__init__(id=id)
        self._team = team
        self._formation = formation
        self._home_square = home_square
        self._deployment = TokenDeployment.NOT_DEPLOYED
        self._walk = walk or Walk()
    
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
    
    def mark_as_deployed(self):
        self._deployment = TokenDeployment.DEPLOYED_TO_HOME_SQUARE
        
    @property
    def walk(self) -> Walk:
        return self._walk
    
    @property
    def position(self) -> Optional[Coord]:
        return self._walk.position
    
    @position.setter
    def position(self, other: Coord):
        position = self._walk.position
        previous_position = self._walk.position
        
        self._walk = Walk(
            position=position,
            previous_position=previous_position,
        )
        
    @property
    def has_been_deployed(self) -> bool:
       return (
               self._walk.position is not None and
               self._deployment == TokenDeployment.DEPLOYED_TO_HOME_SQUARE
       )
    
    @property
    def has_never_been_deployed(self) -> bool:
       return not self.has_been_deployed
    
    def is_friend(self, token: Token) -> bool:
        return self._team == token.team
    
    def is_enemy(self, token: Token) -> bool:
        return not self.is_friend(token)
    
    @property
    @abstractmethod
    def is_ready(self) -> bool:
        pass
    
    @property
    @abstractmethod
    def is_not_ready(self) -> bool:
        pass
    
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
