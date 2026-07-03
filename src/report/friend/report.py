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

from model import CombatantToken, KingToken, Token
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
    def is_enemy_king(self) -> bool:
        return (
                self.is_free_enemy_king or
                self.is_checkmated_enemy_king
        )
    
    @property
    def is_free_enemy_king(self) -> bool:
        return (
                self.are_not_friends and
                self.enemy_king is not None and
                self.enemy_king.is_active and
                self.status == FriendshipStatus.FREE_ENEMY_KING
        )
    
    @property
    def is_checkmated_enemy_king(self) -> bool:
        return (
                self.are_not_friends and
                self.enemy_king is not None and
                self.enemy_king.is_checkmated and
                self.status == FriendshipStatus.CHECKMATED_ENEMY_KING
        )
    
    @property
    def is_undeployed_enemy_king(self) -> bool:
        return (
                self.are_not_friends and
                self.enemy_king is not None and
                self.enemy_king.is_not_deployed and
                self.status == FriendshipStatus.UNDEPLOYED_ENEMY_KING
        )
    
    @property
    def is_enemy_combatant(self) -> bool:
        return (
                self.are_not_friends and
                self.enemy_combatant is not None and
                self.status == FriendshipStatus.ENEMY_PRISONER or
                self.status == FriendshipStatus.FREE_ENEMY_COMBATANT
        )
    
    @property
    def is_free_enemy_combatant(self) -> bool:
        return (
                self.are_not_friends and
                self.enemy_combatant is not None and
                self.enemy_combatant.captor is None and
                self.status == FriendshipStatus.FREE_ENEMY_COMBATANT
        )
    
    @property
    def is_enemy_prisoner(self) -> bool:
        return (
                self.are_not_friends and
                self.enemy_combatant is not None and
                self.enemy_combatant.captor is not None and
                self.status == FriendshipStatus.ENEMY_PRISONER
        )
    
    @property
    def is_undeployed_enemy_combatant(self) -> bool:
        return (
                self.are_not_friends and
                self.enemy_combatant is not None and
                self.enemy_combatant.is_not_deployed and
                self.status == FriendshipStatus.ENEMY_PRISONER
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
    def free_enemy_king(cls, hunter: Token, enemy_king: KingToken) -> FriendshipReport:
        return cls(
            hunter=hunter,
            enemy_king=enemy_king,
            status=FriendshipStatus.FREE_ENEMY_KING,
        )
    
    @classmethod
    def checkmated_enemy_king(cls, hunter: Token, enemy_king: KingToken) -> FriendshipReport:
        return cls(
            hunter=hunter,
            enemy_king=enemy_king,
            status=FriendshipStatus.CHECKMATED_ENEMY_KING,
        )
    
    @classmethod
    def undeployed_enemy_king(cls, hunter: Token, enemy_king: KingToken) -> FriendshipReport:
        return cls(
            hunter=hunter,
            enemy_king=enemy_king,
            status=FriendshipStatus.UNDEPLOYED_ENEMY_KING,
        )
    
    @classmethod
    def free_enemy_combatant(cls, hunter: Token, enemy_combatant: CombatantToken) -> FriendshipReport:
        return cls(
            hunter=hunter,
            enemy_combatant=enemy_combatant,
            status=FriendshipStatus.FREE_ENEMY_COMBATANT,
        )
    
    @classmethod
    def enemy_prisoner(cls, hunter: Token, enemy_prisoner: CombatantToken) -> FriendshipReport:
        return cls(
            hunter=hunter,
            enemy_combatant=enemy_prisoner,
            status=FriendshipStatus.ENEMY_PRISONER,
        )
    
    @classmethod
    def undeployed_enemy_combatant(cls, hunter: Token, enemy_combatant: CombatantToken) -> FriendshipReport:
        return cls(
            hunter=hunter,
            enemy_combatant=enemy_combatant,
            status=FriendshipStatus.UNDEPLOYED_ENEMY_COMBATANT,
        )

    
