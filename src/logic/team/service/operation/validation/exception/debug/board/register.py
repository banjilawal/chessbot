# src/logic/team/service/operation/validation/exception/debug/board/register.py

"""
Module: logic.team.service.operation.validation.exception.board.register
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from logic.team import TeamDebugException
from logic.system import NotRegisteredException

__all__ = [
    # ======================# TEAM_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
    "TeamNotRegisteredBoardException",
]


# ======================# TEAM_NOT_REGISTERED_WITH_BOARD EXCEPTION #======================#
class TeamNotRegisteredBoardException(TeamDebugException, NotRegisteredException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing TeamValidationResult was returned because the candidate team had not
        registered with its board.

    Super Class:
        *   TeamDebugException
        *   NotRegisteredException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_NOT_REGISTERED_WITH_BOARD_EXCEPTION"
    MSG = "Team validation failed: The candidate team had not registered with its board."