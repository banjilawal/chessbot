# src/domain/model/searchable/encounter/mate/model.py.py

"""
Module: domain.model.searchable.encounter.mate.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, cast

from domain import KingToken, Encounter, Maneuver, Square, Token


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
            maneuver: Maneuver,
            location: Optional[Square] | None = None,
            attacker_reward: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            victim: KingToken
            maneuver: Maneuver
            location: Optional[Square]
            attacker_reward: Optional[int]
        """
        super().__init__(
            id=id,
            victim=victim,
            maneuver=maneuver,
            location=location,
            attacker_reward=attacker_reward,
        )
        
    @property
    def looser(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.looser
    
    @property
    def victor(self) -> Token:
        return self.initiater

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, CheckmateEncounter):
            return self.id == other.id
        return False
    


        
        
        
    