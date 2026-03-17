# src/logic/player/service/exception/different.py

"""
Module: logic.player.service.exception.different
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

___all__ = [
    # ======================# TEAM_BELONGS_TO_DIFFERENT_OWNER EXCEPTION #======================#
    "TeamBelongsToDifferentOwnerException",
]

from logic.team import TeamException
from logic.player import PlayerException



# ======================# TEAM_BELONGS_TO_DIFFERENT_OWNER EXCEPTION #======================#
class TeamBelongsToDifferentOwnerException(PlayerException, TeamException):
    """
    Role:Exception Wrapper

    Responsibilities:
    1.  Indicate that a team belongs to a different owner.

    Super Class:
        *   AgentException
        *   TeamException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_BELONGS_TO_DIFFERENT_OWNER"
    MSG = "Team belongs to a different owner."