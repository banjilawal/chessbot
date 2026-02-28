# src/chess/square/service/command/build/exception/anchor.py

"""
Module: chess.square.service.command.build.exception.anchor
Author: Banji Lawal
Created: 2026-02-24
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_BUILD_COMMAND EXCEPTION #======================#
    "SquareBuildCommandPipeline",
]

from chess.system import AnchorException


# ======================# SQUARE_BUILD_COMMAND EXCEPTION #======================#
class SquareBuildCommandPipeline(AnchorException):
    """
    # ROLE: Debug Coverage Target, Exception Chain Layer 0
    
    # RESPONSIBILITIES:
    1.  Layer-0 of Exception chain which is the Parent of ServiceCommandDebugException
    
    # PARENT:
      *   CommandException
    
    # PROVIDES:
    None
    
    # ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_BUILD_COMMAND_EXCEPTION"
    MSG = "SquareBuildCommandPipeline raised an exception."
    CLS_NAME = "SquareBuildCommandPipeline"
    
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
