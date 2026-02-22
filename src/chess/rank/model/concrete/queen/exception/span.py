# src/chess/rank/model/concrete/queen/exception/span.py

"""
Module: chess.rank.model.concrete.queen.exception.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import SpanComputationException

__all__ = [
    # ======================# QUEEN_SPAN_COMPUTATION_FAILURE #======================#
    "QueenSpanComputationException",
]


# ======================# QUEEN_SPAN_COMPUTATION_FAILURE #======================#
class QueenSpanComputationException(SpanComputationException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the Queen's spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "QUEEN_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Queen span computation failed."