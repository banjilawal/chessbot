# system/command/command/serviceexception/debug.py

"""
Module: src.command.command.command.service.exception.debug
Author: Banji Lawal
Created: 2026-02-25
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# COMMAND_SERVICE_DEBUG_EXCEPTION #======================#
    "CommandServiceDebugException",
]

from logic.system import DebugException


# ======================# COMMAND_SERVICE_DEBUG_EXCEPTION #======================#
class CommandServiceDebugException(DebugException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Parent of DebugExceptions pertinent to CommandService instances.

    # PARENT:
        *  DebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
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
    ERR_CODE = "COMMAND_SERVICE_DEBUG_EXCEPTION"
    MSG = "CommandService attribute raised an exception."
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