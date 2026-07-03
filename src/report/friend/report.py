# src/report/friend/report.py

"""
Module: report.friend.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional

from model import CombatantToken, KingToken, OpeningSquare, Token
from report import Report
from report.friend.state import FriendshipStatus


@dataclass
class FriendshipReport(Report):
    """
    Role:
        -   Test results

    Responsibilities:
        1.  Present information about the friendship between a Token pair.
        
    Attributes:
        hunter: Token
        status: FriendshipStatus
        friend: Optional[Token]
        enemy_king: Optional[KingToken]
        enemy_combatant: Optional[CombatantToken]
        
        are_friends: bool
        are_not_friends: bool
        target_is_enemy_king: bool
        target_is_enemy_combatant: bool
        
    Provides:

    Super Class:
        Report
    """
    hunter: Token
    status: FriendshipStatus
    friend: Optional[Token] = None
    enemy_king: Optional[KingToken] = None
    enemy_combatant: Optional[CombatantToken] = None
    
    @property
    def are_friends(self) -> bool:
        return (
                self.friend is not None and
                not self._enemy_exists and
                self.hunter.is_friend(self.friend) and
                self.status == FriendshipStatus.ARE_FRIENDS
        )
    
    @property
    def are_not_friends(self) -> bool:
        return not self.are_friends
    
    @property
    def target_is_enemy_king(self) -> bool:
        return (
                self.are_not_friends and
                self.enemy_king is not None and
                self.status == FriendshipStatus.TARGET_IS_ENEMY_KING
        )
    
    @property
    def target_is_enemy_combatant(self) -> bool:
        return (
                self.are_not_friends and
                self.enemy_combatant is not None and
                self.status == FriendshipStatus.TARGET_IS_ENEMY_COMBATANT
        )
    
    @property
    def _enemy_exists(self) -> bool:
        return (
                self.enemy_king is not None or
                self.enemy_combatant is not None
        )

    @classmethod
    def friends(cls, hunter: Token, friend: Token,) -> FriendshipReport:
        return cls(
            hunter=hunter,
            friend=friend,
            status=FriendshipStatus.ARE_FRIENDS,
        )
    
    @classmethod
    def king_target(cls, hunter: Token, enemy_king: KingToken) -> FriendshipReport:
        return cls(
            hunter=hunter,
            enemy_king=enemy_king,
            status=FriendshipStatus.TARGET_IS_ENEMY_KING,
        )
    
    @classmethod
    def combatant_target(cls, hunter: Token, enemy_combatant: CombatantToken) -> FriendshipReport:
        return cls(
            hunter=hunter,
            enemy_combatant=enemy_combatant,
            status=FriendshipStatus.TARGET_IS_ENEMY_COMBATANT,
        )
    
