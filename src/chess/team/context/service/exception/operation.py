# src/chess/team/context/service/exception/operation.py

"""
Module: chess.team.context.service.exception.operation
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import OperationFailedException
from chess.team import TeamContextServiceException

__all__ = [
    #======================# OPERATION TEAM_CONTEXT_SERVICE EXCEPTIONS #======================#
    "TeamContextServiceOperationFailedException",
]


# ======================# TEAM_CONTEXT_SERVICE OPERATION EXCEPTION #======================#
class TeamContextServiceOperationFailedException(TeamContextServiceException, OperationFailedException):
    """
    # ROLE: Error Tracing, Debugging, Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicates a ameContextService method that returns a Result object caught an unhandled exception 
        in its try-catch-finally block.

    # PARENT:
        *   TeamContextServiceException
        *   OperationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_CONTEXT_SERVICE_OPERATION_ERROR"
    DEFAULT_MESSAGE = "TeamContextService operation failed."