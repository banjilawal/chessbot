# src/domain/metadata/blueprint/model/state/token/blueprint.py

"""
Module: domain.metadata.blueprint.model.state.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Generic, Optional, Type, TypeVar, cast

from domain import (
    CombatantTokenBlueprint, Coord, Formation, HomeSquare,
    KingTokenBlueprint, PawnTokenBlueprint, StateModelBlueprint,
    Team, Token, TokenDeployment, Walk
)
from err import  TokenNullException

T = TypeVar("T", bound="Token")

class TokenBlueprint(StateModelBlueprint[T], Generic[T]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a Token object.

     Attributes:
        team: Team
        walk: Walk
        formation: Formation
        home_square: Optional[HomeSquare]
        deployment: Optional[TokenDeployment]
        id: Optional[int]

        domain_class: Type[Token]
        domain_null_exception: TokenNullException

     Provides:

     Super Class:
        StateModelBlueprint
     """
    _team: Team
    _walk: Walk
    _formation: Formation
    _deployment: TokenDeployment
    _home_square: Optional[HomeSquare]

    
    def __init__(
            self,
            team: Team,
            walk: Walk,
            formation: Formation,
            home_square: Optional[HomeSquare] | None = None,
            deployment: Optional[TokenDeployment] | None = None,
            id: Optional[int] | None = None,
            domain_class: Optional[Type[Token]] | None = None,
            domain_null_exception: Optional[TokenNullException] | None = None,
    ):
        """
        Args:
            team: Team
            walk: Walk
            formation: Formation
            home_square: Optional[HomeSquare]
            deployment: Optional[TokenDeployment]
            id: Optional[int]
            domain_class: Optional[Type[Token]]
            domain_null_exception: Optional[TokenNullException]
        """
        super().__init__(
            id=id,
            domain_class=domain_class or Type[Token],
            domain_null_exception=domain_null_exception or TokenNullException(),
        )
        self._team = team
        self._walk = walk
        self._formation = formation
        self._home_square = home_square
        self._deployment = deployment or TokenDeployment.NOT_DEPLOYED
    
    @property
    def team(self) -> Team:
        return self._team
    
    @property
    def formation(self) -> Formation:
        return self._formation
    
    @property
    def deployment(self) -> TokenDeployment:
        return self._deployment
    
    @property
    def home_square(self) -> Optional[HomeSquare]:
        return self._home_square
    
    @property
    def walk(self) -> Walk:
        return self._walk
    
    @property
    def is_pawn_token_blueprint(self) -> bool:
        return isinstance(self, PawnTokenBlueprint)
    
    @property
    def is_combatant_token_blueprint(self) -> bool:
        return isinstance(self, CombatantTokenBlueprint)
    
    @property
    def is_king_token_blueprint(self) -> bool:
        return isinstance(self, KingTokenBlueprint)
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> TokenNullException:
        return cast(TokenNullException, super().domain_null_exception)
    
    


        
        