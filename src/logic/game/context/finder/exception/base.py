# src/logic/game/finder/exception/base.pb

"""
Module: logic.game.finder.exception.base
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from logic.system import FinderException

__all__ = [
    #======================# GAME_FINDER EXCEPTION #======================#
    "GameFinderException",
]


#======================# GAME_FINDER EXCEPTION #======================#
class GameFinderException(FinderException):
    """
    # ROLE: Exception Wrapper
  
    # RESPONSIBILITIES:
    1.  Parent of exception raised by GameFinder objects.
    2.  Wraps an exception that hits the try-finally block of an GameFinder method.
  
    # PARENT:
        *   FinderException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "GAME_FINDER_EXCEPTION"
    MSG = "GameFinder raised an exception."
