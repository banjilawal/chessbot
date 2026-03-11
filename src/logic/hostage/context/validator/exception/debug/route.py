# src/logic/hostage/context/validator/exception/debug/route.py

"""
Module: logic.hostage.context.validator.exception.debug.route
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""
from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# HOSTAGE_CONTEXT_VALIDATION_ROUTE_EXCEPTION #======================#
    "HostageContextValidationRouteException",
]

from logic.system import ExecutionRouteException

# ======================# HOSTAGE_CONTEXT_VALIDATION_ROUTE_EXCEPTION #======================#
class HostageContextValidationRouteException(ExecutionRouteException):
    """
    # ROLE: Exception Chain Layer 2, Exception Messaging
    # TASK: Capture Error Variable State

    # RESPONSIBILITIES:
    1.  A failure ValidationResult was sent because there was no validation route for the HostageContext
        attribute.

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
    VAR = Optional[str]
    VAL = Optional[Any]
    MSG = "No validation route for HostageContext attribute"
    ERR_CODE = "HOSTAGE_CONTEXT_VALIDATION_ROUTE_EXCEPTION"
    
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