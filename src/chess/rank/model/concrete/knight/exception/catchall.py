# src/chess/rank/model/concrete/knight/exception.py

"""
Module: chess.rank.model.concrete.knight.exception
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
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Knight errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "KNIGHT_ERROR"
    DEFAULT_MESSAGE = "Knight raised an exception."