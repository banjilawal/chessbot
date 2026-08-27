# src/domain/model/searchable/walk/attack/check/model.py

"""
Module: domain.model.searchable.walk.attack.check.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import cast

from domain import Attack, KingToken, Maneuver, Token


class CheckEnemyKing(Attack):
    """
    Role:
        - Model
        -  Data Holder

    Responsibilities:
        1.  Store details about attacking an enemy KingToken

    Attributes:
        checker: Token
        maneuver: Maneuver
        enemy_king: KingToken

    Provides:

    Super Class:
        Attack
    """
    
    def __init__(
            self,
            checker: Token,
            maneuver: Maneuver,
            enemy_king: KingToken,
    ):
        """
        Args:
            checker: Token
            maneuver: Maneuver
            enemy_king: KingToken
        """
        super().__init__(
            victim=enemy_king,
            attacker=checker,
            maneuver=maneuver,
            attacker_reward=enemy_king.rank.ransom
        )

    @property
    def checker(self) -> Token:
        return super().attacker
        
    @property
    def enemy_king(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.enemy_king
    
    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, KingToken):
            return super().__eq__(other)
        return False
        
        
        
    