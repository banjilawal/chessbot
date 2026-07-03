# src/report/friend/report.py

"""
Module: report.friend.report
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class FriendshipStatus(Enum):
    ARE_FRIENDS = auto(),
    FREE_ENEMY_KING = auto(),
    FREE_ENEMY_COMBATANT = auto(),
    CHECKMATED_ENEMY_KING = auto()
    ENEMY_PRISONER = auto()
    UNDEPLOYED_ENEMY_KING = auto()
    UNDEPLOYED_ENEMY_COMBATANT = auto()