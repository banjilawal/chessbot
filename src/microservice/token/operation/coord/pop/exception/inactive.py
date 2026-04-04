# src/logic/token/service/operation/promotion/exception/debug/token.py

"""
Module: logic.token.service.operation.promotion.exception.debug.token
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# INACTIVE_TOKEN_UNDO_COORD_POP_EXCEPTION  #======================#
    "InactiveTokenPoppingCoordException",
]

from model.token import TokenDebugException


# ======================# INACTIVE_TOKEN_UNDO_COORD_POP_EXCEPTION  #======================#
class InactiveTokenPoppingCoordException(TokenDebugException):
    """
    Role:
        -   Error Variable Identifier
        -   Exception Chain Layer 2
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that an inactive Token cannot undo its last move by popping its CoordStackService.
    
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
    ERR_CODE = "INACTIVE_TOKEN_UNDO_COORD_POP_EXCEPTION"
    MSG = "An inactive token cannot pop its CoordStackService."
    
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