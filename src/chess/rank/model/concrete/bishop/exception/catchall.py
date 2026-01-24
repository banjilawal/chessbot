# src/chess/rank/model/concrete/bishop/exception.py

"""
Module: chess.rank.model.concrete.bishop.exception
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
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Bishop errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "BISHOP_ERROR"
    DEFAULT_MESSAGE = "Bishop raised an exception."