# src/logic/team/database/kernel/exception/insertion/work.py

"""
Module: logic.team.database.kernel.exception.insertion.work
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_INSERTION_FAILURE #======================#
    "TeamInsertionException",
]

from logic.system import InsertionException


# ======================# TEAM_INSERTION_FAILURE #======================#
class TeamInsertionException(InsertionException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why TeamStack could not delete a team. The exception chain traces the ultimate source of failure.

    Super Class:
        *   InsertionException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_INSERTION_FAILURE"
    MSG = "Team insertion failed."