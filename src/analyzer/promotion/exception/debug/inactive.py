# src/logic/token/service/operation/promotion/exception/debug/pawn_token.py

"""
Module: logic.token.service.operation.promotion.exception.debug.pawn_token
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# CANNOT_PROMOTE_INACTIVE_PAWN_EXCEPTION  #======================#
    "PromoteInactivePawnException",
]

from model.token import TokenDebugException


# ======================# CANNOT_PROMOTE_INACTIVE_PAWN_EXCEPTION  #======================#
class PromoteInactivePawnException(TokenDebugException):
    """
        -   Error Variable Identifier
        -   Exception Chain Layer 2
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that an inactive PawnToken cannot be promoted.
    
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
    MSG = "An inactive pawn_token cannot be promoted."
    ERR_CODE = "CANNOT_PROMOTE_INACTIVE_PAWN_EXCEPTION"
    
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