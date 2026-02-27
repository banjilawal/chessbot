# src/chess/rank/model/concrete/pawn/exception.py

"""
Module: chess.rank.model.concrete.pawn.exception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import RankException

__all__ = [
    # ======================# PAWN_EXCEPTION EXCEPTION #======================#
    "PawnException",
]

# ======================# PAWN_EXCEPTION EXCEPTION #======================#
class PawnException(RankException):
    """
    # ROLE: Super Exception

    # RESPONSIBILITIES:
    1.  Super for Pawn errors.

    # PARENT:
        *   RankException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "PAWN_EXCEPTION"
    MSG = "Pawn raised an exception."