# src/logic/token/database/core/handler/crud/exception/pop/empty.py

"""
Module: logic.token.database.core.handler.crud.exception.pop.empty
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
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate that a pop failed because the stack was empty.

    # PARENT:
        *   TokenDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   TokenDebugException class for inherited attributes.

    # CONSTRUCTOR:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See TokenDebugException class for inherited methods.
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
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)

