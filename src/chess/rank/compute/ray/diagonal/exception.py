# src/chess/rank/compute/ray/diagonal/exception.py

"""
Module: chess.rank.compute.ray.diagonal.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

__all__ = [
    # ======================# DIAGONAL_RAY_COMPUTATION_FAILURE EXCEPTION #======================#
    "DiagonalRayComputationFailedException",
]

from chess.rank import RayComputationFailedException


# ======================# DIAGONAL_RAY_COMPUTATION_FAILURE EXCEPTION #======================#
class DiagonalRayComputationFailedException(RayComputationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  wrap any debug exception created when a condition prevents the computational logic from producing
        a ray of vectors in the
             where 
                *   i < j the domain is y_i = x_(i-1) + c x_i or
                *   j >= N the domain is y_j = x_(j-1) + c x_j

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