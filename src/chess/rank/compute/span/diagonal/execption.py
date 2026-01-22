# src/chess/rank/compute/span/diagonal/exception.py

"""
Module: chess.rank.compute.span.diagonal.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.rank import SpanComputationFailedException

__all__ = [
    # ======================# DIAGONAL_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
    "DiagonalSpanComputationFailedException",
]


# ======================# DIAGONAL_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
class DiagonalSpanComputationFailedException(SpanComputationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  wrap any debug exception created when a condition prevents the computational logic from producing
        a san in either horizontal:{R(x,y) -> (X,0)}, or vertical:{R(x,y) -> (0,Y)} domains.

    # PARENT:
        *   SpanComputationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DIAGONAL_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Diagonal span computation failed."
    