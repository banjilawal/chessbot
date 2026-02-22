# src/chess/rank/compute/span/exception.py

"""
Module: chess.rank.compute.span.exception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.system import ComputationException

__all__ = [
    # ======================# SPAN_COMPUTATION_FAILURE #======================#
    "SpanComputationException",
]


# ======================# SPAN_COMPUTATION_FAILURE #======================#
class SpanComputationException(ComputationException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  wrap any debug exception created when a condition prevents the computational logic from producing
        a solution. This exception chain is passed to the caller for handling.

    # PARENT:
        *   ComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = " Span computation failed."