# src/assurance/validator/model/encounter/position/table.py

"""
Module: assurance.validator.model.encounter.position.table
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from typing import Dict, Optional

from domain import Coord


class EncounterPositionTable:
    """
    Role
        - Data Holder

    Responsibilities:
        1.  Stores EncounterPositionTableGenerator success data.

    Attributes:
        position: Optional[Coord]
        previous_position: Optional[Coord]

    Provides:

    Super
    """
    _position: Optional[Coord]
    _previous_position: Optional[Coord]
    
    def __init__(
            self,
            position: Optional[Coord] | None = None,
            previous_position: Optional[Coord] | None = None,
    ):
        """
        Args:
            position: Optional[Coord]
            previous_position: Optional[Coord]
        """
        self._position = position
        self._previous_position = previous_position
        
    @property
    def position(self) -> Optional[Coord]:
        return self._position
    
    @property
    def previous_position(self) -> Optional[Coord]:
        return self._previous_position
    
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
            "position": self._position,
            "previous_position": self._previous_position
        }
        return table