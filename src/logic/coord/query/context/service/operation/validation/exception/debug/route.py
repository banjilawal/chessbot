# src/logic/coord/query/context/service/operation/validation/exception/debug/route.py

"""
Module: logic.coord.query.context.service.operation.validation.exception.debug.route
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# COORD_CONTEXT_VALIDATION_ROUTE_EXCEPTION #======================#
    "CoordContextValidationRouteException",
]

from logic.system import ExecutionRouteException

# ======================# COORD_CONTEXT_VALIDATION_ROUTE_EXCEPTION #======================#
class CoordContextValidationRouteException(ExecutionRouteException):
    """
    Role:Exception Chain Layer 2, Exception Messaging
    # TASK: Capture Error Variable State

    Responsibilities:
    1.  A failure ValidationResult was sent because there was no validation route for the CoordContext
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
    MSG = "No validation route for CoordContext attribute"
    ERR_CODE = "COORD_CONTEXT_VALIDATION_ROUTE_EXCEPTION"
    
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