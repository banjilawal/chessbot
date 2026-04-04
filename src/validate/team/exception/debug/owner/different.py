# src/logic/team/service/operation/validation/exception/debug/owner/register.py

"""
Module: logic.team.service.operation.validation.exception.owner.register
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""
from system import NoRelationException
from logic.team import TeamDebugException

__all__ = [
    # ======================# NO_RELATION_BETWEEN_PLAYER_AND_TEAM EXCEPTION #======================#
    "TeamHasDifferentOwnerException",
]


# ======================# NO_RELATION_BETWEEN_PLAYER_AND_TEAM EXCEPTION #======================#
class TeamHasDifferentOwnerException(NoRelationException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing TeamValidationResult was returned because the player and the rank team
        did not have any relationship between them.

    Super Class:
        *   NoRelationException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "NO_RELATION_BETWEEN_PLAYER_AND_TEAM_EXCEPTION"
    MSG = (
        "Team validation failed: There was no relationship between the player and the rank team."
    )