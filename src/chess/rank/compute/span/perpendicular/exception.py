# src/chess/rank/compute/span/perpendicular/exception.py

"""
Module: chess.rank.compute.span.perpendicular.exception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.rank import SpanComputationFailedException


__all__ = [
    # ======================# PERPENDICULAR_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
    "PerpendicularSpanComputationFailedException",
]


# ======================# PERPENDICULAR_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
class PerpendicularSpanComputationFailedException(SpanComputationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  Wrap any debug exception created when a condition prevents the computational logic from producing
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
    ERROR_CODE = "PERPENDICULAR_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Perpendicular span computation failed."