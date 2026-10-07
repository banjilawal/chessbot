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
    EncounterAlertLevel, EncounterWarning, CheckmateEncounter, TokenDeployment, Formation, HomeSquare, Team,
    Token, KingReadiness, TokenReadiness, Walk
)



class KingToken(Token):
    """
    Role:
        - Stateful Data-Holder

    Responsibilities:
        1. Token that can be checkmated not captured.

    Attributes:
        id: int
        team: Team
        walk: Walk
        formation: Formation
        home_square: HomeSquare
        checkmate:
        readiness_state: TokenActivityState



    Super Class:
        Token
    """
    _readiness: KingReadiness
    _alertness_level: EncounterAlertLevel
    _checkmate: Optional[CheckmateEncounter]
    _encounter_warning: Optional[EncounterWarning]

    

    def __init__(
            self,
            id: int,
            team: Team,
            formation: Formation,
            home_square: HomeSquare,
            walk: Optional[Walk] | None = None,
    ):
        """
        Args:
            id: int
            team: Team
            formation: Formation
            home_square: Square
            walk: Optional[Walk]
        """
        super().__init__(
            id=id,
            team=team,
            formation=formation,
            home_square=home_square,
            walk=walk,
        )
        self._checkmate = None
        self._encounter_warning = None
        self._readiness = KingReadiness.NOT_READY
        self._alertness_level = EncounterAlertLevel.LOW
        
    @property
    def readiness(self) -> KingReadiness:
        return self._readiness
    
    @readiness.setter
    def readiness(self, other: KingReadiness):
        self._readiness = other
        
        
    @property
    def alertness_level(self) -> EncounterAlertLevel:
        return self._alertness_level
    
    @alertness_level.setter
    def alertness_level(self, other: EncounterAlertLevel):
        self._alertness_level = other
        
    @property
    def checkmate(self) -> Optional[CheckmateEncounter]:
        return self._checkmate
    
    @checkmate.setter
    def checkmate(self, other: CheckmateEncounter):
        if self._checkmate is None:
            self._checkmate = other
        
    @property
    def encounter_warning(self) -> Optional[EncounterWarning]:
        return self._encounter_warning
    
    @encounter_warning.setter
    def encounter_warning(self, other: EncounterWarning):
        self._encounter_warning = other
        
    @property
    def is_ready(self) -> bool:
        return (
                self.has_been_deployed and
                self._checkmate is None and
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
                self._encounter_warning is None and
                self._alertness_level == EncounterAlertLevel.LOW
        )
    
    @property
    def is_in_danger(self) -> bool:
        return (
                self.is_ready and
                self._encounter_warning is not None and
                self._alertness_level == EncounterAlertLevel.HIGH
        )
    
    @property
    def is_checkmated(self) -> bool:
        return (
                self.has_been_deployed and
                self.checkmate is not None and
                self._readiness == KingReadiness.CHECKMATED
        )
    
    def __eq__(self, other):
        if super().__eq__(other):
            if isinstance(other, KingToken):
                return True
        return False
    
    def __hash__(self):
        return hash(self._id)
