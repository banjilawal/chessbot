# src/chess/system/service/request/exception/debug.py

"""
Module: chess.system.service.request.exception.debug
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SERVICE_REQUEST_DEBUG EXCEPTION #======================#
    "ServiceRequestDebugException",
]

from chess.system import DebugException


# ======================# SERVICE_REQUEST_DEBUG EXCEPTION #======================#
class ServiceRequestDebugException(DebugException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Parent of DebugExceptions related to a Debug instance's state.

    # PARENT:
        *   DebugException

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
        *   val Optional[None])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    ERR_CODE = "SERVICE_REQUEST_DEBUG_ERROR"
    MSG = "A ServiceRequest attribute raised an exception."
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
