# src/chess/game/builder/exception.py

"""
Module: chess.game.builder.exception
Author: Banji Lawal
Created: 2025-09-04
version: 1.0.0
"""

from chess.game import GameException
from chess.system import BuildException


__all__ = [
    # ======================# GAME_BUILD_FAILURE EXCEPTION #======================#
    "GameBuildException",
]


# ======================# GAME_BUILD_FAILURE EXCEPTION #======================#
class GameBuildException(GameException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the Game build creates an exception. Failed check exceptions are encapsulated
        in an GameBuildException which is sent to the caller in a BuildResult.
    2.  The GameBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   GameException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_BUILD_FAILED"
    DEFAULT_MESSAGE = "Game build failed."