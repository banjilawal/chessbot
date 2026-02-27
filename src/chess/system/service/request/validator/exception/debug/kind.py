# src/chess/system/service/request/validator/exception/debug/null.py

"""
Module: chess.system.service.request.validator.exception.debug.null
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# WRONG_ARGUMENT_TYPE EXCEPTION #======================#
    "ArgumentTypeException",
]

from typing import Optional

from chess.system import ServiceRequestDebugException

# ======================# WRONG_ARGUMENT_TYPE EXCEPTION #======================#
class ArgumentTypeException(ServiceRequestDebugException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Indicate that a service_request argument has the wrong type.

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
        *   val Optional[None])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    ERR_CODE = "WRONG_ARGUMENT_TYPE_EXCEPTION"
    MSG = "service_request.arguments[identifier]: has wrong type"
    VAR = None
    VAL = None
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            var: Optional[str] = None,
            val: Optional[None] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        var = var or self.VAR
        val = val or self.VAL
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)

