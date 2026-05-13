# src/command/service/adt/command/exception/debug.py

"""
Module: command.service.adt.command.exception.debug
Author: Banji Lawal
Created: 2026-02-24
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# COMMAND_DEBUG_EXCEPTION #======================#
    "CommandDebugException",
]

from system import DebugException


# ======================# COMMAND_DEBUG_EXCEPTION #======================#
class CommandDebugException(DebugException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Record the condition that fired a variable's error state. a Command instance into its  error state.
        2.  Parent of all debugging metadata providers who must report to Command instances.

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
    ERR_CODE = "COMMAND_DEBUG_EXECUTION"
    MSG = "Command fired into error state by attribute or method."
    
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
