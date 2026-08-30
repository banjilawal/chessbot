# src/domain/model/searchable/walk/attack/checkmate/model.py

"""
Module: domain.model.searchable.walk.attack.checkmate.model
Author: Banji Lawal
Created: 2026-04-03
version: 0.0.2
"""

from __future__ import annotations


from typing import cast

from domain import Attack, KingToken, Maneuver, Token


class MateEnemyKing(Attack):
    """
    Role:
        - Model
        -  Data Holder

    Responsibilities:
        1.  Store details about checkmating an enemy KingToken.

    Attributes:
        victor: Token
        maneuver: Maneuver
        mated_king: KingToken

    Provides:

    Super Class:
        Attack
    """
    
    def __init__(
            self,
            victor: Token,
            maneuver: Maneuver,
            mated_king: KingToken,
    ):
        """
        Args:
            victor: Token
            maneuver: Maneuver
            mated_king: KingToken
        """
        super().__init__(
            victim=mated_king,
            attacker=victor,
            maneuver=maneuver,
            attacker_reward=mated_king.rank.ransom
        )
        
        
    @property
    def mated_king(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    
    @property
    def victim(self) -> KingToken:
        return self.mated_king
    
    
    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, MateEnemyKing):
            return super().__eq__(other)
        return False
        
        
        
    