# src/logic/team/database/kernel/exception/push/duplicate.py

"""
Module: logic.team.database.kernel.exception.push.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from logic.team import TeamStackException

__all__ = [
    # ======================# ADDING_DUPLICATE_TEAM EXCEPTION #======================#
    "AddingDuplicateTeamException",
]


# ======================# ADDING_DUPLICATE_TEAM EXCEPTION #======================#
class AddingDuplicateTeamException(TeamStackException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to add a team to teh schema failed because it was already present.

    Super Class:
        *   TeamStackException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "ADDING_DUPLICATE_TEAM_EXCEPTION"
    MSG = "Pushing team onto schema failed: The team is already present."