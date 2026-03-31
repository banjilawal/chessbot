# src/command/request/validation/exception/debug/identifier.py

"""
Module: command.request.validation.exception.debug.identifier
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# WRONG_ARGUMENT_NAME_EXCEPTION #======================#
    "ArgumentNameException",
]

from logic.system import ServiceRequestDebugException

# ======================# WRONG_ARGUMENT_NAME_EXCEPTION #======================#
class ArgumentNameException(ServiceRequestDebugException):
    """
    Role:Information, Reporting, Debug

    Responsibilities:
    1.  Indicate that a service_request has a wrong argument for the command.
    
    Super Class:
        *  ServiceRequestDebugException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See ServiceRequestDebugException class for inherited attributes.

    Attributes:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    ERR_CODE = "WRONG_ARGUMENT_NAME_EXCEPTION"
    MSG = "Argument name incorrect."
    
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