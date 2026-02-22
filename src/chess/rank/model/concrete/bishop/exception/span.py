# src/chess/rank/model/concrete/bishop/exception/span.py

"""
Module: chess.rank.model.concrete.bishop.exception.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import SpanComputationException

__all__ = [
    # ======================# BISHOP_SPAN_COMPUTATION_FAILURE #======================#
    "BishopSpanComputationException",
]


# ======================# BISHOP_SPAN_COMPUTATION_FAILURE #======================#
class BishopSpanComputationException(SpanComputationException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the Bishop's spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "BISHOP_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Bishop span computation failed."