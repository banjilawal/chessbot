# src/chess/rank/compute/ray/diagonal/exception.py

"""
Module: chess.rank.compute.ray.diagonal.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ComputationFailedException


# ======================# DIAGONAL_RAY_COMPUTATION_FAILURE EXCEPTION #======================#
class DiagonalRayComputationFailedException(ComputationFailedException):
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
    ERROR_CODE = "DIAGONAL_RAY_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Diagonal ray computation failed."