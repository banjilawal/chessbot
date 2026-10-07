# src/domain/metadata/blueprint/model/state/token/combatant/blueprint.py

"""
Module: domain.metadata.blueprint.model.state.token.combatant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from domain import (
    CombatantReadiness, CombatantToken, Coord, Formation, HomeSquare, Team,
    Token, TokenBlueprint, TokenDeployment, Walk
)
from err import CombatantTokenNullException


class CombatantTokenBlueprint(TokenBlueprint[CombatantToken]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a CombatantToken object.

     Attributes:
        captor: Optional[Token]
        readiness: CombatantReadiness

        domain_class: Type[CombatantToken]
        domain_null_exception: CombatantNullException

     Provides:

     Super Class:
        TokenBlueprint
     """
    _captor: Optional[Token]
    _readiness: CombatantReadiness

    
    def __init__(
            self,
            team: Team,
            walk: Walk,
            formation: Formation,
            captor: Optional[Token] | None = None,
            home_square: Optional[HomeSquare] | None = None,
            deployment: Optional[TokenDeployment] | None = None,
            readiness: Optional[CombatantReadiness] | None = None,
            domain_class: Optional[Type[CombatantToken]] | None = None,
            domain_null_exception: Optional[CombatantTokenNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            team: Team
            walk: Walk
            formation: Formation
            captor: Optional[Token]
            home_square: Optional[HomeSquare]
            deployment: Optional[TokenDeployment]
            readiness: Optional[CombatantReadiness]
            domain_class: Optional[Type[CombatantToken]]
            domain_null_exception: Optional[CombatantNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            team=team,
            walk=walk,
            formation=formation,
            deployment=deployment,
            home_square=home_square,
            domain_class=domain_class or Type[CombatantToken],
            domain_null_exception=domain_null_exception or CombatantTokenNullException(),
        )
        self._captor = captor
        self._readiness = readiness or CombatantReadiness.READY
        
    @property
    def readiness(self) -> CombatantReadiness:
        return self._readiness
        
    @property
    def captor(self) -> Optional[Token]:
        return self._captor
    
    @property
    def is_captured(self) -> bool:
        return self._captor is not None and self._readiness == CombatantReadiness.CAPTURED
    
    @property
    def is_not_captured(self) -> bool:
        return not self.is_captured
    
    @property
    def domain_class(self) -> Type[CombatantToken]:
        return cast(Type[CombatantToken], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CombatantTokenNullException:
        return cast(CombatantTokenNullException, super().domain_null_exception)

    


        
        