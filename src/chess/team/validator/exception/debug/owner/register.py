# src/chess/team/validator/exception/debug/owner/register.py

"""
Module: chess.team.validator.exception.owner.register
Author: Banji Lawal
Created: 2025-11-20
version: 1.0.0
"""

from chess.team import TeamDebugException
from chess.system import NotRegisteredException

__all__ = [
    # ======================# TEAM_NOT_REGISTERED_WITH_OWNER EXCEPTION #======================#
    "TeamNotRegisteredOwnerException",
]


# ======================# TEAM_NOT_REGISTERED_WITH_OWNER EXCEPTION #======================#
class TeamNotRegisteredOwnerException(TeamDebugException, NotRegisteredException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing TeamValidationResult was returned because the candidate team had not
        registered with its owner.

    # PARENT:
        *   TeamDebugException
        *   NotRegisteredException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_NOT_REGISTERED_WITH_OWNER_EXCEPTION"
    MSG = "Team validation failed: The candidate team had not registered with its owner."