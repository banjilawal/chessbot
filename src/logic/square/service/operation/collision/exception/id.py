# src/logic/square/service/operation/collision/exception/debug/id.py

"""
Module: logic.square.service.operation.collision.exception.debug.id
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SQUARE_ID_COLLISION EXCEPTION #======================#
    "SquareIdCollisionException",
]

from logic.square import SquareDebugException

# ======================# SQUARE_ID_COLLISION EXCEPTION #======================#
class SquareIdCollisionException(SquareDebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate that two squares share an id instead of having one of their own.

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
    ERR_CODE = "SQUARE_ID_COLLISION EXCEPTION"
    MSG = "Id has already been assigned."
    
    def __init__(
            self,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
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
