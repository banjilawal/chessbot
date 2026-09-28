# src/domain/model/searchable/encounter/warning/model.py.py

"""
Module: domain.model.searchable.encounter.warning.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, cast

from domain import KingToken, Encounter, Maneuver, Path, Square, Token


class EncounterWarning(Encounter):
    """
    Role:
        - Model
        - Data Holder

    Responsibilities:
        1.  Details about an encounter.

    Attributes:
        id: int
        maneuver: Maneuver
        warning_recipient: KingToken
        current_safe_square: Square
        danger_zone: Optional[Square]
        attacker_reward: Optional[int]

    Provides:
        
    Super Class:
        Encounter
    """
    _current_safe_square: Square


    def __init__(
            self,
            id: int,
            maneuver: Maneuver,
            warning_recipient: KingToken,
            current_safe_square: Square,
            danger_zone: Optional[Square] | None = None,
            attacker_reward: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            maneuver: Maneuver
            warning_recipient: KingToken
            current_safe_square: Square
            danger_zone: Optional[Square]
            attacker_reward: Optional[int]
        """
        super().__init__(
            id=id,
            victim=warning_recipient,
            maneuver=maneuver,
            location=danger_zone,
            attacker_reward=attacker_reward,
        )
        self._current_safe_square = current_safe_square
        
    @property
    def warning_recipient(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.warning_recipient
    
    @property
    def threat(self) -> Token:
        return self.initiater
    
    @property
    def current_safe_square(self) -> Square:
        return self._current_safe_square
    
    @property
    def threat_path(self) -> Path:
        return self.maneuver.path

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, EncounterWarning):
            return self.id == other.id
        return False
    


        
        
        
    