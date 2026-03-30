# src/logic/token/query/route/model/exception/debug/missing.py
"""
Module: logic.token.query.route.model.exception.debug.missing
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# MISSING_TOKEN_SEARCH_ROUTE_EXCEPTION #======================#
    "MissingTokenSearchRouteException",
]

from logic.token import TokenDebugException

# ======================# MISSING_TOKEN_SEARCH_ROUTE_EXCEPTION #======================#
class MissingTokenSearchRouteException(TokenDebugException):
    """
    Role:
        -   Error Variable Identifier
        -   Exception Chain Layer 2,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that there was no search logic for a token attribute.

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
    ERR_CODE = "MISSING_TOKEN_SEARCH_ROUTE_EXCEPTION"
    MSG = "There is no search logic for the token attribute."
    
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
        super().__init__(
            ex=ex,
            var=var,
            val=val,
            msg=msg,
            err_code=err_code,
        )
