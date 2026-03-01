# src/logic/team/context/finder/exception/wrapper.py

"""
Module: logic.team.context.finder.exception.wrapper
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""


__all__ = [
    #======================# TEAM_SEARCH_FAILURE #======================#
    "TeamSearchException",
]

from logic.system import SearchException
from logic.team import TeamException


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
    ERR_CODE = "TEAM_SEARCH_FAILURE"
    MSG = "TeamSearch failed."
