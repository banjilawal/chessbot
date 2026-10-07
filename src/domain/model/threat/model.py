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
        checkmate: Optional[CheckmateEncounter]
        encounter_warning: Optional[EncounterWarning]

     Provides:

     Super Class:
        Model
     """
    _checkmate: Optional[CheckmateEncounter]
    _encounter_warning: Optional[EncounterWarning]

    
    
    def __init__(
            self,
            checkmate: Optional[CheckmateEncounter] | None = None,
            encounter_warning: Optional[EncounterWarning] | None = None,
    ):
        """
        Args:
            checkmate: Optional[CheckmateEncounter]
            encounter_warning: Optional[EncounterWarning]
        """
        super().__init__()
        self._checkmate = checkmate
        self._encounter_warning = encounter_warning
    
    
@property
def encounter_warning(self) -> Optional[EncounterWarning]:
    return self._encounter_warning