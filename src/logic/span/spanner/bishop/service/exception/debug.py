# src/logic/span/spanner/bishop/service/exception/debug.py

"""
Module: logic.span.spanner.bishop.service.exception.debug
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# BISHOP_SPAN_SERVICE_DEBUG EXCEPTION #======================#
    "BishopSpanServiceDebugException",
]

from logic.span import SpanServiceDebugException


# ======================# BISHOP_SPAN_SERVICE_DEBUG EXCEPTION #======================#
class BishopSpanServiceDebugException(SpanServiceDebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a BishopSpanService operation failure.

    # PARENT:
        *   SpanServiceDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   var (Optional[str])
        *   val Optional[Any])

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
        *   See SpanServiceDebugException class for inherited methods.
    """
    VAR: None
    VAL = Optional[Any]
    ERR_CODE = "BISHOP_SPAN_SERVICE_EXCEPTION"
    MSG: str = "A variable in BishopSpanService raised an exception."
    
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