# src/chess/node/context/exception/debug.py

"""
Module: chess.node.context.exception.debug
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# NODE_CONTEXT_DEBUG_EXCEPTION #======================#
    "NodeContextDebugException",
]

from chess.system import DebugException

# ======================# NODE_CONTEXT_DEBUG_EXCEPTION #======================#
class NodeContextDebugException(DebugException):
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
    ERR_CODE = "NODE_CONTEXT_EXCEPTION"
    MSG = str = "NodeContext had an error."
    VAR = "NodeContext"
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
        
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
        )

