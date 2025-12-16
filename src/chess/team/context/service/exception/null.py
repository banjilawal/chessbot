# src/chess/team/context/service/exception/null.py

"""
Module: chess.team.context.service.exception.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.team import InvalidTeamContextServiceException

__all__ = [
    #======================# NULL TEAM_CONTEXT_SERVICE EXCEPTIONS #======================#
    "NullTeamContextServiceException",
]


#======================# NULL TEAM_CONTEXT_SERVICE EXCEPTION #======================#
class NullTeamContextServiceException(InvalidTeamContextServiceException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate if an entity, method or operation required an TeamContextService but got null instead.
    
    # PARENT:
        *   InvalidTeamContextServiceException
        *   NullException

    # PROVIDES:
    NullTeamContextServiceException

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TEAM_CONTEXT_SERVICE_ERROR"
    DEFAULT_MESSAGE = "TeamContextService cannot be null."