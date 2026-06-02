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
    # ======================# CIRCULAR_PAWN_RANK_PROMOTION_EXCEPTION  #======================#
    "PromoteToPawnException",
]

from model.token import TokenDebugException


# ======================# CIRCULAR_PAWN_RANK_PROMOTION_EXCEPTION  #======================#
class PromoteToPawnException(TokenDebugException):
    """
    Role:Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
        -   Error Variable Identifier
        -   Exception Chain Layer 2
        -   Exception Messaging
    
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
    ERR_CODE = "CIRCULAR_PAWN_RANK_PROMOTION_EXCEPTION"
    MSG = "Cannot promote a pawn_token to be a pawn_token again."
    
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