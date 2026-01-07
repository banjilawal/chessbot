# src/chess/team/roster/exception/insertion/owner.py

"""
Module: chess.team.roster.exception.insertion.owner
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from chess.team import TeamException
from chess.token import TokenException

__all__ = [
    # ======================# TOKEN_BELONGS_ON_DIFFERENT_ROSTER EXCEPTION #======================#
    "TokenBelongsOnDifferentRosterException",
]


# ======================# TOKEN_BELONGS_ON_DIFFERENT_ROSTER EXCEPTION #======================#
class TokenBelongsOnDifferentRosterException(TeamRosterException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that inserting into a Team's roster failed because it the token had a different team.

    # PARENT:
        *   TeamException
        *   TokenException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "TOKEN_BELONGS_ON_DIFFERENT_ROSTER"
    DEFAULT_MESSAGE = "Adding roster member failed: Token has a different team. It does not belong on this roster."