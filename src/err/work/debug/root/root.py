# src/logic/system/err/debug/debug.py

"""
Module: logic.system.err.debug.debug
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# DEBUG_EXCEPTION #======================#
    "DebugException",
]

from err import ChessException


# ======================# DEBUG_EXCEPTION #======================#
class DebugException(ChessException):
    """
    Role: Exception Messaging, Exception Chain Layer 2
    # TASK: Capture Error Variable State
    
    Responsibilities:
    1.  Produce the:
            *   variable,
            *   it's Value,
            *   event which fired the variable into its error state.
        which occurred in the Anchor method identified in layer-0 of the exception chain.
    
    # ERROR CODE CONVENTION:
    1.  All caps, snake case description of the error with _EXCEPTION as the suffix.
    
    # DEFAULT MSG CONVENTION:
    1.  Work msg followed by a colon. Description of the error after the colon.
    2.  The Syntax is: [Class] operation failed: [Description]

    Super Class:
        *   ChessException

    Provides:

    # LOCAL ATTRIBUTES:
        *   var (Optional[str])
        *   val Optional[Any])

    # INHERITED ATTRIBUTES:
        *   See ChessException class for inherited attributes.

    Attributes:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See ChessException class for inherited methods.
    """
    ERR_CODE = "VARIABLE_EXCEPTION"
    MSG = "A variable had an error."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
            err_code: Optional[str] = None,
    ):
        """
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )

