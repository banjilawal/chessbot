# src/chess/rank/compute/ray/perpendicular/exception.py

"""
Module: chess.rank.compute.ray.perpendicular.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""

from chess.system import ComputationFailedException

__all__ = [
    # ======================# PERPENDICULAR_RAY_COMPUTATION_FAILURE EXCEPTION #======================#
    "PerpendicularRayComputationFailedException",
]


# ======================# PERPENDICULAR_RAY_COMPUTATION_FAILURE EXCEPTION #======================#
class PerpendicularRayComputationFailedException(ComputationFailedException):
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
    ERROR_CODE = "PERPENDICULAR_RAY_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = "Perpendicular ray computation failed."