# src/chess/team/database/core/exception/insertion/duplicate.py

"""
Module: chess.team.database.core.exception.insertion.duplicate
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from chess.team import TeamStackServiceException

__all__ = [
    # ======================# ADDING_DUPLICATE_TEAM EXCEPTION #======================#
    "AddingDuplicateTeamException",
]


# ======================# ADDING_DUPLICATE_TEAM EXCEPTION #======================#
class AddingDuplicateTeamException(TeamStackServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a team to teh stack failed because it was already present.

    # PARENT:
        *   TeamStackServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_TEAM_ERROR"
    DEFAULT_MESSAGE = "Pushing team onto stack failed: The team is already present."