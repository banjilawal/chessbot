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
    "ZeroTeamContextFlagsException"
]


# ========================= ZERO_TEAM_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroTeamContextFlagsException(InvalidTeamContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicates no TeamContext flag was enabled. One and only one Team attribute-value-tuple is required for
        a search.

    # PARENT:
        *   ContextFlagCountException
        *   InvalidTeamContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_TEAM_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "Zero TeamContext flags were set. Cannot search for Teams if one-and_oly-one "
        "context flag is enabled."
    )