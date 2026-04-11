# src/logic/schema/database/search/context/service/operation/validation/exception/flag/excess.py

"""
Module: logic.schema.validation.exception.flag.excess
Author: Banji Lawal
Created: 2025-09-16
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# EXCESS_SCHEMA_CONTEXT_FLAGS_EXCEPTION #======================#
    "ExcessSchemaContextFlagsException",
]

from system import  ExcessContextFlagsException


# ======================# EXCESS_SCHEMA_CONTEXT_FLAGS_EXCEPTION #======================#
class ExcessSchemaContextFlagsException(ExcessContextFlagsException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Indicate that no SchemaContext work was not completed
            because more than one attribute was enabled.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        ExcessContextFlagsException)
    """
    MSG = "Only one SchemaContex should be enabled."
    ERR_CODE = "EXCESS_SCHEMA_CONTEXT_FLAGS_EXCEPTION"
   
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