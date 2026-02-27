# src/chess/system/service/request/validator/exception/debug/identifier.py

"""
Module: chess.system.service.request.validator.exception.debug.identifier
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# UNKNOWN_ARGUMENT_EXCEPTION #======================#
    "ArgumentNameException",
]

from chess.system import ServiceRequestDebugException

# ======================# UNKNOWN_ARGUMENT_EXCEPTION #======================#
class ArgumentNameException(ServiceRequestDebugException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Indicate that a service_request has a wrong argument for the command.
    
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
    ERR_CODE = "UNKNOWN_ARGUMENT_EXCEPTION"
    MSG = "unknown command argument"
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