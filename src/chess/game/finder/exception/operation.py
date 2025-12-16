# src/chess/game/finder/exception

"""
Module: chess.game.finder.exception
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.game.finder import GameFinderException
from chess.system import OperationFailedException

__all__ = [
    #======================# GAME_FINDER_OPERATION_FAILED EXCEPTION #======================#
    "GameFinderOperationFailedException",
]


# ======================# GAME_FINDER_OPERATION_FAILED EXCEPTION #======================#
class GameFinderOperationFailedException(GameFinderException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by GameFinderOperationFailed objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of an GameFinderOperationFailed method.
  
    # PARENT:
        *   FinderException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_FINDER_OPERATION_ERROR"
    DEFAULT_MESSAGE = "GameFinder operation failed."
