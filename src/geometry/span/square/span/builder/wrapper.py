# src/geometry/span/square/build/validator.py

"""
Module: geometry.span.square.build.work
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_SPAN_BUILD_FAILURE #======================#
    "SquareSpanBuildException",
]

from system import BuildException


# ======================# SQUARE_SPAN_BUILD_FAILURE #======================#
class SquareSpanBuildException(BuildException):
    """
    Role:Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    Responsibilities:
    1.  Identify the SquareSpanBuilder method where the exception failed.

    Super Class:
        *   BuildException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See BuildException class for inherited attributes.

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
        *   See BuildException class for inherited methods.
    """
    OP = "Build"
    MTHD_RSLT = "BuildResult"
    ERR_CODE = "SQUARE_SPAN_BUILD_FAILURE"
    MSG = "Failure in SquareSpanBuilder method."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd_rslt: Optional[ResultCategory] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            ex: Optional[Exception]
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