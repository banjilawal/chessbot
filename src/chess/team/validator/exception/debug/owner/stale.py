# src/chess/team/validator/exception/debug/owner/stale.py

"""
Module: chess.team.validator.exception.owner.stale
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.team import TeamDebugException
from chess.system import NotRegisteredException


__all__ = [
    # ======================# PLAYER_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
    "PlayerHasStaleTeamLinkException",
]


#======================# PLAYER_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
class PlayerHasStaleTeamLinkException(TeamDebugException, NotRegisteredException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing ValidationResult was returned because the player had a stale link to a team.

    # PARENT:
        *   TeamDebugException
        *   NotRegisteredException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PLAYER_HAS_STALE_LINK_TO_TEAM_ERROR"
    DEFAULT_MESSAGE = "Team validation failed: The candidate team had not registered with its owner."