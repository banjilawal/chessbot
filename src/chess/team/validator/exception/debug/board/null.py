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
    "TeamHasDifferentBoardException",
]


# ======================# NO_RELATION_BETWEEN_BOARD_AND_TEAM EXCEPTION #======================#
class TeamHasDifferentBoardException(TeamDebugException, NoRelationException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

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
    ERROR_CODE = "NO_RELATION_BETWEEN_BOARD_AND_TEAM_ERROR"
    DEFAULT_MESSAGE = (
        "Team validation failed: There was no relationship between the board and the candidate team."
    )