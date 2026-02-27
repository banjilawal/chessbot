# src/chess/team/validator/exception/debug/board/register.py

"""
Module: chess.team.validator.exception.board.register
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.system import NoRelationException
from chess.team import TeamDebugException

__all__ = [
    # ======================# NO_RELATION_BETWEEN_BOARD_AND_TEAM EXCEPTION #======================#
    "TeamBelongsToDifferentBoardException",
]


# ======================# NO_RELATION_BETWEEN_BOARD_AND_TEAM EXCEPTION #======================#
class TeamBelongsToDifferentBoardException(TeamDebugException, NoRelationException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing TeamValidationResult was returned because the board and the candidate team
        did not have any relationship between them.

    # PARENT:
        *   TeamDebugException
        *   NoRelationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_RELATION_BETWEEN_BOARD_AND_TEAM_EXCEPTION"
    MSG = (
        "Team validation failed: There was no relationship between the board and the candidate team."
    )