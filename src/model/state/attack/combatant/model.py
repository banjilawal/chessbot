# src/model/state/attack/combatant/model.py

"""
Module: model.state.attack.combatant.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, cast

from model import Attack, CombatantAttackState, CombatantToken, Maneuver, Token


class AttackCombatant(Attack[CombatantToken]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Provide information about a Path which might be used to attack
            an victim's CombatantToken.

    Attributes:
        id: int
        maneuver: Maneuver
        victim: CombatantToken
        benefit: Optional[int]

    Provides:

    Super Class:
        Attack
    """
    _attack_state: CombatantAttackState
    
    def __init__(
            self,
            id: int,
            maneuver: Maneuver,
            victim: CombatantToken,
            attacker_benefit: Optional[int] | None,
    ):
        """
        Args:
            id: int
            victim: CombatantToken
            maneuver: Maneuver
            attacker_benefit: Optional[int]
        """
        super().__init__(
            id=id,
            victim=victim,
            maneuver=maneuver,
            attacker_benefit=attacker_benefit
        )
        self._attack_state = CombatantAttackState.ATTACK_NOT_COMPLETED
    
    @property
    def attacker(self) -> Token:
        return self.maneuver.token
        
    @property
    def victim(self) -> CombatantToken:
        return cast(CombatantToken, self.victim)
    
    @property
    def attack_state(self) -> CombatantAttackState:
        return self._attack_state
    
    @property
    def is_attack_completed(self) -> bool:
        return (
            self._maneuver.is_completed and
            self.victim.is_captured and
            self.victim.captor == self.attacker and
            self._attack_state == CombatantAttackState.ATTACK_COMPLETED
        )
    
    @property
    def is_attack_not_completed(self) -> bool:
        return self.is_attack_completed
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, AttackCombatant):
            return (
                    super().__eq__(other) and
                    self.victim == other.victim
            )
        return False
    
    def __hash__(self):
        return super().__hash__()
        
        
        
    