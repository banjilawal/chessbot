# src/chess/square/service/command/exception/super.py

"""
Module: chess.square.service.command.exception.super
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_BUILD_COMMAND EXCEPTION #======================#
    "SquareBuildCommand",
]

from chess.system import SuperClassException


# ======================# SQUARE_BUILD_COMMAND EXCEPTION #======================#
class SquareBuildCommand(SuperClassException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0
    
    # RESPONSIBILITIES:
    1.  Layer-0 of Exception chain which is the Parent of ServiceCommandDebugException
    
    # PARENT:
      *   CommandException
    
    # PROVIDES:
    None
    
    # ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_BUILD_COMMAND_ERROR"
    MSG = "SquareBuildCommand raised an exception."
    CLS_NAME = "SquareBuildCommand"
    
    _cls_name: Optional[str]
    
    def __init__(
            self,
            cls_name: Optional[str] = None,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
    ):
        cls_name = cls_name or self.CLS_NAME
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        
        super().__init__(msg=msg, err_code=err_code, ex=ex, cls_name=cls_name)
