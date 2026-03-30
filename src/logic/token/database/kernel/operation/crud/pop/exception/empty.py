# src/logic/token/database/kernel/operation/crud/pop/exception/empty.py

"""
Module: logic.token.database.kernel.operation.crud.pop.exception.empty
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# POPPING_EMPTY_TOKEN_STACK_EXCEPTION #======================#
    "PoppingEmptyTokenStackException",
]

from logic.system import DebugException


# ======================# POPPING_EMPTY_TOKEN_STACK_EXCEPTION #======================#
class PoppingEmptyTokenStackException(DebugException):
    """
    Role:
        -    Error Variable Identifier
        -   Exception Chain Layer 2,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a pop failed because the stack was empty.
        
    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        
    Provides:

    Super Class:
        TokenDebugException

    """
    ERR_CODE = "POPPING_EMPTY_TOKEN_STACK_EXCEPTION"
    MSG = "TokenStackService pop failed: Cannot pop from an empty stack."
    
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
        super().__init__(
            ex=ex,
            var=var,
            val=val,
            msg=msg,
            err_code=err_code,
        )

