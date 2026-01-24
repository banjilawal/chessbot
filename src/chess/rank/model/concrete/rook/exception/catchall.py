# src/chess/rank/model/concrete/rook/exception.py

"""
Module: chess.rank.model.concrete.rook.exception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import RankException

__all__ = [
    # ======================# ROOK_ERROR EXCEPTION #======================#
    "RookException",
]


# ======================# ROOK_ERROR EXCEPTION #======================#
class RookException(RankException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Rook errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "ROOK_ERROR"
    DEFAULT_MESSAGE = "Rook raised an exception."