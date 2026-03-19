# src/logic/team/validation/exception/debug/player/stale.py

"""
Module: logic.team.validation.exception.player.stale
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from logic.team import TeamDebugException
from logic.system import StaleRelationException

__all__ = [
    # ======================# PLAYER_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
    "PlayerHasStaleTeamLinkException",
]


#======================# PLAYER_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
class PlayerHasStaleTeamLinkException(TeamDebugException, StaleRelationException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing TeamValidationResult was returned because the player had a stale
        link to a former team.

    Super Class:
        *   TeamDebugException
        *   StaleRelationException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PLAYER_HAS_STALE_LINK_TO_TEAM_EXCEPTION"
    MSG = "Team validation failed: The player has a stale link to a former team."