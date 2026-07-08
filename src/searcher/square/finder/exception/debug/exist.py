# src/logic/square/context/route/exception/debug/exist.py

"""
Module: logic.square.context.route.exception.debug.exist
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SQUARE_NOT_FOUND_EXCEPTION #======================#
    "SquareNotFoundException",
]

from logic.square import SquareDebugException


# ======================# SQUARE_NOT_FOUND_EXCEPTION #======================#
class SquareNotFoundException(SquareDebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate that no square was found.

    Super Class:
        *   SquareDebugException

    Provides:


    # INHERITED ATTRIBUTES:
        *   SquareDebugException class for inherited attributes.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See SquareDebugException class for inherited methods.
    """
    ERR_CODE = "SQUARE_NOT_FOUND_EXCEPTION"
    MSG = "No square matching the attribute was found."
    
    def __init__(
            self,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            msg: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
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