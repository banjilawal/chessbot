# src/assurance/validator/model/encounter/participant/table.py

"""
Module: assurance.validator.model.encounter.participant.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional

from domain import Coord


class EncounterParticipantTable:
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores EncounterParticipantTableGenerator success data.

    Attributes:
        participant: Optional[Coord]
        previous_participant: Optional[Coord]

    Provides:

    Super
    """
    _participant: Optional[Coord]
    _previous_participant: Optional[Coord]
    
    def __init__(
            self,
            participant: Optional[Coord] | None = None,
            previous_participant: Optional[Coord] | None = None,
    ):
        """
        Args:
            participant: Optional[Coord]
            previous_participant: Optional[Coord]
        """
        self._participant = participant
        self._previous_participant = previous_participant
        
    @property
    def participant(self) -> Optional[Coord]:
        return self._participant
    
    @property
    def previous_participant(self) -> Optional[Coord]:
        return self._previous_participant
    
    @property
    def size(self) -> int:
        return len(self.to_dict)
    
    @property
    def is_empty(self) -> bool:
        return self.size == 0
    
    @property
    def is_not_empty(self) -> bool:
        return not self.is_empty
    
    @property
    def is_full(self) -> bool:
        return self.size == 2
    
    @property
    def to_dict(self) -> Dict[str, Coord]:
        table = {
            "participant": self._participant,
            "previous_participant": self._previous_participant
        }
        return table