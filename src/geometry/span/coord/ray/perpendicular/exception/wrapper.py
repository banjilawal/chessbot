# src/geometry/span/coord/ray/perpendicular/exception/validator.py

"""
Module: geometry.span.coord.ray.perpendicular.exception.work
Author: Banji Lawal
Created: 2026-03-8
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# PERPENDICULAR_RAY_COMPUTATION_FAILURE #======================#
    "PerpendicularRayComputationException",
]

from math.span import RayComputationException

# ======================# PERPENDICULAR_RAY_COMPUTATION_FAILURE #======================#
class PerpendicularRayComputationException(RayComputationException):
    """
    Role:Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    Responsibilities:
    1.  Identify the PerpendicularRayComputation method where the exception failed.
    2.  wrap any debug exception created when a condition prevents the computational geometry from producing
        a ray of vectors in the
            horizontal subdomains:
                *  the regions where [-n < i] or [i <= j < n] the domain is (x_i, y_i) -> R(:X_i,X_j)
            Vertical subdomains:
                *  the regions where [-n < i] or [i <= j < n] the domain is (x_i, y_i) -> R(:X_j,Y_-)

    Super Class:
        *   RayComputationException

    Provides:

    # LOCAL ATTRIBUTES:
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # INHERITED ATTRIBUTES:
        *   See RayComputationException class for inherited attributes.

    Attributes:
        *   err_code (str)
        *   msg (str)
        *   ex (Optional[Exception])
        *   mthd (Optional[str])
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See RayComputationException class for inherited methods.
    """
    OP = "Computation"
    RSLT_TYPE = "ComputationResult"
    MSG = "PerpendicularRayComputation failed."
    ERR_CODE = "PERPENDICULAR_RAY_COMPUTATION_FAILURE"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None, = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            rslt_type: Optional[str]
        """
        op = op or self.OP
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            rslt_type=rslt_type,
        )