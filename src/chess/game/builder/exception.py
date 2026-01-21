# src/chess/game/builder/exception.py

"""
Module: chess.game.builder.exception
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.game import GameException
from chess.system import BuildFailedException


__all__ = [
    # ======================# GAME_BUILD_FAILURE EXCEPTION #======================#
    "GameBuildFailedException",
]


# ======================# GAME_BUILD_FAILURE EXCEPTION #======================#
class GameBuildFailedException(GameException, BuildFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Game build creates an exception. Failed check exceptions are encapsulated
        in an GameBuildFailedException which is sent to the caller in a BuildResult.
    2.  The GameBuildFailedException provides a trace for debugging and application recovery.

    # PARENT:
        *   GameException
        *   BuildFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_BUILD_FAILED"
    DEFAULT_MESSAGE = "Game build failed."