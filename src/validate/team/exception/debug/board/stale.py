# src/logic/team/service/operation/validation/exception/debug/board/stale.py

"""
Module: logic.team.service.operation.validation.exception.board.stale
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from logic.team import TeamDebugException
from system import StaleRelationException

__all__ = [
    # ======================# BOARD_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
    "BoardHasStaleTeamLinkException",
]


#======================# BOARD_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
class BoardHasStaleTeamLinkException(TeamDebugException, StaleRelationException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing TeamValidationResult was returned because the board had a stale
        link to a former team.

    Super Class:
        *   TeamDebugException
        *   StaleRelationException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BOARD_HAS_STALE_LINK_TO_TEAM_EXCEPTION"
    MSG = "Team validation failed: The board has a stale link to a former team."