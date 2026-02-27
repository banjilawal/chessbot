# src/chess/system/service/command/exception/super.py

"""
Module: chess.system.service.command.exception.super
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations

__all__ = [
    # ======================# SERVICE_COMMAND EXCEPTION #======================#
    "CommandException",
]

from typing import Optional
from chess.system import AnchorException


# ======================# SERVICE_COMMAND EXCEPTION #======================#
class CommandException(AnchorException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    1.  Layer-0 of Exception chain which is the Parent of CommandDebugException

    # PARENT:
      *   AnchorException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "SERVICE_COMMAND_ERROR"
    MSG = "Command raised an exception."
    CLS_NAME = "Command"
    
    def __init__(
            self,
            cls_name: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        cls_name = cls_name or self.__class__.__name__
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        
        super().__init__(msg=msg, err_code=err_code, ex=ex)
        _cls_name = cls_name
    
    @property
    def cls_name(self) -> Optional[str]:
        return self._cls_name
    
    def __str__(self):
        return f"{super().__str__()}, cls_name:{self._cls_name}"