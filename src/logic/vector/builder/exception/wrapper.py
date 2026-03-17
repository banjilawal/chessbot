# src/logic/vector/builder/exception/wrapper.py

"""
Module: logic.vector.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# VECTOR_BUILD_FAILURE #======================#
    "VectorBuildException",
]

from logic.system import BuildException

# ======================# VECTOR_BUILD_FAILURE #======================#
class VectorBuildException(BuildException):
    """
    # ROLE: Worker Method Identification, Exception Chain Layer 1, Exception Messaging

    Responsibilities:
    1.  Indicate the VectorBuilder did not produce a valid work product.
    2.  Identify the VectorBuilder method where the failure occurred.

    # PARENT:
        *   BuildException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See BuildException class for inherited attributes.

    # CONSTRUCTOR:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See BuildException class for inherited methods.
    """
    OP = "Build"
    RSLT_TYPE = "BuildResult"
    ERR_CODE = "VECTOR_BUILD_FAILURE"
    MSG = "Failure in VectorBuilder method."

    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
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