# src/domain/metadata/blueprint/model/searchable/state/token/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain.metadata.blueprint import StateModelBlueprint
from domain.model import HomeSquare, Rank, Team, Token
from domain.schema import Formation


class TokenBlueprint(StateModelBlueprint[Token]):
    """
     Role:
        1.  Metadata
        
    Responsibilities:
        1.  Provides values for hydrating a Token object.

        
    Attributes:
        team: Team,
        formation: Formation
        rank: Optional[Rank]
        home_square: Optional[HomeSquare]
        domain_class: Type[Token]
        
    Provides:

     Super Class:
        StateModelBlueprint
     """
    
    def __init__(
            self,
            team: Team,
            formation: Formation,
            id: Optional[int] | None = None,
            rank: Optional[Rank] | None = None,
            home_square: Optional[HomeSquare] | None = None,
            domain_class: Type[Token] = Token,
    ):
        """
        Args:
            team: Team,
            formation: Formation
            id: Optional[int]
            rank: Optional[Rank]
            home_square: Optional[HomeSquare]
            domain_class: Type[Token] = Type[Token]
        """
        super().__init__(domain_class=domain_class, id=id)
        self._team = team
        self._rank = rank
        self._formation = formation
        self._home_square = home_square
        
    @property
    def domain_class(self) -> Type[Token]:
        return cast(Type[Token], super().domain_class)
    
    @property
    def team(self) -> Team:
        return self._team
    
    @property
    def formation(self) -> Formation:
        return self._formation
    
    @property
    def rank(self) -> Optional[Rank]:
        return self._rank
    
    @property
    def home_square(self) -> Optional[HomeSquare]:
        return self._home_square
    
    

        
        