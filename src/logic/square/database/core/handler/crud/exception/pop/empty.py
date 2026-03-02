# src/logic/square/database/core/exception/deletion/empty.py

"""
Module: logic.square.database.core.exception.deletion.empty
Author: Banji Lawal
Created: 2025-11-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# POPPING_EMPTY_SQUARE_STACK_EXCEPTION #======================#
    "PoppingEmptySquareStackException",
]

from logic.system import DebugException

# ======================# POPPING_EMPTY_SQUARE_STACK_EXCEPTION #======================#
class PoppingEmptySquareStackException(DebugException):
    """
    # ROLE: Exception Chain Layer 2, Exception Messaging
    # TASK: Capture Error Variable State

    # RESPONSIBILITIES:
    1.  Produce the:
            *   variable,
            *   it's value,
            *   event which fired the variable into its error state.
        which occurred in the Hostage method identified in layer-0 of the exception chain.

    2.  A failing DeletionResult was returned because an attempt was made to pop an empty
        square stack.

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
    VAR = Optional[Any]
    VAL = Optional[Any]
    ERR_CODE = "POPPING_EMPTY_SQUARE_STACK_EXCEPTION"
    MSG = "SquareStack pop failed: Cannot pop from an empty stack."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
    ):
        """
        Args:
            msg: str
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(ex=ex, msg=msg, err_code=err_code, var=var, val=val, )
