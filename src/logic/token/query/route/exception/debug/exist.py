# src/logic/token/query/route/exception/debug/exist.py

"""
Module: logic.token.query.route.exception.debug.exist
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# TOKEN_NOT_FOUND_EXCEPTION #======================#
    "TokenNotFoundException",
]

from logic.token import TokenDebugException


# ======================# TOKEN_NOT_FOUND_EXCEPTION #======================#
class TokenNotFoundException(TokenDebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate that no token was found.

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
    ERR_CODE = "TOKEN_NOT_FOUND_EXCEPTION"
    MSG = "No token matching the attribute was found."
    
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