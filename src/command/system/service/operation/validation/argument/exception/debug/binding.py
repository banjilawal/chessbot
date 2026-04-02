# src/command/request/validation/exception/debug/null.py

"""
Module: command.request.validation.exception.debug.null
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# ARGUMENT_NAME_TYPE_MISMATCH_EXCEPTION #======================#
    "ArgumentNameTypeBindingException",
]

from typing import Optional

from logic.system import ServiceRequestDebugException

# ======================# ARGUMENT_NAME_TYPE_MISMATCH_EXCEPTION #======================#
class ArgumentNameTypeBindingException(ServiceRequestDebugException):
    """
    Role:Information, Reporting, Debug

    Responsibilities:
    1.  Indicate that there is a mismatch between a parameter's stack and its type.

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
    ERR_CODE = "ARGUMENT_NAME_TYPE_MISMATCH_EXCEPTION"
    MSG = "Discrepancy in (identifier, type) tuple."
    
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

