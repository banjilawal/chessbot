# src/domain/model/searchable/encounter/kill/model.py.py

"""
Module: domain.model.searchable.encounter.kill.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, cast

from domain import CombatantToken, Encounter, Maneuver, Square, Token


class KillEncounter(Encounter):
    """
    Role:
        - Model
        - Data Holder

    Responsibilities:
        1.  Details about an encounter.

    Attributes:
        id: int
        victim: CombatantToken
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
            counter_maneuver: CombatantToken,
            attacker_maneuver: Maneuver,
            location: Optional[Square] | None = None,
            attacker_reward: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            counter_maneuver: CombatantToken
            attacker_maneuver: Maneuver
            location: Optional[Square]
            attacker_reward: Optional[int]
        """
        super().__init__(
            id=id,
            counter_maneuver=counter_maneuver,
            attacker_maneuver=attacker_maneuver,
            location=location,
            attacker_reward=attacker_reward,
        )
        
    @property
    def victim(self) -> CombatantToken:
        return cast(CombatantToken, super().victim)
    
    @property
    def attacker(self) -> Token:
        return self.initiater

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, KillEncounter):
            return self.id == other.id
        return False
    


        
        
        
    