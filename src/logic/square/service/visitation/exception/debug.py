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
    # ======================# TOKEN_HANDLER_DEBUG_EXCEPTION #======================#
    "TokenVisitHandlerDebugException",
]

from logic.system import DebugException

# ======================# TOKEN_HANDLER_DEBUG_EXCEPTION #======================#
class TokenVisitHandlerDebugException(DebugException):
    """
    Role:
        -   Capture Error Variable State
        -   Exception Chain Layer 2
        -   Exception Messaging

    Responsibilities:
        1.  Produce the:
                *   variable,
                *   it's value,
                *   event which fired the variable into its error state.
            which occurred in the VisitationManager method identified in layer-0 of the exception chain.

    Attributes:
        msg (Optional[str]):
        var (Optional[str]):
        val (Optional[Any]):
        ex (Optional[Exception]):
        err_code (Optional[str]):

    Provides:

    Super Class:
        DebugException
    """
    ERR_CODE = "SQUARE_STACK_TOKEN_HANDLER_EXCEPTION"
    MSG = str = "VisitationManager had an error."
    
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
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(ex=ex, msg=msg, err_code=err_code, var=var, val=val,)