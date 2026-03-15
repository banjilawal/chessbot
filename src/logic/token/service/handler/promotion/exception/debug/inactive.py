# src/logic/token/service/handler/promotion/exception/debug/pawn.py

"""
Module: logic.token.service.handler.promotion.exception.debug.pawn
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

from logic.token import TokenDebugException


# ======================# CANNOT_PROMOTE_INACTIVE_PAWN_EXCEPTION  #======================#
class PromoteInactivePawnException(TokenDebugException):
    """
    # ROLE: Error Variable Identifier, Exception Chain Layer 2, Exception Messaging

    # RESPONSIBILITIES:
    1.  Indicate that an inactive PawnToken cannot be promoted.

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
    ERR_CODE = "CANNOT_PROMOTE_INACTIVE_PAWN_EXCEPTION"
    MSG = "An inactive pawn cannot be promoted."
    
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