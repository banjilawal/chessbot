# src/logic/token/_context/build/exception/route.py

"""
Module: logic.token.query.context.build.exception.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# TOKEN_CONTEXT_BUILD_ROUTE_EXCEPTION #======================#
    "TokenContextBuildRouteException",
]

from logic.system import ExecutionRouteException

# ======================# TOKEN_CONTEXT_BUILD_ROUTE_EXCEPTION #======================#
class TokenContextBuildRouteException(ExecutionRouteException):
    """
    Role:Exception Chain Layer 2, Exception Messaging
    # TASK: Capture Error Variable State

    Responsibilities:
    1.  A failure BuildResult was sent because there was no build route for the TokenContext
        attribute.

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
    MSG = "No build route for TokenContext attribute"
    ERR_CODE = "TOKEN_CONTEXT_BUILD_ROUTE_EXCEPTION"
    
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