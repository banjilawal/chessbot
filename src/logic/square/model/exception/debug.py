# src/logic/square/context/context/exception/debug.py

"""
Module: logic.square.context.context.exception.debug
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SQUARE_CONTEXT_DEBUG_EXCEPTION #======================#
    "SquareContextDebugException",
]

from logic.system import DebugException

# ======================# SQUARE_CONTEXT_DEBUG_EXCEPTION #======================#
class SquareContextDebugException(DebugException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Record the condition that fired a variable's error state. a Square instance into its  error state.
        2.  Parent of all debugging metadata providers who must report to Square instances.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        DebugException
    """
    ERR_CODE = "SQUARE_CONTEXT_EXCEPTION"
    MSG = "SquareContext had an error."
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
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
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)

