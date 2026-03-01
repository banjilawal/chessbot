# src/command/command/exception/super.py

"""
Module: command.command.exception.super
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

__all__ = [
    # ======================# COMMAND_EXCEPTION #======================#
    "CommandException",
]

from typing import Optional
from chess.system import AnchorException


# ======================# COMMAND_EXCEPTION #======================#
class CommandException(AnchorException):
    """
    # ROLE: Debug Coverage Target, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Layer-0 of Exception chain which is the Parent of CommandDebugException

    # PARENT:
      *   AnchorException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "COMMAND_EXCEPTION"
    MSG = "Command raised an exception."
    CLS_NAME = "Command"
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
    ):
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        cls_name = cls_name or self.CLS_NAME
        super().__init__(
            ex=ex,
            msg=msg,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )