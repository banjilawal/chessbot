# src/logic/team/database/kernel/exception/pop/work.py

"""
Module: logic.team.database.kernel.exception.pop.work
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

__all__ = [
    # ======================# POPPING_TEAM_STACK_FAILURE #======================#
    "PoppingTeamStackFailedException",
]

from logic.team import TeamStackException
from logic.system import DeletionException


# ======================# POPPING_TEAM_STACK_FAILURE #======================#
class PoppingTeamStackFailedException(TeamStackException, DeletionException):
    """
    Role:Exception Work

    Responsibilities:
    1.  Wrap debug exceptions indicating why TeamStack could not delete a team. The exception chain traces the ultimate source of failure.

    Super Class:
        *   TeamStackException
        *   DeletionException

    Provides:


    INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "POPPING_TEAM_STACK_FAILURE"
    MSG = "Popping TeamStack Failed."