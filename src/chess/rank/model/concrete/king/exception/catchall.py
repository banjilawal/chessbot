# src/chess/rank/model/concrete/king/exception/catchall.py

"""
Module: chess.rank.model.concrete.king.exception.catchall
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import RankException

__all__ = [
    # ======================# KING_ERROR EXCEPTION #======================#
    "KingException",
]


# ======================# KING_ERROR EXCEPTION #======================#
class KingException(RankException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for King errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "KING_ERROR"
    DEFAULT_MESSAGE = "King raised an exception."