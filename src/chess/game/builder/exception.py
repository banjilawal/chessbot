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
    #======================# GAME BUILD EXCEPTION #======================#
    "GameBuildFailedException",
]


#======================# GAME BUILD EXCEPTION #======================#
class GameBuildFailedException(GameException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exception raised during Game build process.
    2.  Wraps unhandled exception that hit the try-finally block of an GameBuilder method.

    # PARENT:
        *   GameException
        *   BuildFailedException

    # PROVIDES:
    GameBuildFailedException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_BUILD_ERROR"
    DEFAULT_ERROR_CODE = "Game build failed."