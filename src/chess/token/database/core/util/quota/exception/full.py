# src/chess/token/database/core/exception/push/full/rank.py

"""
Module: chess.token.database.core.exception.push.full.rank
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

__all__ = [
    # ======================# NO_OPENINGS_FOR_RANK EXCEPTION #======================#
    "RankQuotaFullException",
]

from chess.system import DebugException
from chess.token import TokenStackException


# ======================# NO_OPENINGS_FOR_RANK EXCEPTION #======================#
class RankQuotaFullException(TokenStackException, DebugException):
    """
    # ROLE: Debug, Error Tracing

    # RESPONSIBILITIES:
    1.  Indicate that pushing a token to the stack failed because there was no openings for the token's rank.

    # PARENT:
        *   DebugException
        *   TokenServiceException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "NO_OPENINGS_FOR_RANK_ERROR"
    DEFAULT_MESSAGE = "Pushing token failed: There were no openings for the token's rank."