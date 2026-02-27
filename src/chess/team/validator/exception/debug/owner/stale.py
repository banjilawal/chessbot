# src/chess/team/validator/exception/debug/player/stale.py

"""
Module: chess.team.validator.exception.player.stale
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from chess.team import TeamDebugException
from chess.system import StaleRelationException

__all__ = [
    # ======================# PLAYER_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
    "PlayerHasStaleTeamLinkException",
]


#======================# PLAYER_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
class PlayerHasStaleTeamLinkException(TeamDebugException, StaleRelationException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing TeamValidationResult was returned because the player had a stale
        link to a former team.

    # PARENT:
        *   TeamDebugException
        *   StaleRelationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "PLAYER_HAS_STALE_LINK_TO_TEAM_EXCEPTION"
    MSG = "Team validation failed: The player has a stale link to a former team."