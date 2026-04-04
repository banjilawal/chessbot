# src/logic/ray/square/ray/build/validator.py

"""
Module: logic.ray.square.ray.build.work
Author: Banji Lawal
Created: 2026-03-11
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_RAY_BUILD_FAILURE #======================#
    "SquareRayBuildException",
]

from system import BuildException

# ======================# SQUARE_RAY_BUILD_FAILURE #======================#
class SquareRayBuildException(BuildException):
    """
    Role:Exception Chain Layer 1, Exception Messaging
    # TASK: Worker Method Identifier

    Responsibilities:
    1.  Identify the SquareRayBuilder method where the exception failed.

    Super Class:
        *   BuildException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See BuildException class for inherited attributes.

    Attributes:
        op: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        ex: Optional[Exception]
        rslt_type: Optional[str]

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See BuildException class for inherited methods.
    """
    OP = "Build"
    RSLT_TYPE = "BuildResult"
    ERR_CODE = "SQUARE_RAY_BUILD_FAILURE"
    MSG = "Failure in SquareRayBuilder method."
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            ex: Optional[Exception]
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