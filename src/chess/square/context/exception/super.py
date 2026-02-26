# src/chess/square/context/exception/debug.py

"""
Module: chess.square.context.exception.debug
Author: Banji Lawal
Created: 2026-02-23
version: 1.0.0
"""

__all__ = [
    # ======================# SQUARE_CONTEXT EXCEPTION #======================#
    "SquareContextException",
]

from typing import Optional

from chess.system import SuperClassException


# ======================# SQUARE_CONTEXT EXCEPTION #======================#
class SquareContextException(SuperClassException):
    """
    # ROLE: DebugException Parent, Exception Chain Layer 0

    # RESPONSIBILITIES:
    Layer-0 of Exception chain which is the Parent of SquareContextDebugException

    # PARENT:
        *   SuperClassException

    # PROVIDES:
    None

    # ATTRIBUTES:
    None
    """
    ERR_CODE = "SQUARE_CONTEXT_ERROR"
    MSG = "SquareContext raised an exception."
    CLS_NAME = "SquareContext"
    
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
        
        super().__init__(msg=msg, err_code=err_code, ex=ex)
        _cls_name = cls_name
    
    
    @property
    def cls_name(self) -> Optional[str]:
        return self._cls_name
    
    
    def __str__(self):
        return f"{super().__str__()}, cls_name:{self._cls_name}"