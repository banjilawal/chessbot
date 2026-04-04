# src/logic/system/err/debug/child/route/root.py

"""
Module: logic.system.err.debug.child.route.root
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# EXECUTION_ROUTE_EXCEPTION #======================#
    "ExecutionRouteException",
]

from logic.system import DebugException

# ======================# EXECUTION_ROUTE_EXCEPTION #======================#
class ExecutionRouteException(DebugException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider
    
    Responsibilities:
        1.  Indicate that an execution route was missing from the logic.
        
    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        
    Provides:
    
    Super Class:
        DebugException
    """
    MSG = "Missing execution route."
    ERR_CODE = "EXECUTION_ROUTE_EXCEPTION"

    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        """
        Args:
            var: Optional[str]
            val: Optional[Any]
            msg: Optional[str]
            ex: Optional[Exception]
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
        )
