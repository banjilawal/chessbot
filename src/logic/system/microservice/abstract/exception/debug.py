# src/logic/system/microservice/abstract/exception/debug.py

"""
Module: logic.system.microservice.abstract.exception.debug
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SERVICE_DEBUG_EXCEPTION #======================#
    "ServiceDebugException",
]

from logic.system import DebugException


# ======================# SERVICE_DEBUG_EXCEPTION #======================#
class ServiceDebugException(DebugException):
    """
    Role:Information, Reporting, Debug

    Responsibilities:
    1.  Parent of DebugExceptions pertinent to MicroService instances.

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
    ERR_CODE = "SERVICE_DEBUG_EXCEPTION"
    MSG = "MicroService attribute raised an exception."
    
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