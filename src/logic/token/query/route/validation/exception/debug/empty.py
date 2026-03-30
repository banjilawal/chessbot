# src/logic/token/query/route/validation/exception/debug/empty.py

"""
Module: logic.token.query.route.validation.exception.debug.empty
Author: Banji Lawal
Created: 2025-10-06
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
#======================# EMPTY_TOKEN_DATASET_EXCEPTION #======================#
    "EmptyTokenDatasetException",
]

from logic.token import TokenDebugException

#======================# EMPTY_TOKEN_DATASET_EXCEPTION #======================#
class EmptyTokenDatasetException(TokenDebugException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that a token dataset is empty where is required to contain items.

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
    MSG = "Token dataset cannot be empty"
    ERR_CODE = "EMPTY_TOKEN_DATASET_EXCEPTION"

    
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
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val,)


    





