# src/logic/schema/database/search/service/exception/exist.py

"""
Module: logic.schema.database.search.service.exception.exist
Author: Banji Lawal
Created: 2025-10-01
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# SCHEMA_NOT_FOUND_EXCEPTION #======================#
    "SchemaNotFoundException",
]

from logic.schema import SchemaDebugException

# ======================# SCHEMA_NOT_FOUND_EXCEPTION #======================#
class SchemaNotFoundException(SchemaDebugException):
    """
    Role:
        -   Exception Chain Layer 0
        -   Exception coverage target
    
    Responsibilities:
        1.  Indicate that no schema was found.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
    
    Provides
    
    Super Class:
        SchemaDebugException
    """
    ERR_CODE = "SCHEMA_NOT_FOUND_EXCEPTION"
    MSG = "No schema matching the attribute was found."
    
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
        super().__init__(msg=msg, err_code=err_code, ex=ex, var=var, val=val)