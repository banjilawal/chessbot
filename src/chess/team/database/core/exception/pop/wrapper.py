# src/chess/team/database/core/exception/deletion/wrapper.py

"""
Module: chess.team.database.core.exception.deletion.wrapper
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

__all__ = [
    # ======================# POPPING_TEAM_STACK_FAILURE EXCEPTION #======================#
    "PoppingTeamStackFailedException",
]

from chess.team import TeamStackException
from chess.system import DeletionFailedException


# ======================# POPPING_TEAM_STACK_FAILURE EXCEPTION #======================#
class PoppingTeamStackFailedException(TeamStackException, DeletionFailedException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Wrap debug exceptions that indicate why TeamStack could not delete a team. The encapsulated
        exceptions create a chain for tracing the source of the failure.

    # PARENT:
        *   TeamStackException
        *   DeletionFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "POPPING_TEAM_STACK_FAILURE"
    DEFAULT_MESSAGE = "Team deletion failed."