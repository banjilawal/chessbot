# src/chess/rank/compute/ray/perpendicular/exception.py

"""
Module: chess.rank.compute.ray.perpendicular.exception
Author: Banji Lawal
Created: 2025-09-08
version: 1.0.0
"""



__all__ = [
    # ======================# PERPENDICULAR_RAY_COMPUTATION_FAILURE EXCEPTION #======================#
    "PerpendicularRayComputationFailedException",
]

from chess.rank import RayComputationFailedException


# ======================# PERPENDICULAR_RAY_COMPUTATION_FAILURE EXCEPTION #======================#
class PerpendicularRayComputationFailedException(RayComputationFailedException):
    """
    # ROLE: Exception Wrapper, Encapsulation, Error Chaining

    # RESPONSIBILITIES:
    1.  wrap any debug exception created when a condition prevents the computational logic from producing
        a ray of vectors in the
            horizontal subdomains:
                *  the regions where [-n < i] or [i <= j < n] the domain is (x_i, y_i) -> R(:X_i,X_j)
            Vertical subdomains:
                *  the regions where [-n < i] or [i <= j < n] the domain is (x_i, y_i) -> R(:X_j,Y_-)
                
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