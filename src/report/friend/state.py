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
    TARGET_IS_ENEMY_KING = auto(),
    TARGET_IS_ENEMY_COMBATANT = auto(),