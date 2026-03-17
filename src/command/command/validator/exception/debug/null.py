# src/command/request/validator/exception/debug/null.py

"""
Module: command.request.validator.exception.debug.null
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# NULL_COMMAND_EXCEPTION #======================#
    "NullCommandException",
]

from logic.system import NullException

# ======================# NULL_COMMAND_EXCEPTION #======================#
class NullCommandException(NullException):
    """
    Role:Information, Reporting, Debug

    Responsibilities:
    1.  Indicate that a Command is null.

    Super Class:
        *  NullException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See NullException class for inherited attributes.

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
    ERR_CODE = "NULL_COMMAND_EXCEPTION"
    MSG = "Command is null"
    
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