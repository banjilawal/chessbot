# src/chess/team/database/core/exception/query/exist.py

"""
Module: chess.team.database.core.exception.query.exist
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""



__all__ = [
    # ======================# TEAM_NOT_FOUND EXCEPTION #======================#
    "TeamNotFoundException",
]

from chess.team import TeamDebugException


# ======================# TEAM_NOT_FOUND EXCEPTION #======================#
class TeamNotFoundException(TeamDebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to remove instances of a item by a unique attribute failed because no bag
        matching the property were found in the dataset.

    # PARENT:
        *   NullException
        *   TeamStackException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_NOT_FOUND_ERROR"
    DEFAULT_MESSAGE = "Team deletion failed: The item was not found in the dataset. Nothing to remove."