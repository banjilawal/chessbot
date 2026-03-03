# src/logic/square.stack/exception/debug.py

"""
Module: logic.square.stack.exception.debug
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SQUARE_STACK_DEBUG_EXCEPTION #======================#
    "SquareStackDebugException",
]

from logic.system import DebugException

# ======================# SQUARE_STACK_DEBUG_EXCEPTION #======================#
class SquareStackDebugException(DebugException):
    """
    # ROLE: Capture Error Variable State, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Produce the:
            *   variable,
            *   it's value,
            *   event which fired the variable into its error state.
        which occurred in the SquareStack method identified in layer-0 of the exception chain.

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
        *   var (Optional[str])
        *   val (Optional[Any])
        *   ex (Optional[Exception])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    VAR = Optional[str]
    VAL = Optional[Any]
    ERR_CODE = "SQUARE_STACK_EXCEPTION"
    MSG = str = "SquareStack had an error."
    
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
            msg (Optional[str]):
            var (Optional[str]):
            val (Optional[Any]):
            ex (Optional[Exception]):
            err_code (Optional[str]):
        """
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(ex=ex, msg=msg, err_code=err_code, var=var, val=val,)