# src/chess/system/service/abstract/exception/debug.py

"""
Module: chess.system.service.abstract.exception.debug
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SERVICE_DEBUG_EXCEPTION #======================#
    "ServiceDebugException",
]

from chess.system import DebugException


# ======================# SERVICE_DEBUG_EXCEPTION #======================#
class ServiceDebugException(DebugException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Parent of DebugExceptions pertinent to Service instances.

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
    ERR_CODE = "SERVICE_DEBUG_EXCEPTION"
    MSG = "Service attribute raised an exception."
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