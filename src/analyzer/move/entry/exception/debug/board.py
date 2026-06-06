# src/logic/square/service/visitation/entry/exception/debug/board.py

"""
Module: logic.square.service.visitation.entry.exception.debug.board
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

___all__ = [
    # ======================# VISITOR_FROM_WRONG_BOARD EXCEPTION #======================#
    "SquareVisitorBoardException",
]

from logic.square import SquareDebugException


# ======================# VISITOR_FROM_WRONG_BOARD EXCEPTION #======================#
class SquareVisitorBoardException(SquareDebugException):
    """
    Role:
        -   Error Variable Identifier
        -   Exception Chain Layer 2
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a square entry failed because the visitor belonged to a different board.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        TokenDebugException
    """
    ERR_CODE = "VISITOR_FROM_WRONG_BOARD_EXCEPTION"
    MSG = "Entry denied. Visitor assigned to a different board."
    
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
