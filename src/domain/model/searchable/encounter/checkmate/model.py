# src/domain/model/searchable/encounter/checkmate/model.py.py

"""
Module: domain.model.searchable.encounter.checkmate.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Dict, Optional, cast

from config import GameColor
from domain import KingToken, Encounter, Maneuver, Player, Square, Token


class CheckmateEncounter(Encounter):
    """
    Role:
        - Model
        - Data Holder

    Responsibilities:
        1.  Details about an encounter.

    Attributes:
        id: int
        victim: KingToken
        maneuver: Maneuver
        location: Square
        attacker_reward: int

    Provides:
        
    Super Class:
        Encounter
    """

    
    def __init__(
            self,
            id: int,
            victim: KingToken,
            attacker_maneuver: Maneuver,
            location: Optional[Square] | None = None,
            attacker_reward: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            victim: KingToken
            attacker_maneuver: Maneuver
            location: Optional[Square]
            attacker_reward: Optional[int]
        """
        super().__init__(
            id=id,
            victim=victim,
            attacker_maneuver=attacker_maneuver,
            location=location,
            attacker_reward=attacker_reward,
        )
        
    @property
    def looser(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.looser

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, CheckmateEncounter):
            return self.id == other.id
        return False
    


        
        
        
    