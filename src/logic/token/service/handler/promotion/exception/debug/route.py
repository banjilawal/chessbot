# src/logic/token/service/handler/promotion/exception/debug/route.py

"""
Module: logic.token.service.handler.promotion.exception.debug.route
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

from logic.token import TokenDebugException


# ======================# NO_PROMOTION_ROUTE_TO_NEW_RANK_EXCEPTION #======================#
class PawnPromotionRouteException(TokenDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate that a pawn could not be promoted because, there was no routing logic to
        the new route.

    # PARENT:
        *   TokenDebugException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   TokenDebugException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
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
    VAR = Optional[str]
    VAL = Optional[Any]
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
        var = var or self.VAR
        val = val or self.VAL
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)
