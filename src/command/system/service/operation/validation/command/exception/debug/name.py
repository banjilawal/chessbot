# src/command/request/validation/exception/debug/null.py

"""
Module: command.request.validation.exception.debug.null
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# COMMAND_NAME_NOT_FOUND_EXCEPTION #======================#
    "CommandNameNotFoundException",
]

from command import CommandDebugException


# ======================# COMMAND_NAME_NOT_FOUND_EXCEPTION #======================#
class CommandNameNotFoundException(CommandDebugException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that the Command's stack is not found in the CommandTable.

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
    ERR_CODE = "COMMAND_NAME_NOT_FOUND_EXCEPTION"
    MSG = str = "Command not found."
    
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