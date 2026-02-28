# src/chess/system/service/request/validator/exception/debug/null.py

"""
Module: chess.system.service.request.validator.exception.debug.null
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# NULL_ARGUMENTS_EXCEPTION #======================#
    "NullArgumentsException",
]

from chess.system import NullException

# ======================# NULL_ARGUMENTS_EXCEPTION #======================#
class NullArgumentsException(NullException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Indicate that a request.arguments dictionary does not exist.

    # PARENT:
        *  NullException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See NullException class for inherited attributes.

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
    ERR_CODE = "NULL_ARGUMENTS_EXCEPTION"
    MSG = "Null arguments"
    VAR = Optional[Any]
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