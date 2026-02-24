# src/chess/team/validator/exception/debug/board/register.py

"""
Module: chess.team.validator.exception.board.register
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.team import TeamDebugException

__all__ = [
    # ======================# TEAM_SLOT_ALREADY_OCCUPIED EXCEPTION #======================#
    "TeamSlotAlreadyOccupiedException",
]


# ======================# TEAM_SLOT_ALREADY_OCCUPIED EXCEPTION #======================#
class TeamSlotAlreadyOccupiedException(TeamDebugException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing TeamValidationResult was returned because the candidate team's board slot was already occupied.

    # PARENT:
        *   TeamDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TEAM_SLOT_ALREADY_OCCUPIED_ERROR"
    DEFAULT_MESSAGE = "Team validation failed: The candidate team slot on the board was already occupied."