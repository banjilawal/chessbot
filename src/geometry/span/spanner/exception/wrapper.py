# src/geometry/span/validation/exception/validator.py

"""
Module: geometry.span.validation.exception.work
Author: Banji Lawal
Created: 2025-09-08
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SPAN_COMPUTATION_FAILURE #======================#
    "SpanComputationException",
]

from system import ComputationException


# ======================# SPAN_COMPUTATION_FAILURE #======================#
class SpanComputationException(ComputationException):
    """
    Role:Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    Responsibilities:
    1.  Identify the Spanner method where the exception failed.

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
    ERR_CODE = "SPAN_COMPUTATION_FAILURE"
    MSG = "Failure in Spanner method."
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None, = None,
            mthd_rslt: Optional[ResultCategory] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            mthd_rslt: Optional[ResultCategory]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            mthd_rslt=mthd_rslt,
        )