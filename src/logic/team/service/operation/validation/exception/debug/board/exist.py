# src/logic/team/service/operation/validation/exception/debug/board/register.py

"""
Module: logic.team.service.operation.validation.exception.board.register
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from logic.system import NoRelationException
from logic.team import TeamDebugException

__all__ = [
    # ======================# NO_RELATION_BETWEEN_BOARD_AND_TEAM EXCEPTION #======================#
    "TeamBelongsToDifferentBoardException",
]


# ======================# NO_RELATION_BETWEEN_BOARD_AND_TEAM EXCEPTION #======================#
class TeamBelongsToDifferentBoardException(TeamDebugException, NoRelationException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing TeamValidationResult was returned because the board and the rank team
        did not have any relationship between them.

    Super Class:
        *   TeamDebugException
        *   NoRelationException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_RELATION_BETWEEN_BOARD_AND_TEAM_EXCEPTION"
    MSG = (
        "Team validation failed: There was no relationship between the board and the rank team."
    )