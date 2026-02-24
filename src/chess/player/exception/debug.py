# src/chess/player/exception/debug.py

"""
Module: chess.player.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# PLAYER_DEBUG EXCEPTION #======================#
    "PlayerDebugException",
]

from chess.player import PlayerException
from chess.system import DebugException


# ======================# PLAYER_DEBUG EXCEPTION #======================#
class PlayerDebugException(PlayerException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Player operation failure.

    # PARENT:
        *   PlayerException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "PLAYER_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A PlayerDebugException was raised."