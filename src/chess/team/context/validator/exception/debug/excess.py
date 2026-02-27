# src/chess/team/context/validator/exception/debug/excess.py

"""
Module: chess.team.context.validator.exception.debug.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from chess.system import ContextFlagCountException
from chess.team import TeamContextException

__all__ = [
    # ========================= ARENA_TEAM_CONTEXT_FLAGS EXCEPTION =========================#
    "ArenaTeamContextFlagsException"
]


# ========================= ARENA_TEAM_CONTEXT_FLAGS EXCEPTION =========================#
class ArenaTeamContextFlagsException(TeamContextException, ContextFlagCountException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not granted TeamContext certification because more than one TeamContext
        flag was enabled.
        
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
    ERR_CODE = "ARENA_TEAM_CONTEXT_FLAGS_EXCEPTION"
    MSG = (
        "TeamContext validation failed: More than one attribute was set. Only one attribute-value should be enabled."
    )