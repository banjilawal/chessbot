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


class CheckmateEnemyKing(Attack):
    """
    Role:
        - Model
        -  Data Holder

    Responsibilities:
        1.  Store details about attacking an enemy KingToken

    Attributes:
        victor: Token
        maneuver: Maneuver
        defeated_king: KingToken

    Provides:

    Super Class:
        Attack
    """
    
    def __init__(
            self,
            victor: Token,
            maneuver: Maneuver,
            defeated_king: KingToken,
    ):
        """
        Args:
            victor: Token
            maneuver: Maneuver
            defeated_king: KingToken
        """
        super().__init__(
            victim=defeated_king,
            attacker=victor,
            maneuver=maneuver,
            attacker_reward=defeated_king.rank.ransom
        )

    @property
    def victor(self) -> Token:
        return super().attacker
        
    @property
    def defeated_king(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.defeated_king
    
    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, CheckmateEnemyKing):
            return super().__eq__(other)
        return False
        
        
        
    