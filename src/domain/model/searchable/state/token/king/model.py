# src/domain/model/searchable/state/token/king/model.py

"""
Module: domain.model.searchable.state.token.king.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Optional

from domain import (
    AlertTable, ThreatLevel, Footstep, Formation, HomeSquare, Square, Team,
    Token, KingReadiness
)


class KingToken(Token):
    """
    Role:
        - Stateful Data-Holder

    Responsibilities:
        1. Token that can be checkmated not captured.

    Attributes:
        alert: AlertTable
        readiness: KingReadiness
        threat_level: EncounterAlertLevel
        potential_destination: Optional[Square]

    Super Class:
        Token
    """
    _alert: AlertTable
    _readiness: KingReadiness
    _threat_level: ThreatLevel
    _potential_destination: Optional[Square]

    def __init__(
            self,
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
            footstep: Optional[Footstep] | None = None,
            alert: Optional[AlertTable] | None = None,
    ):
        """
        Args:
            id: int
            team: Team
            home_square: Square
            formation: Formation
            footstep: Optional[Footstep]
            alert: Optional[AlertTable]
        """
        super().__init__(
            id=id,
            team=team,
            formation=formation,
            home_square=home_square,
            footstep=footstep,
        )
        self._alert = alert or AlertTable()
        self._readiness = KingReadiness.NOT_READY
        self._threat_level = ThreatLevel.LOW
        self._potential_destination = None
        
    @property
    def readiness(self) -> KingReadiness:
        return self._readiness
    
    @readiness.setter
    def readiness(self, other: KingReadiness):
        self._readiness = other
        
        
    @property
    def threat_level(self) -> ThreatLevel:
        return self._threat_level
    
    @threat_level.setter
    def threat_level(self, other: ThreatLevel):
        self._threat_level = other
        
    @property
    def potential_destination(self) -> Optional[Square]:
        return self._potential_destination
    
    @potential_destination.setter
    def potential_destination(self, other: Square):
        self._potential_destination = other
        
    @property
    def alert(self) -> AlertTable:
        return self._alert
        
    @property
    def is_ready(self) -> bool:
        return (
                self.has_been_deployed and
                self._alert.not_checkmated and
                self._readiness == KingReadiness.READY
        )
    
    @property
    def is_not_ready(self) -> bool:
        return (
                self.has_never_been_deployed or
                self.alert.not_checkmated
        )
     
    @property
    def is_safe(self) -> bool:
        return (
                self.is_ready and
                self._alert.no_enemy_detected and
                self._threat_level == ThreatLevel.LOW
        )
    
    @property
    def is_not_safe(self) -> bool:
        return (
                self.is_ready and
                self._alert.enemy_detected and
                self._threat_level == ThreatLevel.HIGH
        )
    
    @property
    def is_checkmated(self) -> bool:
        return (
                self.has_been_deployed and
                self._alert.have_been_checkmated and
                self._readiness == KingReadiness.CHECKMATED
        )
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, KingToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
