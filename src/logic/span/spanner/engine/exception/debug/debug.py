# src/logic/span/spanner/engine/exception/debug/debug.py

"""
Module: logic.span.spanner.engine.exception.debug.debug
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SPANNER_ENGINE_DEBUG_EXCEPTION #======================#
    "SpannerEngineDebugException",
]

from logic.system import DebugException

# ======================# SPANNER_ENGINE_DEBUG_EXCEPTION #======================#
class SpannerEngineDebugException(DebugException):
    """
    # ROLE: Capture Error Variable State, Exception Chain Layer 2, Exception Messaging
    
    # RESPONSIBILITIES:
    1.  Produce the:
            *   variable,
            *   it's value,
            *   event which fired the variable into its error state.
        which occurred in the SpannerEngine method identified in layer-0 of the exception chain.

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
        *   val (Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    VAR = Optional[str]
    VAL = Optional[Any]
    ERR_CODE = "SPANNER_ENGINE_DEBUG_EXCEPTION"
    MSG = str = "Condition brought SpannerEngine into error state."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        """
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            err_code: Optional[str]
            ex: Optional[Exception]
        """
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(ex=ex, msg=msg, var=var, val=val, err_code=err_code)

