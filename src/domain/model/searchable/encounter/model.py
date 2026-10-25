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

from domain import Account, Archetype, Encounterable, Square, SearchableModel, Square, Token


class Encounter(SearchableModel, Encounterable, ABC):
    """
    Role:
        - Model
        - Data Holder

    Responsibilities:
        1.  Details about an encounter.

    Attributes:
        id: int
        victim: Token
        location: Square
        attacker_reward: Optional[int]

    Provides:
        
    Super Class:
        SearchableModel
    """
    _id: int
    _victim: Token
    _location: Square
    _attacker_reward: int

    
    def __init__(
            self,
            id: int,
            victim: Token,
            location: Square,
            attacker_reward: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            victim: Token
            location: Square
            attacker_reward: Optional[int]
        """
        self._id = id
        self._victim = victim
        self._location = location
        self._attacker_reward = attacker_reward or victim.rank.persona.ransom
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def victim(self) -> Token:
        return self._victim
    
    @property
    def location(self) -> Square:
        return self._location
        
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
    


        
        
        
    