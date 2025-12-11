# src/chess/team/schema/context/service/exception/base

"""
Module: chess.team.schema.context.service.exception.base
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ServiceException

__all__ = [
    #======================# GAME_CONTEXT_SERVICE EXCEPTION #======================#
    "GameContextServiceException",
]


#======================# GAME_CONTEXT_SERVICE EXCEPTION #======================#
class GameContextServiceException(ServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception
    
    # RESPONSIBILITIES:
    1.  Parent of exceptions raised when an GameContextService's normal operations are halted
        by an error condition.
    2.  Raised when no specific exception exists for the error interrupting GameContextService's
        processes from their normal flows.
        
    # PARENT:
        *   ServiceException

    # PROVIDES:
    GameContextServiceException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "GAME_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "GameContextService raised an exception."