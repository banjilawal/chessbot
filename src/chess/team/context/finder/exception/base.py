# src/chess/team/context/finder/exception/base.py

"""
Module: chess.team.context.finder.exception.base
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.system import FinderException

__all__ = [
    #======================# TEAM_FINDER EXCEPTION #======================#
    "TeamFinderException",
]


#======================# TEAM_FINDER EXCEPTION #======================#
class TeamFinderException(FinderException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by TeamFinder objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of an TeamFinder method.
  
    # PARENT:
        *   FinderException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_FINDER_ERROR"
    DEFAULT_MESSAGE = "TeamFinder raised an exception."
