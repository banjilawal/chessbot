# src/logic/team/service/operation/validation/exception/debug/owner/register.py

"""
Module: logic.team.service.operation.validation.exception.owner.register
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from logic.team import TeamDebugException
from system import NotRegisteredException

__all__ = [
    # ======================# TEAM_NOT_REGISTERED_WITH_OWNER EXCEPTION #======================#
    "TeamNotRegisteredOwnerException",
]


# ======================# TEAM_NOT_REGISTERED_WITH_OWNER EXCEPTION #======================#
class TeamNotRegisteredOwnerException(TeamDebugException, NotRegisteredException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  A failing TeamValidationResult was returned because the rank team had not
        registered with its owner.

    Super Class:
        *   TeamDebugException
        *   NotRegisteredException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_NOT_REGISTERED_WITH_OWNER_EXCEPTION"
    MSG = "Team validation failed: The rank team had not registered with its owner."