# src/logic/square/service/visitation/exception/terminate/empty.py

"""
Module: logic.square.service.visitation.exception.terminate.empty
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# DEPARTING_EMPTY_SQUARE_EXCEPTION #======================#
    "DepartingEmptySquareException",
]

from logic.square import SquareDebugException


# ======================# DEPARTING_EMPTY_SQUARE_EXCEPTION #======================#
class DepartingEmptySquareException(SquareDebugException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate a SquareDeparture exception failed because the square was already empty.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        SquareDebugException
    """
    ERR_CODE = "DEPARTING_EMPTY_SQUARE_EXCEPTION"
    MSG = "SquareDeparture failed: Cannot reitinerary visitor from empty square."
    
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