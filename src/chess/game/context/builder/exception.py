# src/chess/game/context/builder/exception.py

"""
Module: chess.game.context.builder.exception
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import BuildFailedException
from chess.game import GameContextException


__all__ = [
    #======================# GAME_CONTEXT BUILD EXCEPTIONS #======================#
    "GameContextBuildFailedException",
]


#======================# GAME_CONTEXT BUILD EXCEPTIONS #======================#
class GameContextBuildFailedException(GameContextException, BuildFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during GameContext build process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an GameContextBuilder method.
    
    # PARENT
        *   GameContextException
        *   BuildFailedException

    # PROVIDES:
    GameContextBuildFailedException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_CONTEXT_BUILD_ERROR"
    DEFAULT_MESSAGE = "Game build failed."