# src/logic/schema/database/search/context/service/operation/validation/exception/debug/zero.py

"""
Module: logic.schema.database.search.context.service.operation.validation.exception.debug.zero
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# ZERO_SCHEMA_CONTEXT_FLAGS_EXCEPTION #======================#
    "ZeroSchemaContextFlagsException",
]

from system import ZeroContextFlagsException


# ======================# ZERO_SCHEMA_CONTEXT_FLAGS_EXCEPTION #======================#
class ZeroSchemaContextFlagsException(ZeroContextFlagsException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that no SchemaContext work was not completed because
            no attribute was enabled.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        ZeroContextFlagsException
    """
    MSG = "No SchemaContext flags are enabled."
    ERR_CODE = "ZERO_SCHEMA_CONTEXT_FLAGS_EXCEPTION"
    
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