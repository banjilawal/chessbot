# src/chess/team/context/exception.py

"""
Module: chess.team.context.exception
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.team import TeamException
from chess.system import ContextException

__all__ = [
    # ======================# TEAM_CONTEXT EXCEPTION #======================#
    "TeamContextException",
]

# ======================# TEAM_CONTEXT EXCEPTION #======================#
class TeamContextException(TeamException, ContextException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for TeamContext errors not covered by TeamException subclasses.

    # PARENT:
        *   TeamException
        *   ContextException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_CONTEXT_ERROR"
    DEFAULT_MESSAGE = "TeamContext raised an exception."