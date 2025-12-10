# src/chess/game/snapshot/context/exception.py

"""
Module: chess.game.snapshot.context.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import ContextException

__all__ = [
    # ======================# GAME_CONTEXT EXCEPTION SUPER CLASS #======================#
    "GameSnapshotContextException",
]


# ======================# GAME_CONTEXT EXCEPTION SUPER CLASS #======================#
class GameSnapshotContextException(ContextException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by GameSnapshotContext objects.
    2.  Catchall for conditions which are not covered by lower level GameSnapshotContext exceptions.

    # PARENT
        *   ContextException

    # PROVIDES:
    GameSnapshotContextException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_CONTEXT_ERROR"
    DEFAULT_ERROR_CODE = "GameSnapshotContext raised an exception."