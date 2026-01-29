# src/chess/tea/database/core/exception/deletion/wrapper.py

"""
Module: chess.team.database.core.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_DELETION_FAILURE EXCEPTION #======================#
    "TeamDeletionFailedException",
]

from chess.system import DeletionFailedException


# ======================# TEAM_DELETION_FAILURE EXCEPTION #======================#
class TeamDeletionFailedException(DeletionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why TeamListService could not delete a team. The encapsulated
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   DeletionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_DELETION_FAILURE"
    DEFAULT_MESSAGE = "Team deletion failed."