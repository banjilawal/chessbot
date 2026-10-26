# src/domain/bluprint/model/state/token/blueprint.py

"""
Module: domain.bluprint.model.state.token.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Generic, Optional, Type, TypeVar, cast

from domain import (
    CombatantTokenBlueprint, Coord, Formation, HomeSquare,
    KingTokenBlueprint, PawnTokenBlueprint, StateModelBlueprint,
    Team, Token, TokenDeployment, Footstep
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
        footstep: Footstep
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
    _footstep: Footstep
    _formation: Formation
    _deployment: TokenDeployment
    _home_square: Optional[HomeSquare]

    
    def __init__(
            self,
            team: Team,
            footstep: Footstep,
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
            footstep: Footstep
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
        self._footstep = footstep
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
    def footstep(self) -> Footstep:
        return self._footstep
    
    @property
    def deployment_consistency_exists(self) -> bool:
        if self._footstep.is_not_consistent:
            return False
        if (
                self._footstep.position_does_not_exist and
                self._deployment == TokenDeployment.DEPLOYED_TO_HOME_SQUARE
        ):
            return False
        if (
                self._footstep.position_exists and
                self._deployment == TokenDeployment.NOT_DEPLOYED
        ):
            return False
        return True
    
    @property
    def has_deployment_inconsistency(self) -> bool:
        return not self.deployment_consistency_exists
    
    @property
    def domain_class(self) -> Type[T]:
        return cast(Type[T], super().domain_class)
    
    @property
    def domain_null_exception(self) -> TokenNullException:
        return cast(TokenNullException, super().domain_null_exception)
    
    


        
        