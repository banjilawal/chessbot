# src/logic/span/service/exception.debug.py

"""
Module: logic.span.service.exception.debug
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# COMPUTED_NULL_RAY_DEBUG_EXCEPTION #======================#
    "ComputedNullRayDebugException",
]

from logic.system import NullException

# ======================# COMPUTED_NULL_RAY_DEBUG_EXCEPTION #======================#
class ComputedNullRayDebugException(NullException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Indicate that a rsy computation's result had no origin, and no members.
        This happens when the start and endpoints are the same.

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
        *   var (Optional[str])
        *   val Optional[Any])
        *   ex (Optional[Exception])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    VAR = Optional[str]
    VAL = Optional[Any]
    ERR_CODE = "COMPUTED_NULL_RAY_DEBUG_EXCEPTION"
    MSG = "The computed ray's start and end points are the same. Product is null."
    
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