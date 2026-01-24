# src/chess/rank/model/concrete/rook/exception/span.py

"""
Module: chess.rank.model.concrete.rook.exception.span
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import SpanComputationFailedException

__all__ = [
    # ======================# ROOK_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
    "RookSpanComputationFailedException",
]


# ======================# ROOK_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
class RookSpanComputationFailedException(SpanComputationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any exceptions that prevent the Rook's spanning set computation from producing a result.

    # PARENT:
        *   SpanComputationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "ROOK_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Rook span computation failed."