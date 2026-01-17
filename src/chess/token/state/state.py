# src/chess/token/state/state.py

"""
Module: chess.token.state.state
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from enum import Enum, auto


class TokenState(Enum):
    ACTIVE_KING = auto(),
    KING_IN_CHECK = auto(),
    CHECKMATED_KING = auto(),
    ACTIVE_COMBATANT = auto(),
    CAPTURED_COMBATANT = auto(),
    BLOCKED_COMBATANT = auto(),
    PROMOTED_PAWN = auto(),
    NOT_OPENED = auto(),
    FORMATION__ASSIGNED =  auto(),
    FORMATION_ENACTED = auto(),
    FORMED_ON_BOARD = auto()
    REMOVED_FROM_BOARD = auto()
    REGISTERED_HOSTAGE = auto(),
