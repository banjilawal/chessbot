# src/logic/coord/database/kernel/operation/crud/exception/pop/empty.py

"""
Module: logic.coord.database.kernel.operation.crud.exception.pop.empty
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# POPPING_EMPTY_COORD_STACK EXCEPTION #======================#
    "PoppingEmtpyCoordStackException",
]

from logic.system import DebugException


# ======================# POPPING_EMPTY_COORD_STACK EXCEPTION #======================#
class PoppingEmtpyCoordStackException(DebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate popping a CoordStack failed because the stack was empty.

    Super Class:
        *   DebugException

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
    MSG = "Cannot pop an empty CoordStack."
    ERR_CODE = "POPPING_EMPTY_COORD_STACK EXCEPTION"
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            msg: Optional[str] = None,
            err_code: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        """
        Args:
            var: Optional[str]
            val: Optional[Any]
            msg: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)
 