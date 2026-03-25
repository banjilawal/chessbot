# src/logic/square/service/operation/collision/exception/debug/square.py

"""
Module: logic.square.service.operation.collision.exception.debug.square
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SQUARE_COORD_COLLISION_EXCEPTION #======================#
    "SquareCoordCollisionException",
]

from logic.square import SquareDebugException

# ======================# SQUARE_COORD_COLLISION_EXCEPTION #======================#
class SquareCoordCollisionException(SquareDebugException):
    """
    Role:
        -   Error Variable Identifier
        -   Exception Chain Layer 2, 
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that two squares share a coord instead of having one of their own.
        
    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        SquareDebugException
    """
    ERR_CODE = "SQUARE_COORD_COLLISION_EXCEPTION"
    MSG = "Another Square is using that coord"
    
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
