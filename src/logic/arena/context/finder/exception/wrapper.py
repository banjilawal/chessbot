# src/logic/arena/context/finder/exception.py

"""
Module: logic.arena.cntext.finder.exception
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from logic.arena import ArenaException
from logic.system import SearchException

__all__ = [
    #======================# ARENA_FINDER EXCEPTION #======================#
    "ArenaSearchException",
]


#======================# ARENA_FINDER EXCEPTION #======================#
class ArenaSearchException(ArenaException, SearchException):
    """
    # ROLE: Exception Wrapper
  
    # RESPONSIBILITIES:
    1.  Parent of exception raised when ArenaFinder objects.
    2.  Wraps an exception that hits the try-finally block of an ArenaFinder method.
  
    # PARENT:
        *   ArenaException
        *   FinderException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ARENA_FINDER_EXCEPTION"
    MSG = "ArenaFinder raised an exception."
