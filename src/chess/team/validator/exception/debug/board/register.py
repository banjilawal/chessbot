# src/chess/team/validator/exception/debug/board/register.py

"""
Module: chess.team.validator.exception.board.register
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.team import TeamDebugException
from chess.system import NotRegisteredException

__all__ = [
    # ======================# TEAM_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
    "TeamNotRegisteredBoardException",
]


# ======================# TEAM_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
class TeamNotRegisteredBoardException(TeamDebugException, NotRegisteredException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing TeamValidationResult was returned because the candidate team had not
        registered with its board.

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
    ERR_CODE = "TEAM_NOT_REGISTERED_WITH_BOARD_ERROR"
    MSG = "Team validation failed: The candidate team had not registered with its board."