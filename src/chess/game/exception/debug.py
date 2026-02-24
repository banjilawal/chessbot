# src/chess/game/exception/debug.py

"""
Module: chess.game.exception.debug
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""


__all__ = [
    # ======================# GAME_DEBUG EXCEPTION #======================#
    "GameDebugException",
]

from chess.game import GameException
from chess.system import DebugException


# ======================# GAME_DEBUG EXCEPTION #======================#
class GameDebugException(GameException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Game operation failure.

    # PARENT:
        *   GameException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "GAME_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A GameDebugException was raised."