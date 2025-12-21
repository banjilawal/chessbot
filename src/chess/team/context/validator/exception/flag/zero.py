# src/chess/team/context/validator/exception/flag/zero.py

"""
Module: chess.team.context.validator.exception.flag.zero
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.team import InvalidTeamContextException

__all__ = [
    # ========================= ZERO_TEAM_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroTeamContextFlagsException",
]


# ========================= ZERO_TEAM_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroTeamContextFlagsException(InvalidTeamContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate no TeamContext flag is provided with a searcher value.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidTeamContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    NONE
    """
    ERROR_CODE = "ZERO_TEAM_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = "No TeamContext flag was selected. A context flag must be turned on with a target value."