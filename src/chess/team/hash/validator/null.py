# src/chess/team/hash/validator/null.py

"""
Module: chess.team.hash.validator.null
Author: Banji Lawal
Created: 2025-02-08
version: 1.0.0
"""

__all__ = [
    # ======================# TEAM_HASH_NULL_EXCEPTION EXCEPTION #======================#
    "TeamHashNullException",
]

from chess.system import NullException
from chess.team import TeamHashException


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
    ERROR_CODE = "TEAM_HASH_NULL_EXCEPTION_ERROR"
    DEFAULT_MESSAGE = "TeamHash validation failed: The candidate was null."