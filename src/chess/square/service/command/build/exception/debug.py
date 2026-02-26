# src/chess/square/service/command/exception/debug.py

"""
Module: chess.square.service.command.exception.debug
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_COMMAND_DEBUG EXCEPTION #======================#
    "SquareDebugException",
]

from chess.system import DebugException


# ======================# SQUARE_COMMAND_DEBUG EXCEPTION #======================#
class SquareDebugException(DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a SquareCommandDebug

    # PARENT:
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   var (Optional[str])
        *   val Optional[None])

    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

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
    ERR_CODE = "SERVICE_COMMAND_DEBUG_ERROR"
    MSG = "A ServiceCommandDebugException was raised."
    VAR: None
    VAL: None
    
    _var: Optional[str]
    _val: Optional[None]
    
    def debug(
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
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)