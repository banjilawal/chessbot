# src/chess/team/validator/exception/flag/zero.py

"""
Module: chess.team.validator.exception.flag.zero
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
        "TeamContext validation failed: The candidate had more than one attribute set. Cannot search for teams if "
        "without one and only attribute-value tuple enabled."
    )