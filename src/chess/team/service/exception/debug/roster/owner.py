# src/chess/team/service/exception/token.py

"""
Module: chess.team.service.exception.token
Author: Banji Lawal
Created: 2025-11-24
version: 1.0.0
"""

from chess.team import TeamException
from chess.token import TokenException

__all__ = [
    # ======================# TOKEN_BELONGS_ON_DIFFERENT_ROSTER EXCEPTION #======================#
    "TokenBelongsOnDifferentRosterException",
]


# ======================# TOKEN_BELONGS_ON_DIFFERENT_ROSTER EXCEPTION #======================#
class TokenBelongsOnDifferentRosterException(TeamException, TokenException):
    """
    # ROLE: Exception Wrapper, Catchall Exception

    # RESPONSIBILITIES:
    1.  Indicate that insterting into a Team's roster failed because it the token had a different team.

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
    DEFAULT_MESSAGE = "Roster insertion failed: Token has a different team. It does not belong on this roster."