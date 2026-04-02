# src/logic/square/validation/exception/flag/excess.py

"""
Module: logic.square.validation.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# EXCESS_SQUARE_CONTEXT_FLAGS_EXCEPTION #======================#
    "ExcessSquareContextFlagsException",
]

from logic.system import DebugException

# ======================# EXCESS_SQUARE_CONTEXT_FLAGS_EXCEPTION #======================#
class ExcessSquareContextFlagsException(DebugException):
    """
    Role:Exception Chain Layer 2, Exception Messaging
    # TASK: Capture Error Variable State

    Responsibilities:
    1.  Produce the:
            *   variable,
            *   it's value,
            *   event which fired the variable into its error state.
        which occurred in the SquareContextBuilder method identified in layer-0 of the exception chain.

    2.  A failing ValidationResult was returned because SquareContext rank had more than one flag enabled.
    
    Super Class:
        *   DebugException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

    Attributes:
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
    MSG = "More than one SquareContext flag enabled."
    ERR_CODE = "EXCESS_SQUARE_CONTEXT_FLAGS_EXCEPTION"
    
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
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(ex=ex, msg=msg, err_code=err_code, var=var, val=val,)