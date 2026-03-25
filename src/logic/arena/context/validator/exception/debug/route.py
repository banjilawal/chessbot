# src/logic/arena/query/validation/exception/debug/route.py

"""
Module: logic.arena.query.validation.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# ARENA_CONTEXT_VALIDATION_ROUTE_EXCEPTION #======================#
    "ArenaContextValidationRouteException",
]

from logic.system import ExecutionRouteException

# ======================# ARENA_CONTEXT_VALIDATION_ROUTE_EXCEPTION #======================#
class ArenaContextValidationRouteException(ExecutionRouteException):
    """
    Role:Exception Chain Layer 2, Exception Messaging
    # TASK: Capture Error Variable State

    Responsibilities:
    1.  A failure ValidationResult was sent because there was no validation route for the ArenaContext
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
    MSG = "No validation route for ArenaContext attribute"
    ERR_CODE = "ARENA_CONTEXT_VALIDATION_ROUTE_EXCEPTION"
    
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