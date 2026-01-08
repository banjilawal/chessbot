# src/chess/team/roster/exception/insertion/captured.py

"""
Module: chess.team.roster.exception.insertion.captured
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""


__all__ = [
    # ======================# DELETING_ACTIVE_TOKEN_FROM_ROSTER EXCEPTION #======================#
    "DeletingActiveTokenException",
]

from chess.team import RosterServiceException


# ======================# DELETING_ACTIVE_TOKEN_FROM_ROSTER EXCEPTION #======================#
class DeletingActiveTokenException(RosterServiceException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a token cannot be removed from the roster because it has not been captured.

    # PARENT:
        *   RosterServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DELETING_ACTIVE_TOKEN_FROM_ROSTER_ERROR"
    DEFAULT_MESSAGE = "Roster member deletion failed: An active token cannot be removed from roster."