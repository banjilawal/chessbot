# src/logic/token/database/searcher/context/service/operation/validation/exception/debug/null.py

"""
Module: logic.token.database.searcher.context.service.operation.validation.exception.debug.null
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

__all__ = [
    # ======================# TOKEN_QUERY_NULL_EXCEPTION #======================#
    "TokenQueryNullException",
]

from typing import Any, Optional

from system import NullException


# ======================# TOKEN_QUERY_NULL_EXCEPTION #======================#
class TokenQueryNullException(NullException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that a client got null instead of a List[Token].

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        NullException
    """
    MSG = "TokenQuery cannot be null."
    ERR_CODE = "TOKEN_QUERY_NULL_EXCEPTION"
    
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