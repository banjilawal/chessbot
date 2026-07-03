# src/model/model/attack.py

"""
Module: model.model.attack
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import Maneuver, Square, Token


class Attack:
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
        benefit: Optional[int]

    Provides:

    Super Class:
    """
    _id: int
    _maneuver: Maneuver
    _benefit: Optional[int]
    
    def __init__(
            self,
            id: int,
            maneuver: Maneuver,
            benefit: Optional[int] | None,
    ):
        """
        Args:
            id: int
            maneuver: Maneuver
            benefit: Optional[int]
        """
        self._id = id
        self._maneuver = maneuver
        self._benefit = benefit
        
    @property
    def id(self) -> int:
        return self._id
        
    @property
    def maneuver(self) -> Maneuver:
        return self._maneuver
        
    @property
    def attacker(self) -> Token:
        return self._maneuver.token
    
    @property
    def attack_origin(self) -> Square:
        return self._maneuver.path.origin
    
    @property
    def target_square(self) -> Square:
        return self._maneuver.path.origin
    
    @property
    def benefit(self) -> Optional[int]:
        return self._benefit
    
    @benefit.setter
    def benefit(self, benefit: Optional[int]):
        self._benefit = benefit
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, Attack):
            return (
                    self._id == other.id and
                    self._maneuver == other.maneuver and
                    self._benefit == other.benefit
            )
        return False
    
    def __hash__(self):
        return hash(self._id)
        
        
        
    