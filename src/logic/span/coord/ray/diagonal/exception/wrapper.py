# src/logic/span/coord/ray/diagonal/diagonal/exception/wrapper.py

"""
Module: logic.span.coord.ray.diagonal.diagonal.exception.wrapper
Author: Banji Lawal
Created: 2026-02-28
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# DIAGONAL_RAY_COMPUTATION_FAILURE #======================#
    "DiagonalRayComputationException",
]

from logic.span import RayComputationException

# ======================# DIAGONAL_RAY_COMPUTATION_FAILURE #======================#
class DiagonalRayComputationException(RayComputationException):
    """
    # ROLE: Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    # RESPONSIBILITIES:
    1.  Identify the DiagonalRayComputation method where the process failed.
    2.  wrap any debug exception created when a condition prevents the computational logic
        from producing a ray of vectors in the
             where
                *   i < j the domain is y_i = x_(i-1) + c x_i or
                *   j >= N the domain is y_j = x_(j-1) + c x_j

    # PARENT:
        *   RayComputationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

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
    MTHD = Optional[str]
    OP = "Computation"
    RSLT_TYPE = "ComputationResult"
    ERR_CODE = "DIAGONAL_RAY_COMPUTATION_FAILURE"
    MSG = "Failure in DiagonalRayComputation method."
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        op = op or self.OP
        msg = msg or self.MSG
        mthd = mthd or self.MTHD
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            rslt_type: Optional[str]
        """
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            rslt_type=rslt_type,
        )