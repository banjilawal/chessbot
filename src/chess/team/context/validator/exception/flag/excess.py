# src/chess/team/validator/exception/flag/excess.py

"""
Module: chess.team.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.team import InvalidTeamContextException

__all__ = [
    # ========================= EXCESSIVE_TEAM_CONTEXT_FLAG EXCEPTION =========================#
    "ExcessiveTeamContextFlagsException"
]


# ========================= EXCESSIVE_TEAM_CONTEXT_FLAG EXCEPTION =========================#
class ExcessiveTeamContextFlagsException(InvalidTeamContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate That  more than one TeamContext flag was enabled. Only one Team attribute-value-tuple can be used in
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
    ERROR_CODE = "EXCESSIVE_TEAM_CONTEXT_FLAG_ERROR"
    DEFAULT_MESSAGE = (
        "Excessive TeamContext flags were set. an Team search can only use one-and-only "
        "map flag at a time."
    )