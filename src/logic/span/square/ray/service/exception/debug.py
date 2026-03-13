# src/logic/span/square/rayservice/exception.debug.py

"""
Module: logic.span.square.ray.service.exception.debug
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SQUARE_RAY_SERVICE_DEBUG_EXCEPTION #======================#
    "SquareRayServiceDebugException",
]

from logic.system import DebugException

# ======================# SQUARE_RAY_SERVICE_DEBUG_EXCEPTION #======================#
class SquareRayServiceDebugException(DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a SquareRayService operation failure.

    # PARENT:
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   DebugException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[Any])
        
    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    VAR = Optional[str]
    VAL = Optional[Any]
    ERR_CODE = "SQUARE_RAY_SERVICE_EXCEPTION"
    MSG = "A variable in SquareRayService raised an exception."
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
):
        """
        Args:
            var: Optional[str]
            val: Optional[Any]
            msg: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)