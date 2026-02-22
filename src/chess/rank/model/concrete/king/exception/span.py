# src/chess/rank/model/concrete/king/exception/span.py

"""
Module: chess.rank.model.concrete.king.exception.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import SpanComputationException

__all__ = [
    # ======================# KING_SPAN_COMPUTATION_FAILURE #======================#
    "KingSpanComputationException",
]


# ======================# KING_SPAN_COMPUTATION_FAILURE #======================#
class KingSpanComputationException(SpanComputationException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the King's spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "KING_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "King span computation failed."