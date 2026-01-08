# src/chess/team/roster/exception/insertion/different.py

"""
Module: chess.team.roster.exception.insertion.different
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import RosterServiceException

__all__ = [
    # ======================# ENEMY_CANNOT_JOIN_ROSTER EXCEPTION #======================#
    "EnemyCannotJoinRosterException",
]


# ======================# ENEMY_CANNOT_JOIN_ROSTER EXCEPTION #======================#
class EnemyCannotJoinRosterException(RosterServiceException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that inserting into a Team's roster failed because it the token had a different team.

    # PARENT:
        *   RosterServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ENEMY_CANNOT_JOIN_ROSTER"
    DEFAULT_MESSAGE = "Adding roster member failed: The token is on an enemy team."