# src/chess/system/builder/exception/wrapper.py

"""
Module: chess.system.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""
from typing import Optional

from chess.system import OperationException

__all__ = [
    # ======================# BUILD_FAILURE #======================#
    "BuildException",
]


# ======================# BUILD_FAILURE #======================#
class BuildException(OperationException):
    """
    # ROLE: Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Encapsulate the Layer-1 DebugException which describes what condition prevented the build 
        from completing.

    # PARENT:
        *   OperationException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
    None
    """
    ERR_CODE = "BUILD_FAILURE"
    MSG = "Build failed."
    MTHD = "build"
    OP_NAME = "build"
    RSLT = "BuildResult"
    
    def __init__(
            self,
            rslt: Optional[str] = None,
            op_name: Optional[str] = None,
            mthd: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        rslt = rslt or self.RSLT
        op_name = op_name or self.OP_NAME
        mthd = mthd or self.MTHD
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        
        super().__init__(msg=msg, err_code=err_code, ex=ex, rslt=rslt, mthd=mthd, op_name=op_name)
