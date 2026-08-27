# src/domain/model/searchable/attack/dossier/model.py

"""
Module: domain.model.searchable.walk.attack.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations

from abc import ABC
from typing import Optional

from domain import Maneuver, SearchableModel, Token


class Attack(SearchableModel, ABC,):
    """
    Role:
        - Model
        -  Data Holder

    Responsibilities:
        1.  Details about an attack.

    Attributes:
        victim: Token
        attacker: Token
        maneuver: Maneuver
        attacker_reward: int

    Provides:
        -  def are_attacking_same_victim(attack: Attack) -> bool
        
    Super Class:
        SearchableModel
    """
    _victim: Token
    _attacker: Token
    _maneuver: Maneuver
    _attacker_reward: int
    
    def __init__(
            self,
            victim: Token,
            attacker: Token,
            maneuver: Maneuver,
            attacker_reward: Optional[int] | None = None,
    ):
        """
        Args:
            victim: Token
            attacker: Token
            maneuver: Maneuver
            attacker_reward: Optional[int]
        """
        self._victim = victim
        self._attacker = attacker
        self._maneuver = maneuver
        self._attacker_reward = attacker_reward or victim.rank.ransom
    
    @property
    def victim(self) -> Token:
        return self._victim
    
    @property
    def attacker(self) -> Token:
        return self._attacker
        
    @property
    def maneuver(self) -> Maneuver:
        return self._maneuver
    
    @property
    def attacker_reward(self) -> int:
        return self._attacker_reward
    
    def are_attacking_same_victim(self, attack: Attack) -> bool:
        if attack is self:
            return True
        if attack is None:
            return False
        return self._victim == attack.victim
    
    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, Attack):
            return (
                    self._attacker == other.attacker and
                    self._victim == other.victim
            )
        return False
    


        
        
        
    