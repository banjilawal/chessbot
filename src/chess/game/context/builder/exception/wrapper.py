# src/chess/game/builder/exception.py

"""
Module: chess.game.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildException
from chess.game import GameContextException

__all__ = [
    # ======================# GAME_CONTEXT_BUILD_FAILURE #======================#
    "GameContextBuildException",
]


# ======================# GAME_CONTEXT_BUILD_FAILURE #======================#
class GameContextBuildException(GameContextException, BuildException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Any failed check during the GameContext build creates an exception. Failed check exceptions are encapsulated
        in an GameContextBuildException which is sent to the caller in a BuildResult.
    2.  The GameContextBuildException provides a trace for debugging and application recovery.

    # PARENT:
        *   GameContextException
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_CONTEXT_BUILD_FAILED"
    DEFAULT_MESSAGE = "GameContext build failed."