# src/logic/system/search/resource/context/exception/debug/null.py

"""
Module: logic.system.search.resource.context.exception.debug.null
Author: Banji Lawal
Created: 2026-04-01
Version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

_all_ = [
    # ======================# NULL_CONTEXT_EXCEPTION #======================#
    "NullContextException",
]

from logic.system import NullException


# ======================# NULL_CONTEXT_EXCEPTION #======================#
class NullContextException(NullException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that null was received instead of a Context.

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
    MSG = str = "Context cannot be null."
    ERR_CODE = "NULL_CONTEXT_EXCEPTION"
    
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