# src/logic/schema/database/search/query/service/operation/validation/exception/null.py

"""
Module: logic.schema.database.search.query.service.operation.validation.exception.null
Author: Banji Lawal
Created: 2025-10-03
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SCHEMA_STACK_NULL_EXCEPTION #======================#
    "SchemaStackNullException",
]

from logic.system import NullException

# ======================# SCHEMA_STACK_NULL_EXCEPTION #======================#
class SchemaStackNullException(NullException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that a client got null instead of a List[Schema].

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
    MSG = "SchemaStack cannot be null."
    ERR_CODE = "SCHEMA_STACK_NULL_EXCEPTION"

    
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


    





