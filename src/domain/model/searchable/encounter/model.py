# src/domain/model/searchable/encounter/model.py.py

"""
Module: domain.model.searchable.encounter.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Optional

from domain import Maneuver, SearchableModel, Square, Token


class Encounter(SearchableModel, ABC):
    """
    Role:
        - Model
        - Data Holder

    Responsibilities:
        1.  Details about an encounter.

    Attributes:
        id: int
        victim: Token
        maneuver: Maneuver
        location: Square
        attacker_reward: int

    Provides:
        
    Super Class:
        SearchableModel
    """
    _id: int
    _victim: Token
    _location: Square
    _maneuver: Maneuver
    _attacker_reward: int

    
    def __init__(
            self,
            id: int,
            victim: Token,
            maneuver: Maneuver,
            location: Optional[Square] | None = None,
            attacker_reward: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            victim: Token
            maneuver: Maneuver
            location: Optional[Square]
            attacker_reward: Optional[int]
        """
        self._id = id
        self._victim = victim
        self._maneuver = maneuver
        self._location = location or maneuver.path.endpoints.destination
        self._attacker_reward = attacker_reward or victim.rank.ransom
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def victim(self) -> Token:
        return self._victim
    
    @property
    def maneuver(self) -> Maneuver:
        return self._maneuver
    
    @property
    def initiater(self) -> Token:
        return self._maneuver.traveler
        
    @property
    def attacker_reward(self) -> int:
        return self._attacker_reward
    
    @property
    def location(self) -> Square:
        return self._location
    
    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, Encounter):
            return (
                    self.id == other.id and
                    self._initiater == other.attacker and
                    self._victim == other.victim
            )
        return False
    


        
        
        
    