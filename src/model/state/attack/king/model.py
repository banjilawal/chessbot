# src/model/state/attack/king/model.py

"""
Module: model.state.attack.king.model
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Optional, cast

from model import Attack, KingAttackState, KingToken, Maneuver, Token


class AttackKing(Attack[KingToken]):
    """
    Role:
        -   Model
        -   Data Holder

    Responsibilities:
        1.  Provide information about a Path which might be used to attack
            an victim's KingToken.

    Attributes:
        id: int
        maneuver: Maneuver
        victim: KingToken
        benefit: Optional[int]

    Provides:

    Super Class:
        Attack
    """
    _attack_state: KingAttackState
    
    def __init__(
            self,
            id: int,
            maneuver: Maneuver,
            victim: KingToken,
            attacker_benefit: Optional[int] | None,
    ):
        """
        Args:
            id: int
            victim: KingToken
            maneuver: Maneuver
            attacker_benefit: Optional[int]
        """
        super().__init__(
            id=id,
            victim=victim,
            maneuver=maneuver,
            attacker_benefit=attacker_benefit
        )
        self._attack_state = KingAttackState.ATTACK_NOT_COMPLETED
    
    @property
    def attacker(self) -> Token:
        return self._maneuver.token
        
    @property
    def victim(self) -> KingToken:
        return cast(KingToken, self.victim)
    
    @property
    def attack_state(self) -> KingAttackState:
        return self._attack_state
    
    @property
    def check_completed(self) -> bool:
        return (
                self._maneuver.token.has_checked_enemy_king and
                self._maneuver.path.endpoints.destination.occupant == self.victim and
                self._attack_state == KingAttackState.CHECKED_ENEMY_KING
        )
    
    @property
    def check_not_completed(self) -> bool:
        return not self.check_completed
    
    def __eq__(self, other):
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, AttackKing):
            return (
                    super().__eq__(other) and
                    self.victim == other.victim
            )
        return False
    
    def __hash__(self):
        return super().__hash__()
        
        
        
    