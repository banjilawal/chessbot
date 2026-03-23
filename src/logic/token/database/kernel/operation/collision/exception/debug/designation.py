# src/logic/token/database/kernel/operation/collision/exception/debug/designation.py

"""
Module: logic.token.database.kernel.operation.collision.exception.debug.designation
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# TOKEN_DESIGNATION_COLLISION EXCEPTION #======================#
    "TokenDesignationCollisionException",
]

from logic.token import TokenDebugException


# ======================# TOKEN_DESIGNATION_COLLISION EXCEPTION #======================#
class TokenDesignationCollisionException(TokenDebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate that two tokens share a designation instead of having one of their own.

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
    ERR_CODE = "TOKEN_DESIGNATION_COLLISION EXCEPTION"
    MSG = "Designation has already been assigned."
    
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