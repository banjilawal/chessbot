# src/domain/model/searchable/walk/attack/kill/model.py

"""
Module: domain.model.searchable.walk.attack.kill.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import Optional, cast

from domain import Attack, CombatantToken, Maneuver, Token


class KillEnemyCombatant(Attack):
    """
    Role:
        - Model
        -  Data Holder

    Responsibilities:
        1.  Store details about attacking an enemy CombatantToken

    Attributes:
        killer: Token
        maneuver: Maneuver
        victim: CombatantToken
        attacker_reward: int

    Provides:

    Super Class:
        Attack
    """
    
    def __init__(
            self,
            killer: Token,
            maneuver: Maneuver,
            victim: CombatantToken,
            attacker_reward: Optional[int] | None = None,
    ):
        """
        Args:
            killer: Token
            maneuver: Maneuver
            victim: CombatantToken
            attacker_reward: Optional[int]
        """
        super().__init__(
            victim=victim,
            attacker=killer,
            maneuver=maneuver,
            attacker_reward=attacker_reward or victim.rank.ransom
        )

    @property
    def killer(self) -> Token:
        return super().attacker
        
    @property
    def victim(self) -> CombatantToken:
        return cast(CombatantToken, super().victim)
    
    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, KillEnemyCombatant):
            return super().__eq__(other)
        return False
        
        
        
    