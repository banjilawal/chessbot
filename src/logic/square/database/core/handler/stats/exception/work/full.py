# src/logic/square/database/core/util/stats/exception/work/full.py

"""
Module: logic.square.database.core.handler.stats.exception.work..full
Author: Banji Lawal
Created: 2026-02-21
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SQUARE_STACK_FULL_EXCEPTION #======================#
    "SquareStackFullException",
]

from logic.system import DebugException

# ======================# SQUARE_STACK_FULL_EXCEPTION #======================#
class SquareStackFullException(DebugException):
    """
    # ROLE: Exception Chain Layer 2, Exception Messaging
    # TASK: Capture Error Variable State

    # RESPONSIBILITIES:
    1.  Produce the:
            *   variable,
            *   it's value,
            *   event which fired the variable into its error state.
        which occurred in the SquareStackCountsAnalyzer method identified in layer-0 of the exception chain.
        
    2.  Indicate a failure InsertionResult was returned because the full SquareStackService had was full.

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
    ERR_CODE = "SQUARE_STACK_FULL_EXCEPTION"
    MSG = "No space to insert a square."
    
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
        super().__init__(ex=ex, msg=msg, err_code=err_code, var=var, val=val,)
