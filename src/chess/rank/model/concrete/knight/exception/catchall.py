# src/chess/rank/model/concrete/knight/exception/super.py

"""
Module: chess.rank.model.concrete.knight.exception.super
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import RankException

__all__ = [
    # ======================# KNIGHT_ERROR EXCEPTION #======================#
    "KnightException",
]


# ======================# KNIGHT_ERROR EXCEPTION #======================#
class KnightException(RankException):
    """
    # ROLE: Super Exception

    # RESPONSIBILITIES:
    1.  Super for Knight errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "KNIGHT_ERROR"
    MSG = "Knight raised an exception."