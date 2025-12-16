# src/chess/team/context/service/exception/base

"""
Module: chess.team.context.service.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    #======================# TEAM_CONTEXT_SERVICE EXCEPTION #======================#
    "TeamContextServiceException",
]


#======================# TEAM_CONTEXT_SERVICE EXCEPTION #======================#
class TeamContextServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
    
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when an TeamContextService's normal operations are halted
        by an error condition.
    2.  Raised when no specific exception exists for the error interrupting TeamContextService's
        processes from their normal flows.
        
    # PARENT:
        *   ServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TeamContextService raised an exception."