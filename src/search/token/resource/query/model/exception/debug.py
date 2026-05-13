# src/logic/token/database/search/token/model/exception/queryDebug/__init__.py

"""
Module: logic.token.database.search.token.model.exception.queryDebug.__init__
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# TOKEN_QUERY_DEBUG_EXCEPTION #======================#
    "TokenQueryDebugException",
]

from system import QueryDebugException

# ======================# TOKEN_QUERY_DEBUG_EXCEPTION #======================#
class TokenQueryDebugException(QueryDebugException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   QueryDebugging Metadata provider

    Responsibilities:
        1.  Record the condition that fired a Token variable's error state.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        QueryDebugException
    """
    ERR_CODE = "TOKEN_QUERY_DEBUG_EXCEPTION"
    MSG = "Token had an error."
    
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
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
        )


