# src/chess/team/exception/debug.py

"""
Module: chess.team.exception.debug
Author: Banji Lawal
Created: 2026-01-26
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_DEBUG EXCEPTION #======================#
    "TeamDebugException",
]

from chess.team import TeamException
from chess.system import DebugException


# ======================# TEAM_DEBUG EXCEPTION #======================#
class TeamDebugException(TeamException, DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Team operation failure.

    # PARENT:
        *   TeamException
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
     None
    """
    ERROR_CODE = "TEAM_DEBUG_ERROR"
    DEFAULT_MESSAGE = "A team debug error occurred."