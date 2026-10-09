# src/domain/metadata/blueprint/model/state/token/king/blueprint.py

"""
Module: domain.metadata.blueprint.model.state.token.king.blueprint
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional, Type, cast


from domain import (
    Alert, Footstep, KingReadiness, KingToken, Formation, HomeSquare,
    Team, ThreatLevel, TokenBlueprint, TokenDeployment
)
from err import KingTokenNullException


class KingTokenBlueprint(TokenBlueprint[KingToken]):
    """
     Role:
        1.  Metadata

     Responsibilities:
         1.  Provides values for hydrating a KingToken object.

     Attributes:
        alert: Alert
        readiness: KingReadiness
        threat_level: ThreatLevel

        domain_class: Type[KingToken]
        domain_null_exception: KingTokenNullException

     Provides:

     Super Class:
        TokenBlueprint
     """
    _alert: Alert
    _readiness: KingReadiness
    _threat_level: ThreatLevel

    def __init__(
            self,
            team: Team,
            footstep: Footstep,
            formation: Formation,
            home_square: Optional[HomeSquare] | None = None,
            deployment: Optional[TokenDeployment] | None = None,
            readiness: Optional[KingReadiness] | None = None,
            threat_level: Optional[ThreatLevel] | None = None,
            alert: Optional[Alert] | None = None,
            domain_class: Optional[Type[KingToken]] | None = None,
            domain_null_exception: Optional[KingTokenNullException] | None = None,
            id: Optional[int] | None = None,
    ):
        """
        Args:
            team: Team
            footstep: Footstep
            formation: Formation
            home_square: Optional[HomeSquare]
            deployment: Optional[TokenDeployment]
            readiness: Optional[KingReadiness]
            threat_level: Optional[ThreatLevel]
            alert: Optional[Alert]
            domain_class: Optional[Type[KingToken]]
            domain_null_exception: Optional[KingTokenNullException]
            id: Optional[int]
        """
        super().__init__(
            id=id,
            team=team,
            footstep=footstep,
            formation=formation,
            home_square=home_square,
            deployment=deployment,
            domain_class=domain_class or Type[KingToken],
            domain_null_exception=domain_null_exception or KingTokenNullException(),
        )
        self._alert = alert or Alert()
        self._threat_level = threat_level or ThreatLevel.LOW
        self._readiness = readiness or KingReadiness.NOT_READY
        
    @property
    def readiness(self) -> KingReadiness:
        return self._readiness
        
    @property
    def alert(self) -> Alert:
        return self._alert
    
    @property
    def threat_level(self) -> ThreatLevel:
        return self._threat_level
    
    @property
    def domain_class(self) -> Type[KingToken]:
        return cast(Type[KingToken], super().domain_class)
    
    @property
    def domain_null_exception(self) -> KingTokenNullException:
        return cast(KingTokenNullException, super().domain_null_exception)
    


        
        