# src/chess/team/context/validator/exception/debug/zero.py

"""
Module: chess.team.context.validator.exception.debug.zero
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.team import TeamContextException

__all__ = [
    # ========================= ZERO_TEAM_CONTEXT_FLAGS EXCEPTION =========================#
    "ZeroTeamContextFlagsException"
]


# ========================= ZERO_TEAM_CONTEXT_FLAGS EXCEPTION =========================#
class ZeroTeamContextFlagsException(TeamContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted TeamContext certification because no TeamContext flag
        was enabled.

    # PARENT:
        *   ContextFlagCountException
        *   TeamContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ZERO_TEAM_CONTEXT_FLAGS_ERROR"
    DEFAULT_MESSAGE = (
        "TeamContext validation failed: All attributes were null. One attribute should have a value."
    )