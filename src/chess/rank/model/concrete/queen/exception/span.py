# src/chess/rank/model/concrete/queen/exception/span.py

"""
Module: chess.rank.model.concrete.queen.exception.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import SpanComputationFailedException

__all__ = [
    # ======================# QUEEN_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
    "QueenSpanComputationFailedException",
]


# ======================# QUEEN_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
class QueenSpanComputationFailedException(SpanComputationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the Queen's spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "QUEEN_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Queen span computation failed."