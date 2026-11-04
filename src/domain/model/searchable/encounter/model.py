# src/domain/model/searchable/encounter/model.py

"""
Module: domain.model.searchable.encounter.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Dict, Optional

from domain import Account, Archetype, Maneuver, Path, Square, Token


class Encounter(Maneuver, ABC):
    """
    Role:
        - Model
        - Data Holder

    Responsibilities:
        1.  Details about an encounter.

    Attributes:
        id: int
        victim: Token
        attacker_reward: Optional[int]

    Provides:
        
    Super Class:
        Maneuver
    """
    _id: int
    _victim: Token

    
    def __init__(
            self,
            id: int,
            victim: Token,
            attacker: Token,
            attacker_path: Path,
            attacker_reward: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            victim: Token
            attacker: Token
            attacker_path: Path
            attacker_reward: Optional[int]
        """
        super().__init__(path=attacker_path, traveler=attacker)
        self._id = id
        self._victim = victim
        self._attacker_reward = attacker_reward or victim.rank.persona.ransom
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def victim(self) -> Token:
        return self._victim
    
    @property
    def attacker(self) -> Token:
        return self.traveler
    
    @property
    def location(self) -> Square:
        return self.destination
        
    @property
    def attacker_reward(self) -> int:
        return self._attacker_reward
    
    @property
    def score(self) -> Dict[str, Dict[Archetype, Account]]:
        return {}
    
    @property
    def consistency_exists(self) -> bool:
        return (
            self._location.occupant == self._victim and
            self._location.coord == self._victim.footstep.position
        )
    
    @property
    def is_not_consistent(self) -> bool:
        return not self.consistency_exists
    
    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, Encounter):
            return self.id == other.id
        return False
    


        
        
        
    