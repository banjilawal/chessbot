# src/chess/team/validator/exception/debug/owner/stale.py

"""
Module: chess.team.validator.exception.owner.stale
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

from chess.team import TeamDebugException
from chess.system import StaleRelationException

__all__ = [
    # ======================# OWNER_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
    "OwnerHasStaleTeamLinkException",
]


#======================# OWNER_HAS_STALE_LINK_TO_TEAM EXCEPTION #======================#
class OwnerHasStaleTeamLinkException(TeamDebugException, StaleRelationException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging

    # RESPONSIBILITIES:
    1.  A failing TeamValidationResult was returned because the owner had a stale
        link to a former team.

    # PARENT:
        *   TeamDebugException
        *   StaleRelationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "OWNER_HAS_STALE_LINK_TO_TEAM_ERROR"
    DEFAULT_MESSAGE = "Team validation failed: The owner has a stale link to a former team."