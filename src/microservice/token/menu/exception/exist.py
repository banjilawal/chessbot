# src/logic/token/service/menu/exception/debug.py

"""
Module: logic.token.service.menu.exception.debug
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# TOKEN_COMMAND_NOT_FOUND_EXCEPTION #======================#
    "TokenCommandDebugException",
]

from command import TokenCommandDebugException


# ======================# TOKEN_COMMAND_NOT_FOUND_EXCEPTION #======================#
class TokenCommandNotFoundException(TokenCommandDebugException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that the Command does not exist in the TokenCommand set.
        
    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        
    Provides:
    
    Super Class:
        TokenCommandDebugException
    """
    ERR_CODE = "TOKEN_COMMAND_NOT_FOUND_EXCEPTION"
    MSG = "Command not found in the TokenCommand set."
    
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
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
        )

