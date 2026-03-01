# src/logic/rank/_context/builder/exception/route.py

"""
Module: logic.rank.context.builder.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# RANK_CONTEXT_EXECUTION_ROUTE_EXCEPTION #======================#
    "RankContextExecutionRouteException",
]

from logic.system import ExecutionRouteException


# ======================# RANK_CONTEXT_EXECUTION_ROUTE_EXCEPTION #======================#
class RankContextExecutionRouteException(ExecutionRouteException):
    """
    # ROLE: Error Tracing, Debugging, Super Exception

    # RESPONSIBILITIES:
    1.  Indicate that there is no build route for a RankContext attribute.

    # PARENT:
        *   ExecutionRoute

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ExecutionRoute class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
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
    ERR_CODE = "RANK_CONTEXT_EXECUTION_ROUTE_EXCEPTION"
    MSG = "No build route for RankContext attribute"
    VAR = Optional[Any]
    VAL = Optional[Any]
    
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
        var = var or self.VAR
        val = val or self.VAL
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)