# src/command/request/validator/exception/debug/count.py

"""
Module: command.request.validator.exception.debug.count
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# ARGUMENT_COUNT_EXCEPTION #======================#
    "ArgumentCountException",
]

from logic.system import ServiceRequestDebugException


# ======================# ARGUMENT_COUNT_EXCEPTION #======================#
class ArgumentCountException(ServiceRequestDebugException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Indicate that a service_request has the wrong number of arguments for the command

    # PARENT:
        *  ServiceRequestDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See ServiceRequestDebugException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val (Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    ERR_CODE = "ARGUMENT_COUNT_EXCEPTION"
    MSG = "Incorrect number of arguments."
    VAR = Optional[str]
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
