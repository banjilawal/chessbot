# src/domain/metadata/blueprint/model/searchable/state/token/king/blueprint.py

"""
Module: domain.metadata.blueprint.model.searchable.state.token.king.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast


from domain import (
    CheckWarning, CheckmateAttack, Coord, KingReadiness, KingToken, Formation, HomeSquare,
    Team, TokenBlueprint, TokenDeployment
)
from err import KingTokenNullException, TokenDeploymentException


class KingTokenBlueprint(TokenBlueprint):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a KingToken object.

     Attributes:
        team: Team,
        formation: Formation
        rank: Optional[Rank]
        positions: Optional[CoordDatabase]
        id: Optional[int]

        domain_class: Type[KingToken]
        domain_null_exception: KingTokenNullException

     Provides:

     Super Class:
        TokenBlueprint
     """
    _readiness: KingReadiness
    _checkmate: Optional[CheckmateAttack]
    _check_warning: Optional[CheckWarning]

    
    def __init__(
            self,
            team: Team,
            formation: Formation,
            position: Optional[Coord] | None = None,
            previous_position: Optional[Coord] | None = None,
            home_square: Optional[HomeSquare] | None = None,
            deployment: Optional[TokenDeployment] | None = None,
            readiness: Optional[KingReadiness] | None = None,
            checkmate: Optional[CheckmateAttack] | None = None,
            check_warning: Optional[CheckWarning] | None = None,
            domain_class: Optional[Type[KingToken]] | None = None,
            domain_null_exception: Optional[KingTokenNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            team: Team,
            formation: Formation
            position: Optional[Coord]
            previous_position: Optional[Coord]
            readiness: Optional[KingReadiness]
            deployment: Optional[TokenDeployment]
            checkmate: Optional[CheckmateAttack]
            check_warning: Optional[CheckWarning]
            domain_class: Optional[Type[KingToken]]
            domain_null_exception: Optional[KingTokenNullException]
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
            domain_class=domain_class or Type[KingToken],
            domain_null_exception=domain_null_exception or KingTokenNullException(),
        )
        self._checkmate = checkmate
        self._check_warning = check_warning
        self._readiness = readiness or KingReadiness.READY
        
    @property
    def readiness(self) -> KingReadiness:
        return self._readiness
        
    @property
    def checkmate(self) -> Optional[CheckmateAttack]:
        return self._checkmate
    
    @property
    def check_warning(self) -> Optional[CheckWarning]:
        return self._check_warning
    
    @property
    def domain_class(self) -> Type[KingToken]:
        return cast(Type[KingToken], super().domain_class)
    
    @property
    def domain_null_exception(self) -> KingTokenNullException:
        return cast(KingTokenNullException, super().domain_null_exception)
    


        
        