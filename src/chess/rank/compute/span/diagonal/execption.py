# src/chess/rank/compute/span/diagonal/exception.py

"""
Module: chess.rank.compute.span.diagonal.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ComputationFailedException


__all__ = [
    # ======================# DIAGONAL_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
    "DiagonalSpanComputationFailedException",
]

# ======================# DIAGONAL_SPAN_COMPUTATION_FAILURE EXCEPTION #======================#
class DiagonalSpanComputationFailedException(ComputationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  wrap any debug exception created when a condition prevents the computational logic from producing
        a solution. This exception chain is passed to the caller for handling.

    # PARENT:
        *   ComputationFailedException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "DIAGONAL_SPAN_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Diagonal span computation failed."
    