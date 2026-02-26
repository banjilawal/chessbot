# src/chess/rank/model/concrete/queen/exception/super.py

"""
Module: chess.rank.model.concrete.queen.exception.super
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
    # ROLE: Super Exception

    # RESPONSIBILITIES:
    1.  Super for Queen errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "QUEEN_ERROR"
    MSG = "Queen raised an exception."