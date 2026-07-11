# src/model/state/model/state/attack.py

"""
Module: model.state.model.attack
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations

from abc import ABC
from typing import Generic, Optional, TypeVar

from model import Maneuver

T = TypeVar("T", bound="Token")


class Attack(ABC, Generic[T]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Provide information about a Path which might be used to attack
            an enemy's CombatantToken.

    Attributes:
        id: int
        maneuver: Maneuver
        attacker_benefit: Optional[int]

    Provides:

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
    def maneuver(self) -> Maneuver:
        return self._maneuver
        
    @property
    def victim(self) -> T:
        return self._maneuver.token
    
    @property
    def attacker_benefit(self) -> Optional[int]:
        return self._attacker_benefit
    
    @attacker_benefit.setter
    def attacker_benefit(self, attacker_benefit: Optional[int]):
        self._attacker_benefit = attacker_benefit
    
    def is_same_attack(self, attack: Attack) -> bool:
        if attack is self: return True
        if attack is None: return False
        return (
                self._maneuver.token == attack.maneuver.token and
                self.maneuver.is_same_path(attack.maneuver)
        )
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, Attack):
            return (
                    self._id == other.id and
                    self._maneuver == other.maneuver and
                    self._attacker_benefit == other.attacker_benefit
            )
        return False
    
    def __hash__(self):
        return hash(self._id)
    


        
        
        
    