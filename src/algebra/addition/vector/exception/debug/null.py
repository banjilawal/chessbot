# src/logic/vector/service/operation/validate/exception/debug/null.py

"""
Module: logic.vector.service.operation.validate.exception.debug.null
Author: Banji Lawal
Created: 2025-11-19
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# NULL_VECTOR_LIST_EXCEPTION #======================#
    "NullVectorListException",
]

from system import NullException


# ======================# NULL_VECTOR_LIST_EXCEPTION #======================#
class NullVectorListException(NullException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate that Vector addition failed because the list was null.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        NulException
    """
    MSG = "List cannot be null."
    ERR_CODE = "NULL_VECTOR_LIST_EXCEPTION"

    
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


    





