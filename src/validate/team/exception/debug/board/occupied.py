# src/logic/team/service/operation/validation/exception/debug/board/register.py

"""
Module: logic.team.service.operation.validation.exception.board.register
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from logic.team import TeamDebugException

__all__ = [
    # ======================# TEAM_SLOT_ALREADY_OCCUPIED EXCEPTION #======================#
    "TeamSlotAlreadyOccupiedException",
]


# ======================# TEAM_SLOT_ALREADY_OCCUPIED EXCEPTION #======================#
class TeamSlotAlreadyOccupiedException(TeamDebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing TeamValidationResult was returned because the rank team's board slot was already occupied.

    Super Class:
        *   TeamDebugException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_SLOT_ALREADY_OCCUPIED_EXCEPTION"
    MSG = "Team validation failed: The rank team slot on the board was already occupied."