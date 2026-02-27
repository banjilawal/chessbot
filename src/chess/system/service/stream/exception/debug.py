# src/chess/system/service/stream/exception/debug.py

"""
Module: chess.system.service.stream.exception.debug
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SERVICE_STREAM_DEBUG_EXCEPTION #======================#
    "ServiceStreamDebugException",
]

from chess.system import DebugException


# ======================# SERVICE_STREAM_DEBUG_EXCEPTION #======================#
class ServiceStreamDebugException(DebugException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Parent of DebugExceptions pertinent to ServiceStream instances.

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
        *   val Optional[None])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    ERR_CODE = "SERVICE_STREAM_DEBUG_EXCEPTION"
    MSG = "ServiceStream attribute raised an exception."
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