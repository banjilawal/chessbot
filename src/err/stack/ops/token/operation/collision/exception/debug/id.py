# src/logic/token/database/kernel/operation/collision/exception/debug/id.py

"""
Module: logic.token.database.kernel.operation.collision.exception.debug.id
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# TOKEN_ID_COLLISION EXCEPTION #======================#
    "TokenIdCollisionException",
]

from model.token import TokenDebugException

# ======================# TOKEN_ID_COLLISION EXCEPTION #======================#
class TokenIdCollisionException(TokenDebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate that two tokens share an id instead of having one of their own.

    Super Class:
        *   TokenDebugException

    Provides:


    # INHERITED ATTRIBUTES:
        *   TokenDebugException class for inherited attributes.

    Attributes:
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
    ERR_CODE = "TOKEN_ID_COLLISION EXCEPTION"
    MSG = "Id has already been assigned."
    
    def __init__(
            self,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            err_code: Optional[str] | None = None,
            msg: Optional[str] | None = None,
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
