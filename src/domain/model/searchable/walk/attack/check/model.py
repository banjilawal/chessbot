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


class CheckWarning(Attack):
    """
    Role:
        - Model
        - Data Holder

    Responsibilities:
        1.  Store details about checking a King.

    Attributes:
        attacker: Token
        maneuver: Maneuver
        enemy_king: KingToken

    Provides:

    Super Class:
        Attack
    """
    
    def __init__(
            self,
            attacker: Token,
            maneuver: Maneuver,
            checked_king: KingToken,
    ):
        """
        Args:
            attacker: Token
            maneuver: Maneuver
            checked_king: KingToken
        """
        super().__init__(
            victim=checked_king,
            attacker=attacker,
            maneuver=maneuver,
            attacker_reward=checked_king.rank.ransom
        )

    @property
    def attacker(self) -> Token:
        return super().attacker
        
    @property
    def checked_king(self) -> KingToken:
        return cast(KingToken, super().victim)
    
    @property
    def victim(self) -> KingToken:
        return self.checked_king
    
    def __eq__(self, other) -> bool:
        if other is None:
            return False
        if other == self:
            return True
        if isinstance(other, CheckWarning):
            return super().__eq__(other)
        return False
        
        
        
    