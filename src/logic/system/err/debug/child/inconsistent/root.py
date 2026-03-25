# src/logic//service/handler/promotion/exception/debug/double.py

"""
Module: logic.service.handler.promotion.exception.debug.double
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# INCONSISTENT_STATE_EXCEPTION #======================#
    "InconsistentStateException",
]

from logic.system import DebugException


# ======================# INCONSISTENT_STATE_EXCEPTION #======================#
class InconsistentStateException(DebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate that an object's data does not reflect the changes made during
        the successful update.

    Super Class:
        *   DebugException

    Provides:


    # INHERITED ATTRIBUTES:
        *   DebugException class for inherited attributes.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See DebugException class for inherited methods.
    """
    ERR_CODE = "INCONSISTENT_STATE_EXCEPTION"
    MSG = "The data does not reflect the changes made during the successful update."
    
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
