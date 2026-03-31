# src/command/token/exception/debug.py

"""
Module: command.token.exception.debug
Author: Banji Lawal
Created: 2026-02-24
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# TOKEN_COMMAND_DEBUG_EXCEPTION #======================#
    "TokenCommandDebugException",
]

from command import CommandDebugException


# ======================# TOKEN_COMMAND_DEBUG_EXCEPTION #======================#
class TokenCommandDebugException(CommandDebugException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Carry metadata about the variable that fired a TokenCommand instance into its error state.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        CommandDebugException
    """
    ERR_CODE = "TOKEN_COMMAND_DEBUG_EXCEPTION"
    MSG = "TokenCommand variable raised an exception."
    
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
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
        )
    

