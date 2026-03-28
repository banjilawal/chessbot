# src/logic/team/database/kernel/exception/query/exist.py

"""
Module: logic.team.database.kernel.exception.query.exist
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""



__all__ = [
    # ======================# TEAM_NOT_FOUND EXCEPTION #======================#
    "TeamNotFoundException",
]

from logic.team import TeamDebugException


# ======================# TEAM_NOT_FOUND EXCEPTION #======================#
class TeamNotFoundException(TeamDebugException):
    """
    Role:Debug, Error Tracing

    Responsibilities:
    1.  Indicate that an attempt to remove instances of a item by a unique attribute failed because no bag
        matching the property were found in the collider_candidates.

    Super Class:
        *   NullException
        *   TeamStackException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_NOT_FOUND_EXCEPTION"
    MSG = "Team deletion failed: The item was not found in the collider_candidates. Nothing to remove."