# src/chess/game/finder/exception

"""
Module: chess.game.finder.exception
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.system import FinderException

__all__ = [
    #======================# GAME_FINDER EXCEPTIONS #======================#
    "GameFinderException",
]


#======================# GAME_FINDER EXCEPTIONS #======================#
class GameFinderException(FinderException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by GameFinder objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of an GameFinder method.
  
    # PARENT:
        *   FinderException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_FINDER_ERROR"
    DEFAULT_MESSAGE = "GameFinder raised an exception."
