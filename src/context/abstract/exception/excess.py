# src/context/abstract/exception/excess.py

"""
Module: context.abstract.exception.excess
Author: Banji Lawal
Created: 2026-04-03
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from context import ContextException

_all_ = [
    # ======================# EXCESS_CONTEXT_FLAGS_EXCEPTION #======================#
    "ExcessContextFlagsException",
]

# ======================# EXCESS_CONTEXT_FLAGS_EXCEPTION #======================#
class ExcessContextFlagsException(ContextException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that the work was not completed because too many context
            attributes was enabled.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        ContextException
    """
    MSG = str = "Too many context attributes enabled."
    ERR_CODE = "EXCESS_CONTEXT_FLAGS_EXCEPTION"
   
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