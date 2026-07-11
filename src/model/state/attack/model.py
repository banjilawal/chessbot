# src/model/state/attack/model.py

"""
Module: model.state.attack.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

from model import Maneuver, StateModel


T = TypeVar("T", bound="Token")

class Attack(StateModel, Generic[T]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Details about an attack.

    Attributes:
        id: int
        victim:
        maneuver: Maneuver
        attacker_benefit: Optional[int]

    Provides:
        -   are_attacking_same_victim(attack: Attack) -> bool
        
    Super Class:
        Model
    """
    _id: int
    _victim: T
    _maneuver: Maneuver
    _attacker_benefit: Optional[int]
    
    def __init__(
            self,
            id: int,
            victim: T,
            maneuver: Maneuver,
            attacker_benefit: Optional[int] | None = None,
    ):
        """
        Args:
            id: int
            victim: 
            maneuver: Maneuver
            attacker_benefit: Optional[int]
        """
        self._id = id
        self._victim: victim
        self._maneuver = maneuver
        self._attacker_benefit = attacker_benefit
        
    @property
    def id(self) -> int:
        return self._id
    
    @property
    def victim(self) -> T:
        return self._victim
        
    @property
    def maneuver(self) -> Maneuver:
        return self._maneuver
    
    @property
    def attacker_benefit(self) -> Optional[int]:
        return self._attacker_benefit
    
    @attacker_benefit.setter
    def attacker_benefit(self, attacker_benefit: Optional[int]):
        self._attacker_benefit = attacker_benefit
    
    def are_attacking_same_victim(self, attack: Attack) -> bool:
        if attack is self:
            return True
        if attack is None:
            return False
        return self._victim == attack.victim
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, Attack):
            return self._id == other.id
    
    def __hash__(self):
        return hash(self._id)
    


        
        
        
    