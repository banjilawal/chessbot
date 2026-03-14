# src/logic/system/err/debug/debug.py

"""
Module: logic.system.err.debug.debug
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# DEBUG_EXCEPTION #======================#
    "DebugException",
]

from logic.system import ChessException

# ======================# DEBUG_EXCEPTION #======================#
class DebugException(ChessException):
    """
    # ROLE:  Exception Messaging, Exception Chain Layer 2
    # TASK: Capture Error Variable State
    
    # RESPONSIBILITIES:
    1.  Produce the:
            *   variable,
            *   it's Value,
            *   event which fired the variable into its error state.
        which occurred in the Anchor method identified in layer-0 of the exception chain.
    
    # ERROR CODE CONVENTION:
    1.  All caps, snake case description of the error with _EXCEPTION as the suffix.
    
    # DEFAULT MSG CONVENTION:
    1.  Wrapper msg followed by a colon. Description of the error after the colon.
    2.  The Syntax is: [Class] operation failed: [Description]

    # PARENT:
        *   ChessException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   var (Optional[str])
        *   val Optional[Any])

    # INHERITED ATTRIBUTES:
        *   See ChessException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
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
    VAR = Optional[str]
    VAL = Optional[Any]
    
    _var: Optional[str]
    _val: Optional[Any]
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        
        super().__init__(msg=msg, err_code=err_code, ex=ex)
        self._var = var
        self._val = val
    
    @property
    def var(self) -> Optional[str]:
        return self._var
    
    @property
    def val(self) -> Optional[Any]:
        return self._val
    
    def __str__(self):
        return f"{super().__str__()}, var:{self._var}, val:{self._val}"

