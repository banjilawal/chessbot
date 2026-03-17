# src/command/command/menu/exception/debug.py

"""
Module: command.command.menu.exception.debug
Author: Banji Lawal
Created: 2026-02-25
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SERVICE_MENU_DEBUG_EXCEPTION #======================#
    "ServiceMenuDebugException",
]

from logic.system import DebugException


# ======================# SERVICE_MENU_DEBUG_EXCEPTION #======================#
class ServiceMenuDebugException(DebugException):
    """
    Role:Information, Reporting, Debug

    Responsibilities:
    1.  Parent of DebugExceptions pertinent to ServiceMenu instances.

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
    ERR_CODE = "SERVICE_MENU_DEBUG_EXCEPTION"
    MSG = "ServiceMenu attribute raised an exception."
    
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