# src/chess/team/validator/exception/debug/owner/register.py

"""
Module: chess.team.validator.exception.owner.register
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""
from chess.system import NoRelationException
from chess.team import TeamDebugException

__all__ = [
    # ======================# NO_RELATION_BETWEEN_PLAYER_AND_TEAM EXCEPTION #======================#
    "TeamHasDifferentOwnerException",
]


# ======================# NO_RELATION_BETWEEN_PLAYER_AND_TEAM EXCEPTION #======================#
class TeamHasDifferentOwnerException(TeamDebugException, NoRelationException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing TeamValidationResult was returned because the player and the candidate team
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
    ERR_CODE = "NO_RELATION_BETWEEN_PLAYER_AND_TEAM_ERROR"
    MSG = (
        "Team validation failed: There was no relationship between the player and the candidate team."
    )