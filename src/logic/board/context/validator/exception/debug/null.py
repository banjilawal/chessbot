# src/logic/board/context/validator/exception/debug/null.py

"""
Module: logic.board.context.validator.exception.debug.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# NULL_BOARD_CONTEXT_EXCEPTION #======================#
    "NullBoardContextException",
]

from logic.system import NullException

# ======================# NULL_BOARD_CONTEXT_EXCEPTION #======================#
class NullBoardContextException(NullException):
    """
    Role:Exception Chain Layer 2, Exception Messaging
    # TASK: Capture Error Variable State

    Responsibilities:
    1.  Produce the:
            *   variable,
            *   it's value,
            *   event which fired the variable into its error state.
        which occurred in the BoardContextValidator method identified in layer-0 of the exception chain.

    2.  A failing ValidationResult was returned because the candidate was null.

    Super Class:
        *   NullException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See NullException class for inherited attributes.

    Attributes:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   var (Optional[str])
        *   val (Optional[Any])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See NullException class for inherited methods.
    """
    MSG = "BoardContext cannot be null."
    ERR_CODE = "NULL_BOARD_CONTEXT_EXCEPTION"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
    ):
        """
        Args:
            msg: str
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(ex=ex, msg=msg, err_code=err_code, var=var, val=val, )