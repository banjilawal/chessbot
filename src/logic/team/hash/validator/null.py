# src/logic/team/hash/validator/null.py

"""
Module: logic.team.hash.validator.null
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_HASH_NULL_EXCEPTION EXCEPTION #======================#
    "TeamHashNullException",
]

from logic.system import NullException
from logic.team import TeamHashException


# ======================# TEAM_HASH_NULL_EXCEPTION EXCEPTION #======================#
class TeamHashNullException(TeamHashException, NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that the candidate was not validated as a TeamHash because it was null.

    # PARENT:
        *   NullException
        *   TeamHashException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_HASH_NULL_EXCEPTION_EXCEPTION"
    MSG = "TeamHash validation failed: The candidate was null."