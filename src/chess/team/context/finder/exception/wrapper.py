# src/chess/team/context/finder/exception/wrapper.py

"""
Module: chess.team.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


__all__ = [
    #======================# TEAM_SEARCH_FAILURE #======================#
    "TeamSearchException",
]

from chess.system import SearchException
from chess.team import TeamException


#======================# TEAM_SEARCH_FAILURE #======================#
class TeamSearchException(TeamException, SearchException):
    """
    # ROLE: Exception Wrapper
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by TeamFinder objects.
    2.  Wrap an exception that hits the try-finally block of an TeamFinder method.
  
    # PARENT:
        *   FinderException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SEARCH_FAILURE"
    DEFAULT_MESSAGE = "TeamSearch failed."
