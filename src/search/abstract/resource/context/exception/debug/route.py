# src/logic/system/search/resource/context/exception/debug/route.py

"""
Module: logic.system.search.resource.context.exception.debug.route
Author: Banji Lawal
Created: 2026-04-01
Version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional


_all_ = [
    # ======================# CONTEXT_ROUTE_EXCEPTION #======================#
    "ContextRouteException",
]

from logic.system import ExecutionRouteException


# ======================# CONTEXT_ROUTE_EXCEPTION #======================#
class ContextRouteException(ExecutionRouteException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that a Context worker did not have execution logic for
            a Context's attribute.

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
    MSG = str = "No execution logic for the Context attribute."
    ERR_CODE = "CONTEXT_ROUTE_EXCEPTION"
    
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