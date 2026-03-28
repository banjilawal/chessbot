# src/logic/span/spanner/engine/exception/debug/route.py

"""
Module: logic.span.spanner.engine.exception.debug.route
Author: Banji Lawal
Created: 2026-03-10
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# SPAN_COMPUTATION_ROUTE_EXCEPTION #======================#
    "SpanComputationRouteException",
]

from logic.system import ExecutionRouteException

# ======================# SPAN_COMPUTATION_ROUTE_EXCEPTION #======================#
class SpanComputationRouteException(ExecutionRouteException):
    """
    Role:Exception Chain Layer 2, Exception Messaging
    # TASK: Capture Error Variable State

    Responsibilities:
    1.  A failure ComputationResult was sent because there was no arithmetic route for the RayProvider.

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
    ERR_CODE = "SPAN_COMPUTATION_ROUTE_EXCEPTION"
    MSG = "No span arithmetic route for the ray provider."
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
    ):
        """
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)