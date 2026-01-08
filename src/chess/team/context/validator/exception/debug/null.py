# src/chess/team/context/validator/exception/debug/null.py

"""
Module: chess.team.context.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""


__all__ = [
    # ======================# NULL_TEAM_CONTEXT EXCEPTION #======================#
    "NullTeamContextException",
]

from chess.system import NullException
from chess.team import TeamContextException


# ======================# NULL_TEAM_CONTEXT EXCEPTION #======================#
class NullTeamContextException(TeamContextException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted TeamContext certification because it was null.

    # PARENT:
        *   NullTeamContextException
        *   TeamContextException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NULL_TEAM_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamContext validation failed: The candidate was null."