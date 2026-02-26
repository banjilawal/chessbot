# src/chess/system/err/debug/child/null.py

"""
Module: chess.system.err.debug.child.null
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional


__all__ = [
    # ======================# NO_EXECUTION_ROUTE_FOR_OPTION EXCEPTION #======================#
    "NoExecutionRouteException",
]

from chess.system import DebugException

# ======================# NO_EXECUTION_ROUTE_FOR_OPTION EXCEPTION #======================#
class NoExecutionRouteException(DebugException):
    """
    # ROLE: Error Tracing, Debugging, Super Exception

    # RESPONSIBILITIES:
    1.  Indicate that an operation failed because there was no coverage for at least one of its optional
        success paths.

    # PARENT:
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[None])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    ERR_CODE = "NO_EXECUTION_ROUTE_FOR_OPTION_ERROR"
    MSG = "No execution route exists for the operation option."
    VAR: None
    VAL: None
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            var: Optional[str] = None,
            val: Optional[None] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        var = var or self.VAR
        val = val or self.VAL
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)

 
    