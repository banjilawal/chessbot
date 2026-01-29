# src/chess/team/database/exception/duplicate.py

"""
Module: chess.team.database.exception.duplicate
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from chess.team import UniqueTeamDataServiceException

__all__ = [
    # ======================# ADDING_DUPLICATE_TEAM EXCEPTION #======================#
    "AddingDuplicateTeamException",
]


# ======================# ADDING_DUPLICATE_TEAM EXCEPTION #======================#
class AddingDuplicateTeamException(UniqueTeamDataServiceException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that an attempt to add a team to the TeamDatabase's dataset failed because the team was
        already in the collection

    # PARENT:
        *   TeamDatabaseException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ADDING_DUPLICATE_TEAM_ERROR"
    DEFAULT_MESSAGE = (
        "Team insertion failed: TeamDatabase is already managing the team. It cannot be added to the "
        "dataset again."
    )