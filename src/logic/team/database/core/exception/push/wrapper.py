# src/logic/team/database/core/exception/push/worker.py

"""
Module: logic.team.database.core.exception.push.work
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
    Role:Exception Work

    Responsibilities:
    1.  Indicate that pushing a Team on the Stack failed.

    Super Class:
        *   TeamStackException
        *   InsertionException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_PUSH_FAILURE"
    MSG = "Team push failed."