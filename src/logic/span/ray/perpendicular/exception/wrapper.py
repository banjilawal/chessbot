# src/logic/span/ray/perpendicular/exception/wrapper.py

"""
Module: logic.span.ray/perpendicular.exception.wrapper
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

from logic.span import RayComputationException

# ======================# PERPENDICULAR_RAY_COMPUTATION_FAILURE #======================#
class PerpendicularRayComputationException(RayComputationException):
    """
    # ROLE: Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    # RESPONSIBILITIES:
    1.  Identify the PerpendicularRayComputation method where the process failed.
    2.  wrap any debug exception created when a condition prevents the computational logic from producing
        a ray of vectors in the
            horizontal subdomains:
                *  the regions where [-n < i] or [i <= j < n] the domain is (x_i, y_i) -> R(:X_i,X_j)
            Vertical subdomains:
                *  the regions where [-n < i] or [i <= j < n] the domain is (x_i, y_i) -> R(:X_j,Y_-)

    # PARENT:
        *   RayComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # INHERITED ATTRIBUTES:
        *   See RayComputationException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:)
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
    MTHD = None
    OP = "Computation"
    RSLT_TYPE = "ComputationResult"
    MSG = "PerpendicularRayComputation failed."
    ERR_CODE = "PERPENDICULAR_RAY_COMPUTATION_FAILURE"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            rslt_type: Optional[str]
        """
        op = op or self.OP
        msg = msg or self.MSG
        mthd = mthd or self.MTHD
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