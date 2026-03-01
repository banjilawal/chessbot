# src/logic/team/validator/exception/debug/board/stale.py

"""
Module: logic.team.validator.exception.board.stale
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from logic.team import TeamDebugException
from logic.system import StaleRelationException

__all__ = [
    # ======================# BOARD_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
    "BoardHasStaleTeamLinkException",
]


#======================# BOARD_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
class BoardHasStaleTeamLinkException(TeamDebugException, StaleRelationException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing TeamValidationResult was returned because the board had a stale
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
    ERR_CODE = "BOARD_HAS_STALE_LINK_TO_TEAM_EXCEPTION"
    MSG = "Team validation failed: The board has a stale link to a former team."