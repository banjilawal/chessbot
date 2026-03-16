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

from logic.token import TokenDebugException


# ======================# CIRCULAR_PAWN_RANK_PROMOTION_EXCEPTION  #======================#
class PromoteToPawnException(TokenDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate that promoting a PawnToken failed because the new rank was still a Pawn's rank.

    # PARENT:
        *   TokenDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   TokenDebugException class for inherited attributes.

    # CONSTRUCTOR:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See TokenDebugException class for inherited methods.
    """
    ERR_CODE = "CIRCULAR_PAWN_RANK_PROMOTION_EXCEPTION"
    MSG = "Cannot promote a pawn_token to be a pawn_token again."
    
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
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)