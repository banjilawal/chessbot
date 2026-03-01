# src/logic/team/database/core/exception/push/wrapper.py

"""
Module: logic.team.database.core.exception.push.wrapper
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_PUSH_FAILURE #======================#
    "PushingTeamFailedException",
]

from logic.team import TeamStackException
from logic.system import InsertionException


# ======================# TEAM_PUSH_FAILURE #======================#
class PushingTeamFailedException(TeamStackException, InsertionException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that pushing a Team on the Stack failed.

    # PARENT:
        *   TeamStackException
        *   InsertionException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_PUSH_FAILURE"
    MSG = "Team push failed."