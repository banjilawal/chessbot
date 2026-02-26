# src/chess/rank/model/concrete/king/exception/super.py

"""
Module: chess.rank.model.concrete.king.exception.super
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
    # ROLE: Super Exception

    # RESPONSIBILITIES:
    1.  Super for King errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "KING_ERROR"
    MSG = "King raised an exception."