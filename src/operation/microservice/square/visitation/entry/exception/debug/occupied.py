# src/logic/square/service/visitation/entry/exception/debug/full.py

"""
Module: logic.square.service.visitation.entry.exception.debug.full
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# VISITING_OCCUPIED_SQUARE EXCEPTION #======================#
    "SquareOccupiedException",
]

from logic.square import SquareDebugException


# ======================# VISITING_OCCUPIED_SQUARE EXCEPTION #======================#
class SquareOccupiedException(SquareDebugException):
    """
    Role:
        -   Error Variable Identifier
        -   Exception Chain Layer 2
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a square entry failed the square was already occupied

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
    ERR_CODE = "VISITING_OCCUPIED_SQUARE_EXCEPTION"
    MSG = "The square is already occupied."
    
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
