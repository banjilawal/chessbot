# src/domain/model/danger/model.py

"""
Module: domain.model.danger.model
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations

from typing import Optional

from domain import CheckmateEncounter, EncounterWarning, Model


class ThreatTable(Model):
    """
     Role:
         - Data Holder

     Responsibilities:
        2.  Direct a Team's pieces that are in an Arena's Board during a Game.

     Attributes:
        threat: Optional[EncounterWarning]
        checkmate: Optional[CheckmateEncounter]

     Provides:

     Super Class:
        Model
     """
    _threat: Optional[EncounterWarning]
    _checkmate: Optional[CheckmateEncounter]
    
    def __init__(
            self,
            threat: Optional[EncounterWarning] | None = None,
            checkmate: Optional[CheckmateEncounter] | None = None,
    ):
        """
        Args:
            threat: Optional[EncounterWarning]
            checkmate: Optional[CheckmateEncounter]
        """
        super().__init__()
        self._threat = threat
        self._checkmate = checkmate
    
    @property
    def threat(self) -> Optional[EncounterWarning]:
        return self._threat
    
    @threat.setter
    def threat(self, other: EncounterWarning):
        self._threat = other
        
    @property
    def checkmate(self) -> Optional[CheckmateEncounter]:
        return self._checkmate
    
    @checkmate.setter
    def checkmate(self, other: CheckmateEncounter):
        self._checkmate = other
        
    @property
    def size(self) -> int:
        return len([self._threat, self._checkmate])
    
    @property
    def enemy_detected(self) -> bool:
        return self._threat is not None
    
    @property
    def no_enemy_detected(self) -> bool:
        return not self.enemy_detected
    
    @property
    def checkmate_exists(self) -> bool:
        return self._checkmate is not None
    
    @property
    def has_not_been_checkmated(self) -> bool:
        return not self.checkmate_exists