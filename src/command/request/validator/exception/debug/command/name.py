# src/command/request/validator/exception/debug/command.py

"""
Module: command.request.validator.exception.debug.command
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# COMMAND_NAME_NOT_FOUND #======================#
    "CommandNameException",
]

from command import RequestDebugException


# ======================# COMMAND_NAME_NOT_FOUND #======================#
class CommandNameException(RequestDebugException):
    """
    Role:Information, Reporting, Debug

    Responsibilities:
    1.  Indicate that a service_request command_name has an error.

    Super Class:
        *  RequestDebugException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See RequestDebugException class for inherited attributes.

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
    ERR_CODE = "COMMAND_NAME_NOT_FOUND"
    MSG = "unknown command argument"
    
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