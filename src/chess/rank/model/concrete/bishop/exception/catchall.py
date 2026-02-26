# src/chess/rank/model/concrete/bishop/exception/super.py

"""
Module: chess.rank.model.concrete.bishop.exception.super
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import RankException

__all__ = [
    # ======================# BISHOP_ERROR EXCEPTION #======================#
    "BishopException",
]


# ======================# BISHOP_ERROR EXCEPTION #======================#
class BishopException(RankException):
    """
    # ROLE: Super Exception

    # RESPONSIBILITIES:
    1.  Super for Bishop errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "BISHOP_ERROR"
    MSG = "Bishop raised an exception."