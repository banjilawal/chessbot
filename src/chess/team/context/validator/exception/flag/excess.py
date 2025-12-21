# src/chess/team/context/validator/exception/flag/excess.py

"""
Module: chess.team.context.validator.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.team import InvalidTeamContextException

__all__ = [
    # ========================= EXCESSIVE_TEAM_CONTEXT_FLAGS EXCEPTION =========================#
    "ExcessiveTeamContextFlagsException"
]

# ========================= EXCESSIVE_TEAM_CONTEXT_FLAGS EXCEPTION =========================#
class ExcessiveTeamContextFlagsException(InvalidTeamContextException, ContextFlagCountException):
    """
    # ROLE: ContextFlagException, TeamContextException

    # RESPONSIBILITIES:
    1.  Indicate if more than one Team attribute is going to be used in an TeamFinder.

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
    ERROR_CODE = "EXCESSIVE_TEAM_CONTEXT_FLAGS"
    DEFAULT_MESSAGE = "More than one TeamContext flag was selected. Only one context flag is allowed."