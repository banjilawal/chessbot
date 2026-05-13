# src/geometry/diagonalRay/arithmetic/exception/validator.py

"""
Module: geometry.diagonalRay.arithmetic.exception.work
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# RAY_COMPUTATION_FAILURE #======================#
    "RayComputationException",
]

from system import ComputationException


# ======================# RAY_COMPUTATION_FAILURE #======================#
class RayComputationException(ComputationException):
    """
    Role:Worker Method Identifier, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Identify the DiagonalRayComputation method where the exception failed.
    2.  wrap any debug exception created when a condition prevents the computational geometry
        from producing a ray of vectors in the
             where
                *   i < j the domain is y_i = x_(i-1) + c x_i or
                *   j >= N the domain is y_j = x_(j-1) + c x_j

    Super Class:
        *   ComputationException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ComputationException class for inherited attributes.

    Attributes:
        *   err_code (str)
        *   msg (str)
        *   ex (Optional[Exception])
        *   mthd (Optional[str])
        *   op (Optional[str])
        *   mthd_rslt (Optional[str])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See ComputationException class for inherited methods.
    """
    OP = "Computation"
    MTHD_RSLT = "ComputationResult"
    ERR_CODE = "RAY_COMPUTATION_FAILURE"
    MSG = "CoordRay arithmetic failed."
    
    def __init__(
            self,
            err_code: Optional[str] | None = None,
            msg: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd: Optional[str] = None, = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )