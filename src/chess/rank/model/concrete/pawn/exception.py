# src/chess/rank/model/concrete/pawn/exception.py

"""
Module: chess.rank.model.concrete.pawn.exception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import RankException

__all__ = [
    # ======================# PAWN_ERROR EXCEPTION #======================#
    "PawnException",
]

# ======================# PAWN_ERROR EXCEPTION #======================#
class PawnException(RankException):
    """
    # ROLE: Catchall Exception

    # RESPONSIBILITIES:
    1.  Catchall for Pawn errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERROR_CODE = "PAWN_ERROR"
    DEFAULT_MESSAGE = "Pawn raised an exception."