# src/logic/rank/model/concrete/queen/exception/span.py

"""
Module: logic.rank.model.concrete.queen.exception.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from logic.rank import SpanComputationException

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
    ERR_CODE = "QUEEN_SPAN_COMPUTATION_FAILURE"
    MSG = "Queen span computation failed."