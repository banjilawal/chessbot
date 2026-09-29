# src/domain/model/searchable/encounter/stalemate/model.py.py

"""
Module: domain.model.searchable.encounter.stalemate.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, cast

from domain import KingToken, Encounter, Maneuver, PlayerColorBinder, Square, Token


class StalemateEncounter(Encounter):
    """
    Role:
        - Model
        - Data Holder

    Responsibilities:
        1.  Details about a StalemateEncounter.

    Attributes:
        id: int
        counter_maneuver: Maneuver

    Provides:
        
    Super Class:
        Encounter
    """
    _counter_maneuver: Maneuver

    
    def __init__(
            self,
            id: int,
            attacker_maneuver: Maneuver,
            counter_maneuver: Maneuver,
            location: Optional[Square] | None = None,
            attacker_reward: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            attacker_maneuver: Maneuver
            counter_maneuver: Maneuver
            location: Optional[Square]
            attacker_reward: Optional[int]
        """
        super().__init__(
            id=id,
            victim=counter_maneuver.traveler,
            attacker_maneuver=attacker_maneuver,
            location=location,
            attacker_reward=attacker_reward,
        )
        
    @property
    def players(self) -> PlayerColorBinder:
        return self.attacker_maneuver.traveler.team.board.arena.player_binder

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, StalemateEncounter):
            return self.id == other.id
        return False
    


        
        
        
    