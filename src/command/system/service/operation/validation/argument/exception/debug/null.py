# src/command/request/validation/exception/debug/null.py

"""
Module: command.request.validation.exception.debug.null
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# NULL_ARGUMENTS_EXCEPTION #======================#
    "NullArgumentsException",
]

from system import NullException

# ======================# NULL_ARGUMENTS_EXCEPTION #======================#
class NullArgumentsException(NullException):
    """
    Role:Information, Reporting, Debug

    Responsibilities:
    1.  Indicate that a request.arguments dictionary does not exist.

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
    ERR_CODE = "NULL_ARGUMENTS_EXCEPTION"
    MSG = "Null arguments"
    
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