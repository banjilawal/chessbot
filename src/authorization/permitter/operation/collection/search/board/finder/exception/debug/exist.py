# src/logic/board/context/route/exception/debug/exist.py

"""
Module: logic.board.context.route.exception.debug.exist
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# BOARD_NOT_FOUND_EXCEPTION #======================#
    "BoardNotFoundException",
]

from logic.board import BoardDebugException


# ======================# BOARD_NOT_FOUND_EXCEPTION #======================#
class BoardNotFoundException(BoardDebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate that no board was found.

    Super Class:
        *   BoardDebugException

    Provides:


    # INHERITED ATTRIBUTES:
        *   BoardDebugException class for inherited attributes.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See BoardDebugException class for inherited methods.
    """
    ERR_CODE = "BOARD_NOT_FOUND_EXCEPTION"
    MSG = "No board matching the attribute was found."
    
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
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)