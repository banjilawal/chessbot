# src/model/state/attack/combatant/model/state.py

"""
Module: model.state.attack.combatant.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional

from model import Attack, CombatantToken, Maneuver


class AttackCombatant(Attack):
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
        enemy: CombatantToken
        benefit: Optional[int]

    Provides:

    Super Class:
        Attack
    """
    _enemy: CombatantToken
    
    def __init__(
            self,
            id: int,
            maneuver: Maneuver,
            enemy: CombatantToken,
            benefit: Optional[int] | None,
    ):
        """
        Args:
            id: int
            maneuver: Maneuver
            enemy: CombatantToken
            benefit: Optional[int]
        """
        super().__init__(
            id=id,
            maneuver=maneuver,
            benefit=benefit,
        )
        self._enemy = enemy
        
    @property
    def enemy(self) -> CombatantToken:
        return self._enemy
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, AttackCombatant):
            return (
                    super().__eq__(other) and
                    self.enemy == other.enemy
            )
        return False
    
    def __hash__(self):
        return super().__hash__()
        
        
        
    