# src/domain/metadata/blueprint/model/searchable/state/token/combatant/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.token.combatant.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast

from collection import CoordDatabase
from domain import (
    CombatantReadiness, CombatantToken, Coord, Formation, HomeSquare, Rank, Team, Token, TokenBlueprint,
    TokenDeployment
)
from err import CombatantNullException


class CombatantBlueprint(TokenBlueprint):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a CombatantToken object.

     Attributes:
        team: Team,
        formation: Formation
        rank: Optional[Rank]
        captor: Optional[Token]
        positions: Optional[CoordDatabase]
        id: Optional[int]

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
            formation: Formation,
            position: Optional[Coord] | None = None,
            previous_position: Optional[Coord] | None = None,
            deployment: Optional[TokenDeployment] | None = None,
            readiness: Optional[CombatantReadiness] | None = None,
            captor: Optional[Token] | None = None,
            home_square: Optional[HomeSquare] | None = None,
            domain_class: Optional[Type[CombatantToken]] | None = None,
            domain_null_exception: Optional[CombatantNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            team: Team,
            formation: Formation
            position: Optional[Coord]
            previous_position: Optional[Coord]
            deployment: Optional[TokenDeployment]
            readiness: Optional[CombatantReadiness]
            captor: Optional[Token]
            positions: Optional[CoordDatabase]
            domain_class: Optional[Type[CombatantToken]]
            domain_null_exception: Optional[CombatantNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            team=team,
            position=position,
            formation=formation,
            home_square=home_square,
            deployment=deployment,
            previous_position=previous_position,
            domain_class=domain_class or Type[CombatantToken],
            domain_null_exception=domain_null_exception or CombatantNullException(),
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
    def domain_class(self) -> Type[CombatantToken]:
        return cast(Type[CombatantToken], super().domain_class)
    
    @property
    def domain_null_exception(self) -> CombatantNullException:
        return cast(CombatantNullException, super().domain_null_exception)
    
    @property
    def is_captured(self) -> bool:
        return self._captor is not None
    
    @property
    def is_not_captured(self) -> bool:
        return not self.is_captured
    


        
        