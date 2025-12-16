# src/chess/team/context/service/exception/invalid.py

"""
Module: chess.team.context.service.exception.invalid
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ValidationFailedException
from chess.team import TeamContextServiceException


__all__ = [
    #======================# TEAM_CONTEXT_SERVICE VALIDATION EXCEPTIONS #======================#
    "InvalidTeamContextServiceException",
]


#======================# TEAM_CONTEXT_SERVICE VALIDATION EXCEPTIONS #======================#
class InvalidTeamContextServiceException(TeamContextServiceException, ValidationFailedException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Parent of exceptions raised during TeamContextService verification process.
    2.  Wraps unhandled exceptions that hit the try-finally block of an TeamContextServiceValidator method.
    
    # PARENT:
        *   TeamContextServiceException
        *   ValidationFailedException

    # PROVIDES:
    InvalidTeamContextServiceException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_CONTEXT_SERVICE_VALIDATION_ERROR"
    DEFAULT_MESSAGE = "TeamContextService validation failed."