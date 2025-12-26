# src/chess/team/finder/exception/wrapper.py

"""
Module: chess.team.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


__all__ = [
    #======================# TEAM_SEARCH_FAILURE EXCEPTION #======================#
    "TeamSearchFailedException",
]

from chess.system import SearchFailedException
from chess.team import TeamException


#======================# TEAM_SEARCH_FAILURE EXCEPTION #======================#
class TeamSearchFailedException(TeamException, SearchFailedException):
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
    ERROR_CODE = "TEAM_SEARCH_FAILURE_ERROR"
    DEFAULT_MESSAGE = "TeamSearch failed."
