# src/chess/system/builder/exception/wrapper.py

"""
Module: chess.system.builder.exception.wrapper
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
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
    
    # PROVIDES:
    None
    
    # LOCAL ATTRIBUTES:
        *   op_name (Optional[str])
    
    INHERITED ATTRIBUTES:
        *   See WrapperException class for inherited attributes.
    
    # CONSTRUCTOR PARAMETERS:
            *   op_name (Optional[str])
            *   rslt (Optional[str])
            *   mthd (Optional[str])
                err_code (Optional[str])
                ms (Optional[str])
                ex (Optional[Exception])
    
    # LOCAL METHODS:
    None
    
    # INHERITED METHODS:
    *   See WrapperException class for inherited methods.
    """
    ERR_CODE = "BUILD_FAILURE"
    MSG = "Build failed."
    MTHD = "build"
    OP_NAME = "build"
    RSLT = "BuildResult"
    
    _op_name: Optional[str]
    _rslt: Optional[str]
    
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
        
        super().__init__(msg=msg, err_code=err_code, ex=ex)
        self._rslt = rslt
        self._mthd = mthd
        self._op_name = op_name or self.OP_NAME
    
    @property
    def rslt(self) -> Optional[str]:
        return self._rslt
    
    @property
    def mthd(self) -> Optional[str]:
        return self._mthd
    
    @property
    def op_name(self) -> Optional[str]:
        return self._op_name
    
    def __str__(self):
        return f"{super().__str__()}, op_name:{self._op_name}, rslt:{self._rslt}"
