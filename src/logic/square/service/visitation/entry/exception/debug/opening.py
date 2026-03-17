# src/logic/square/service/visitation/entry/exception/debug/opening.py

"""
Module: logic.square.service.visitation.entry.exception.debug.opening
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# WRONG_OPENING_SQUARE_EXCEPTION #======================#
    "WrongOpeningSquareException",
]

from logic.square import SquareDebugException


# ======================# WRONG_OPENING_SQUARE_EXCEPTION #======================#
class WrongOpeningSquareException(SquareDebugException):
    """
    Role:
        -   Error Variable Identifier
        -   Exception Chain Layer 2
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a square entry failed because a token tried deploying to the
            wrong opening square.

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
    ERR_CODE = "WRONG_OPENING_SQUARE_EXCEPTION"
    MSG = "Token deployed to wrong square"
    
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
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)