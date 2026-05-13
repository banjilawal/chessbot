# system/command/system/serviceexception/debug.py

"""
Module: src.command.root.system.service.exception.debug
Author: Banji Lawal
Created: 2026-02-25
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# COMMAND_SERVICE_DEBUG_EXCEPTION #======================#
    "CommandServiceDebugException",
]

from system import DebugException


# ======================# COMMAND_SERVICE_DEBUG_EXCEPTION #======================#
class CommandServiceDebugException(DebugException):
    """
    Role:Information, Reporting, Debug

    Responsibilities:
    1.  Parent of DebugExceptions pertinent to CommandService instances.

    Super Class:
        *  DebugException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See DebugException class for inherited attributes.

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
    ERR_CODE = "COMMAND_SERVICE_DEBUG_EXCEPTION"
    MSG = "CommandService attribute raised an exception."
    
    def __init__(
            self,
            err_code: Optional[str] | None = None,
            msg: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)