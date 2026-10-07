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
    EncounterAlertLevel, Formation, HomeSquare, Team,
    Token, KingReadiness
)


class KingToken(Token):
    """
    Role:
        - Stateful Data-Holder

    Responsibilities:
        1. Token that can be checkmated not captured.

    Attributes:
        threats: ThreatTable
        readiness: KingReadiness
        alertness: EncounterAlertLevel

    Super Class:
        Token
    """
    _threats: ThreatTable
    _readiness: KingReadiness
    _alertness: EncounterAlertLevel

    def __init__(
            self,
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
            footstep: Optional[Footstep] | None = None,
            threats: Optional[ThreatTable] | None = None,
    ):
        """
        Args:
            id: int
            team: Team
            home_square: Square
            formation: Formation
            footstep: Optional[Footstep]
            threats: Optional[ThreatTable]
        """
        super().__init__(
            id=id,
            team=team,
            formation=formation,
            home_square=home_square,
            footstep=footstep,
        )
        self._threats = threats or ThreatTable()
        self._readiness = KingReadiness.NOT_READY
        self._alertness = EncounterAlertLevel.LOW
        
    @property
    def readiness(self) -> KingReadiness:
        return self._readiness
    
    @readiness.setter
    def readiness(self, other: KingReadiness):
        self._readiness = other
        
        
    @property
    def alertness(self) -> EncounterAlertLevel:
        return self._alertness
    
    @alertness.setter
    def alertness(self, other: EncounterAlertLevel):
        self._alertness = other
        
    @property
    def threats(self) -> ThreatTable:
        return self._threats
        
    @property
    def is_ready(self) -> bool:
        return (
                self.has_been_deployed and
                self._threats.has_not_been_checkmated and
                self._readiness == KingReadiness.READY
        )
    
    @property
    def is_not_ready(self) -> bool:
        return (
                self.has_never_been_deployed or
                self.is_checkmated
        )
     
    @property
    def is_safe(self) -> bool:
        return (
                self.is_ready and
                self._threats.no_enemy_detected and
                self._alertness == EncounterAlertLevel.LOW
        )
    
    @property
    def is_in_danger(self) -> bool:
        return (
                self.is_ready and
                self._threats.enemy_detected and
                self._alertness == EncounterAlertLevel.HIGH
        )
    
    @property
    def is_checkmated(self) -> bool:
        return (
                self.has_been_deployed and
                self._threats.checkmate_exists and
                self._readiness == KingReadiness.CHECKMATED
        )
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, KingToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
