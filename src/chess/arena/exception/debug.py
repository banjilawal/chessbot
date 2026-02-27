# src/chess/arena/exception/debug.py

"""
Module: chess.arena.exception.debug
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# ARENA_DEBUG_EXCEPTION #======================#
    "ArenaDebugException",
]

from chess.system import DebugException

# ======================# ARENA_DEBUG_EXCEPTION #======================#
class ArenaDebugException(DebugException):
    """
    # ROLE: Capture Error Variable State, Exception Chain Layer 2, Exception Messaging
    
    # RESPONSIBILITIES:
    1.  Produce the:
            *   variable,
            *   it's value,
            *   event which fired the variable into its error state.
        which occurred in the Anchor method identified in layer-0 of the exception chain.

    # PARENT:
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   var (Optional[str])
        *   val (Optional[None])

    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val (Optional[None])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    ERR_CODE = "ARENA_EXCEPTION"
    MSG = str = "Arena had an error."
    VAR = None
    VAL = None
    
    _var = Optional[str]
    _val = Optional[None]
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            var: Optional[str] = None,
            val: Optional[None] = None,
    ):
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(ex=ex, msg=msg, var=var, val=val, err_code=err_code,)

