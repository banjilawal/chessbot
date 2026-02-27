# src/chess/system/err/debug/debug.py

"""
Module: chess.system.err.debug.debug
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# DEBUG EXCEPTION #======================#
    "DebugException",
]

from chess.system import ChessException

# ======================# DEBUG EXCEPTION #======================#
class DebugException(ChessException):
    """
    # ROLE: Error Block Identifier, Exception Chain Layer 1, Exception Messaging
    
    # RESPONSIBILITIES:
    1.  Identifies the code block in a method where the error occurred.
    2.  Describe what condition or state prevented an operation from completing successfully.
    3.  Lowest part of the 3-layer exception chain. Should not contain other exceptions.
    
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
        *   val Optional[None])

    # INHERITED ATTRIBUTES:
        *   See ChessException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[None])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See ChessException class for inherited methods.
    """
    ERR_CODE = "VARIABLE_EXCEPTION"
    MSG: str = "A variable had an error."
    VAR: None
    VAL = None
    
    _var: Optional[str]
    _val: Optional[None]
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[None] = None,
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
    def val(self) -> Optional[None]:
        return self._val
    
    def __str__(self):
        return f"{super().__str__()}, var:{self._var}, val:{self._val}"

