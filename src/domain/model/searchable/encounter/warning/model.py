# src/domain/model/searchable/encounter/warning/model.py

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
        checked_king: KingToken
        enemy_origin: Square
        enemy_origin: Optional[Square]
        attacker_reward: Optional[int]

    Provides:
        
    Super Class:
        Encounter
    """
    
    _enemy: Token
    _enemy_origin: Square



    def __init__(
            self,
            id: int,
            enemy: Token,
            checked_king: KingToken,
            enemy_origin: Square,
            location: Square,
            attacker_reward: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            enemy: Token,
            checked_king: KingToken
            location: Square
            enemy_origin: Square
            attacker_reward: Optional[int]
        """
        super().__init__(
            id=id,
            victim=checked_king,
            location=location,
            attacker_reward=attacker_reward,
        )
        self._enemy = enemy
        self._enemy_origin = enemy_origin
        
    @property
    def checked_king(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.checked_king
    
    @property
    def enemy(self) -> Token:
        return self._enemy
    
    @property
    def enemy_origin(self) -> Square:
        return self._enemy_origin
    
    @property
    def consistency_exists(self) -> bool:
        return (
            super().consistency_exists and
            self._enemy_origin.occupant == self._enemy and
            self._enemy_origin.coord == self._enemy.footstep.position
        )
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists

    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, EncounterWarning):
            return self.id == other.id
        return False
    


        
        
        
    