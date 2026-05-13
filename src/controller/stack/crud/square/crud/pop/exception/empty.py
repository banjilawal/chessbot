# src/logic/square/database/kernel/operation/crud/pop/exception/empty.py

"""
Module: logic.square.database.kernel.operation.crud.pop.exception.empty
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# POPPING_EMPTY_SQUARE_STACK_EXCEPTION #======================#
    "PoppingEmptySquareStackException",
]

from system import DebugException


# ======================# POPPING_EMPTY_SQUARE_STACK_EXCEPTION #======================#
class PoppingEmptySquareStackException(DebugException):
    """
    Role:
        -    Error Variable Identifier
        -   Exception Chain Layer 2,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a pop failed because the schema was empty.
        
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
    ERR_CODE = "POPPING_EMPTY_SQUARE_STACK_EXCEPTION"
    MSG = "SquareStackService pop failed: Cannot pop from an empty schema."
    
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

