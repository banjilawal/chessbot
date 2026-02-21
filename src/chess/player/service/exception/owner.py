# src/chess/owner/service/exception/different.py

"""
Module: chess.owner.service.exception.different
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

___all__ = [
    # ======================# TEAM_BELONGS_TO_DIFFERENT_OWNER EXCEPTION #======================#
    "TeamBelongsToDifferentOwnerException",
]

from chess.team import TeamException
from chess.player import PlayerException



# ======================# TEAM_BELONGS_TO_DIFFERENT_OWNER EXCEPTION #======================#
class TeamBelongsToDifferentOwnerException(PlayerException, TeamException):
    """
    # ROLE: Exception Wrapper

    # RESPONSIBILITIES:
    1.  Indicate that a team belongs to a different owner.

    # PARENT:
        *   AgentException
        *   TeamException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_BELONGS_TO_DIFFERENT_OWNER"
    DEFAULT_MESSAGE = "Team belongs to a different owner."