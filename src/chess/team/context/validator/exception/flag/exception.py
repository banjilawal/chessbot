# src/chess/team/context/validator/exception/flag/exception.py

"""
Module: chess.team.context.validator.exception.flag.exception
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from chess.system import BoundsException
from chess.team import InvalidTeamContextException

__all__ = [
    # ========================= TEAM_CONTEXT FLAG EXCEPTIONS =========================#
    "NoTeamContextFlagSetException",
    "TooManyTeamContextFlagsSetException"
]


# ========================= TEAM_CONTEXT FLAG EXCEPTIONS =========================#
class NoTeamContextFlagSetException(InvalidTeamContextException, BoundsException):
    """Raised if no TeamContext was selected."""
    ERROR_CODE = "NO_TEAM_CONTEXT_FLAG_SET_ERROR"
    DEFAULT_MESSAGE = "One and only one, TeamContext flag must be set."


class TooManyTeamContextFlagsSetException(InvalidTeamContextException, BoundsException):
    """Raised if too many TeamContext flags were set."""
    ERROR_CODE = "TEAM_CONTEXT_MAX_PARAM_ERROR"
    DEFAULT_MESSAGE = "Only one TeamContext flag can be set."