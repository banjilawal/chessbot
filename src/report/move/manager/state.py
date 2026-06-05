# src/report/move/manager/state.py

"""
Module: report.move.manager.state
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from enum import Enum, auto


class MoveDecision(Enum):
    ATTACK_ENEMY_SQUARE = auto(),
    OCCUPY_EMPTY_SQUARE = auto(),
    AVOID_ENEMY_DESTINATION = auto(),
    CHECKED_SQUARE_BLOCK = auto(),
    FRIENDLY_SQUARE_BLOCK = auto(),
    INACTIVE_COMBATANT_MOVE_DENIAL = auto(),
    CHECKMATED_KING_MOVE_DENIAL = auto(),