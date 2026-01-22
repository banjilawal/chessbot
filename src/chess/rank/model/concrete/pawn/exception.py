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
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the Pawn's spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "PAWN_ERROR"
    DEFAULT_MESSAGE = "Pawn raised an exception."