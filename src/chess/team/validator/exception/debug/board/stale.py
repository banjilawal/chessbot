# src/chess/team/validator/exception/debug/board/stale.py

"""
Module: chess.team.validator.exception.board.stale
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from chess.team import TeamDebugException
from chess.system import StaleRelationException

__all__ = [
    # ======================# BOARD_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
    "BoardHasStaleTeamLinkException",
]


#======================# BOARD_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
class BoardHasStaleTeamLinkException(TeamDebugException, StaleRelationException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

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
    ERR_CODE = "BOARD_HAS_STALE_LINK_TO_TEAM_ERROR"
    MSG = "Team validation failed: The board has a stale link to a former team."