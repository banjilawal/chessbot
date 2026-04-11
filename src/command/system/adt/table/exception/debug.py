# src/command/service/adt/table/exception/debug.py

"""
Module: command.service.adt.table.exception.debug
Author: Banji Lawal
Created: 2026-02-24
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# COMMAND_ARGS_DEBUG_EXCEPTION #======================#
    "CommandArgsDebugException",
]

from system import DebugException


# ======================# COMMAND_ARGS_DEBUG_EXCEPTION #======================#
class CommandArgsDebugException(DebugException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Record the condition that fired a variable's error state. a CommandArgs instance into its  error state.
        2.  Parent of all debugging metadata providers who must report to CommandArgs instances.

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
    ERR_CODE = "COMMAND_ARGS_DEBUG_EXECUTION"
    MSG = "CommandArgs fired into error state by attribute or method."
    
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
