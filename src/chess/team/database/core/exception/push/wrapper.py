# src/chess/team/database/core/exception/insertion/wrapper.py

"""
Module: chess.team.database.core.exception.insertion.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_INSERTION_FAILURE #======================#
    "PushingTeamFailedException",
]

from chess.team import TeamStackException
from chess.system import InsertionFailedException


# ======================# TEAM_INSERTION_FAILURE #======================#
class PushingTeamFailedException(TeamStackException, InsertionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that pushing a Team on the Stack failed.

    # PARENT:
        *   TeamStackException
        *   InsertionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_INSERTION_FAILURE_ERROR"
    DEFAULT_MESSAGE = "Team insertion failed."