# src/chess/graph/exception/debug.py

"""
Module: chess.graph.exception.debug
Author: Banji Lawal
Created: 2026-01-26
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# GRAPH_DEBUG EXCEPTION #======================#
    "GraphDebugException",
]

from chess.system import DebugException


# ======================# GRAPH_DEBUG EXCEPTION #======================#
class GraphDebugException(DebugException):
    """
    # ROLE: Error Tracing, Debugging

    # RESPONSIBILITIES:
    1.  Describes the condition that caused a Graph operation failure.

    # PARENT:
        *   DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
        *   var (Optional[str])
        *   val Optional[None])

    # INHERITED ATTRIBUTES:
        *   DebugException class for inherited attributes.

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
    ERR_CODE = "GRAPH_EXCEPTION"
    MSG: str = "A variable in Graph raised an exception."
    VAR: None
    VAL = None
    
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