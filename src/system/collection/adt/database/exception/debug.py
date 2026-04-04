# src/logic/system/collection/adt/database/exception/debug.py

"""
Module: logic.system.collection.adt.database.exception.debug
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# DATABASE_DEBUG_EXCEPTION #======================#
    "DatabaseDebugException",
]

from system import ServiceDebugException


# ======================# DATABASE_DEBUG_EXCEPTION #======================#
class DatabaseDebugException(ServiceDebugException):
    """
    Role:
        -   Exception Chain Layer 2
        -   Error Variable Identifier
        -   Debugging Metadata provider

    Responsibilities:
        1.  Record the condition that fired a Database variable's error state.
        
    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        
    Provides:
    
    Super Class:
        ServiceDebugException
    """
    ERR_CODE = "DATABASE_DEBUG_EXCEPTION"
    MSG = str = "Database fired into error state by attribute or method."
    
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

