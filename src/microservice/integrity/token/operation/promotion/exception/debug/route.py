# src/logic/token/service/operation/promotion/exception/debug/route.py

"""
Module: logic.token.service.operation.promotion.exception.debug.route
Author: Banji Lawal
Created: 2026-03-14
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# NO_PROMOTION_ROUTE_TO_NEW_RANK_EXCEPTION #======================#
    "PawnPromotionRouteException",
]

from model.token import TokenDebugException


# ======================# NO_PROMOTION_ROUTE_TO_NEW_RANK_EXCEPTION #======================#
class PawnPromotionRouteException(TokenDebugException):
    """
        -   Error Variable Identifier
        -   Exception Chain Layer 2
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that a pawn_token could not be promoted because, there was no routing logic to
            the new route.
        
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
    MSG = "No promotion route to the new rank."
    ERR_CODE = "NO_PROMOTION_ROUTE_TO_NEW_RANK_EXCEPTION"
    
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
