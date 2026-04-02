# src/logic/system/search/resource/context/exception/debug.py

"""
Module: logic.system.search.resource.context.exception.debug
Author: Banji Lawal
Created: 2026-04-01
Version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# QUERY_DEBUG_EXCEPTION #======================#
    "QueryDebugException",
]

from logic.system import DebugException

# ======================# QUERY_DEBUG_EXCEPTION #======================#
class QueryDebugException(DebugException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Record the condition that fired a Query variable's error state.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        DebugException
    """
    ERR_CODE = "QUERY_EXCEPTION"
    MSG = str = "Query had an error."
    
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
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
        )


