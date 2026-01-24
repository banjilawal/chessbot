# src/chess/rank/model/concrete/queen/exception/catchall.py

"""
Module: chess.rank.model.concrete.queen.exception.catchall
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import RankException

__all__ = [
    # ======================# QUEEN_ERROR EXCEPTION #======================#
    "QueenException",
]


# ======================# QUEEN_ERROR EXCEPTION #======================#
class QueenException(RankException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Queen errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "QUEEN_ERROR"
    DEFAULT_MESSAGE = "Queen raised an exception."