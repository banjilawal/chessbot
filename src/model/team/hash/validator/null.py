# src/logic/team/hash/validation/null.py

"""
Module: logic.team.hash.validation.null
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
    Role:Error Tracing, Debugging

    Responsibilities:
    1.  Indicate that the rank was not validated as a TeamHash because it was null.

    Super Class:
        *   NullException
        *   TeamHashException

    Provides:


    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "TEAM_HASH_NULL_EXCEPTION_EXCEPTION"
    MSG = "TeamHash validation failed: The rank was null."