# src/logic/team/validator/exception/debug/owner/register.py

"""
Module: logic.team.validator.exception.owner.register
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""
from logic.system import NoRelationException
from logic.team import TeamDebugException

__all__ = [
    # ======================# NO_RELATION_BETWEEN_PLAYER_AND_TEAM EXCEPTION #======================#
    "TeamHasDifferentOwnerException",
]


# ======================# NO_RELATION_BETWEEN_PLAYER_AND_TEAM EXCEPTION #======================#
class TeamHasDifferentOwnerException(TeamDebugException, NoRelationException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

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
    ERR_CODE = "NO_RELATION_BETWEEN_PLAYER_AND_TEAM_EXCEPTION"
    MSG = (
        "Team validation failed: There was no relationship between the player and the candidate team."
    )