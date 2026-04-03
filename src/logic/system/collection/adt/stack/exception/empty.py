# src/logic/system/collection/adt/stack/exception/empty.py

"""
Module: logic.system.collection.adt.stack.exception.empty
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# POPPING_EMPTY_STACK_EXCEPTION #======================#
    "PoppingEmptyStackException",
]

from logic.system import StackServiceDebugException


# ======================# POPPING_EMPTY_STACK_EXCEPTION #======================#
class PoppingEmptyStackException(StackServiceDebugException):
    """
    Role:
        -   Error Variable Identifier
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
        DebugException

    """
    ERR_CODE = "POPPING_EMPTY_STACK_EXCEPTION"
    MSG = "Cannot pop from an empty stack."
    
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

