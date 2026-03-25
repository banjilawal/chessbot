# src/logic/node/query/exception/debug.py

"""
Module: logic.node.query.exception.debug
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

from logic.system import DebugException

# ======================# NODE_CONTEXT_DEBUG_EXCEPTION #======================#
class NodeContextDebugException(DebugException):
    """
    Role:Capture Error Variable State, Exception Chain Layer 2, Exception Messaging
    
    Responsibilities:
    1.  Produce the:
            *   variable,
            *   it's value,
            *   event which fired the variable into its error state.
        which occurred in the Anchor method identified in layer-0 of the exception chain.

    Super Class:
        *   DebugException

    Provides:

    # LOCAL ATTRIBUTES:
        *   var (Optional[str])
        *   val (Optional[Any])

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
    ERR_CODE = "NODE_CONTEXT_EXCEPTION"
    MSG = str = "NodeContext had an error."
    VAR = "NodeContext"
    VAL = Optional[Any]
    
    _var = Optional[str]
    _val = Optional[Any]
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
    ):
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
        )

