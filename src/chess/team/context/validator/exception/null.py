# src/chess/team/context/number_bounds_validator/exception/flag.py

"""
Module: chess.team.context.number_bounds_validator.exception.flag
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import NullException
from chess.team import InvalidTeamContextException

__all__ = [
    #======================# TEAM_CONTEXT NULL EXCEPTION #======================#
    "NullTeamContextException",
]

#======================# TEAM_CONTEXT NULL EXCEPTION #======================#
class NullTeamContextException(InvalidTeamContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Raised if an TeamContext validation candidate is null.
    2.  Raised if an entity, method or operation requires an TeamContext but receives null instead.
    
    # PARENT:
        *   InvalidTeamContextException
        *   NullTeamContextException

    # PROVIDES:
    NullTeamContextException

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TEAM_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamContext cannot be null."
    
    
    