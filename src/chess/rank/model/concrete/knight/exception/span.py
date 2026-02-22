# src/chess/rank/model/concrete/knight/exception/span.py

"""
Module: chess.rank.model.concrete.knight.exception.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import SpanComputationException

__all__ = [
    # ======================# KNIGHT_SPAN_COMPUTATION_FAILURE #======================#
    "KnightSpanComputationException",
]


# ======================# KNIGHT_SPAN_COMPUTATION_FAILURE #======================#
class KnightSpanComputationException(SpanComputationException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the Knight's spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "KNIGHT_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Knight span computation failed."