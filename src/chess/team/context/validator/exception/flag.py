# src/chess/team/context/validator/exception/flag.py

"""
Module: chess.team.context.validator.exception.flag
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.team import InvalidTeamContextException

__all__ = [
    #========================= NO_TEAM_CONTEXT_FLAG EXCEPTION =========================#
    "NoTeamContextFlagException",
    #========================= TOO_MANY_TEAM_CONTEXT_FLAGS EXCEPTION =========================#
    "TooManyTeamContextFlagsException"
]


#========================= NO_TEAM_CONTEXT_FLAG EXCEPTION =========================#
class NoTeamContextFlagException(InvalidTeamContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no TeamContext flag is provided with a searcher value.
    
    # PARENT:
        *   InvalidTeamContextException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    NONE
    """
    ERROR_CODE = "NO_TEAM_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = "No TeamContext flag was selected. A context flag must be turned on with a target value."


#========================= TOO_MANY_TEAM_CONTEXT_FLAGS EXCEPTION =========================#
class TooManyTeamContextFlagsException(InvalidTeamContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, TeamContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one Team attribute is going to be used in an TeamSnapshotFinder.
    
    # PARENT:
        *   InvalidTeamContextException
        *   ContextFlagCountException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None
    
    # INHERITED ATTRIBUTES:
    NONE
    """
    ERROR_CODE = "TOO_MANY_TEAM_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "More than one TeamContext flag was selected. Only one context flag is allowed."
