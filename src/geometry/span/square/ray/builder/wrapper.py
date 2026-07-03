# src/geometry/ray/square/ray/build/validator.py

"""
Module: geometry.ray.square.ray.build.work
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_RAY_BUILDER_FAILURE #======================#
    "SquareRayBuilderException",
]

from system import BuilderException

# ======================# SQUARE_RAY_BUILDER_FAILURE #======================#
class SquareRayBuilderException(BuilderException):
    """
    Role:Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    Responsibilities:
    1.  Identify the SquareRayBuilder method where the exception failed.

    Super Class:
        *   BuilderException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See BuilderException class for inherited attributes.

    Attributes:
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        ex: Optional[Exception]
        mthd_rslt_type: Optional[MethodResultType]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See BuilderException class for inherited methods.
    """
    OP = "Build"
    MTHD_RSLT = "BuildResult"
    ERR_CODE = "SQUARE_RAY_BUILDER_FAILURE"
    MSG = "Failure in SquareRayBuilder method."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd_rslt_Ttype: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            ex: Optional[Exception]
            mthd_rslt_type: Optional[MethodResultType]
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
            mthd_rslt_type=mthd_rslt_type,
        )