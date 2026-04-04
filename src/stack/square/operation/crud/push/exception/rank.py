# src/logic/square/database/kernel/operation/crud/push/exception/rank.py

"""
Module: logic.square.database.kernel.operation.crud.push.exception.rank
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# NO_OPENINGS_FOR_RANK_EXCEPTION #======================#
    "SquareStackCapacityFullException",
]

from logic.square import SquareDebugException


# ======================# NO_OPENINGS_FOR_RANK_EXCEPTION #======================#
class SquareStackCapacityFullException(SquareDebugException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate that pushing a square to the schema failed because there were no
            openings for the square's rank.
        
    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        
    Provides:
    
    Super Class:
        *   SquareSquareDebugException
    """
    ERR_CODE = "NO_OPENINGS_FOR_RANK_EXCEPTION"
    MSG = "Pushing square failed: There were no openings for the square's rank."
    
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