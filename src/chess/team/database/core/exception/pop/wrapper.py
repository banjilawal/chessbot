# src/chess/team/database/core/exception/pop/wrapper.py

"""
Module: chess.team.database.core.exception.pop.wrapper
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
    1.  Wrap debug exceptions indicating why TeamStack could not delete a team. The exception chain traces the ultimate source of failure.

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
    DEFAULT_MESSAGE = "Popping TeamStack Failed."