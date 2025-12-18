# src/chess/team/context/finder/exception/operation.py

"""
Module: chess.team.context.finder.exception.operation
Author: Banji Lawal
Created: 2025-11-17
version: 1.0.0
"""

from chess.team import TeamFinderException
from chess.system import OperationFailedException

__all__ = [
    #======================# TEAM_FINDER_OPERATION_FAILED EXCEPTION #======================#
    "TeamFinderOperationFailedException",
]


# ======================# TEAM_FINDER_OPERATION_FAILED EXCEPTION #======================#
class TeamFinderOperationFailedException(TeamFinderException, OperationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
  
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised by TeamFinderOperationFailed objects.
    2.  Wraps unhandled exceptions that hit the try-finally block of an TeamFinderOperationFailed method.
  
    # PARENT:
        *   FinderException
  
    # PROVIDES:
    None
  
    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_FINDER_OPERATION_ERROR"
    DEFAULT_MESSAGE = "TeamFinder operation failed."
