# src/domain/metadata/blueprint/model/searchable/state/token/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import Formation, HomeSquare, Rank, StateModelBlueprint, Team, Token, TokenContext
from err import TokenNullException


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
        id: Optional[int]

        domain_class: Type[Token]
        search_context_class: Type[TokenContext]
        domain_null_exception: TokenNullException

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _team: Team
    _rank: Optional[Rank]
    _formation: Formation
    _home_square: Optional[HomeSquare]
    
    def __init__(
            self,
            team: Team,
            formation: Formation,
            domain_class: Optional[Type[Token]] | None = None,
            search_context_class: Optional[Type[TokenContext]] | None = None,
            domain_null_exception: Optional[TokenNullException] | None = None,
            id: Optional[int] | None = None,
            rank: Optional[Rank] | None = None,
            home_square: Optional[HomeSquare] | None = None,
    ):
        """
        Args:
            domain_class: Optional[Type[Token]]
            search_context_class: Optional[Type[TokenContext]]
            domain_null_exception: Optional[TokenNullException]
            id: Optional[int]
            team: Team,
            formation: Formation
            rank: Optional[Rank]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Token],
            search_context_class=search_context_class or Type[TokenContext],
            domain_null_exception=domain_null_exception or TokenNullException(),
        )
        self._team = team
        self._rank = rank
        self._formation = formation
        self._home_square = home_square
    
    @property
    def domain_class(self) -> Type[Token]:
        return cast(Type[Token], super().domain_class)
    
    @property
    def search_context_class(self) -> Type[TokenContext]:
        return cast(Type[TokenContext], super().search_context_class)
    
    @property
    def domain_null_exception(self) -> TokenNullException:
        return cast(TokenNullException, super().domain_null_exception)
    
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
    

        
        