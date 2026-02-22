# src/chess/rank/compute/ray/exception.py

"""
Module: chess.rank.compute.ray.exception
Author: Banji Lawal
Created: 2026-01-22
version: 1.0.0
"""

from chess.system import ComputationException

__all__ = [
    # ======================# RAY_COMPUTATION_FAILURE #======================#
    "RayComputationException",
]


# ======================# RAY_COMPUTATION_FAILURE #======================#
class RayComputationException(ComputationException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  wrap any debug exception created when a condition prevents the computational logic from producing
        a solution to a subdomain of a ray computation. This exception chain is passed to the caller for handling.

    # PARENT:
        *   ComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERROR_CODE = "RAY_COMPUTATION_FAILURE"
    DEFAULT_MESSAGE = " Ray computation failed."