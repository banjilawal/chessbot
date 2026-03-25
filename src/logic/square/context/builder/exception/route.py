# src/logic/square/_context/builder/exception/route.py

"""
Module: logic.square.query.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SQUARE_CONTEXT_EXECUTION_ROUTE_EXCEPTION #======================#
    "SquareContextExecutionRouteException",
]

from logic.system import ExecutionRouteException


# ======================# SQUARE_CONTEXT_EXECUTION_ROUTE_EXCEPTION #======================#
class SquareContextExecutionRouteException(ExecutionRouteException):
    """
    Role:Error Tracing, Debugging, Super Exception

    Responsibilities:
    1.  Indicate that there is no build route for a SquareContext attribute.

    Super Class:
        *   ExecutionRoute

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ExecutionRoute class for inherited attributes.

    Attributes:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See ExecutionRoute class for inherited methods.
    """
    MSG = "No build route for SquareContext attribute"
    ERR_CODE = "SQUARE_CONTEXT_EXECUTION_ROUTE_EXCEPTION"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)