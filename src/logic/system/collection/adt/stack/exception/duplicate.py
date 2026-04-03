# src/logic/system/collection/adt/stack/exception/duplicate.py

"""
Module: logic.system.collection.adt.stack.exception.duplicate
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# ADDING_DUPLICATE_ITEM_EXCEPTION #======================#
    "PushingDuplicateItemException",
]

from logic.system import StackServiceDebugException


# ======================# ADDING_DUPLICATE_ITEM_EXCEPTION #======================#
class PushingDuplicateItemException(StackServiceDebugException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate an insertion failed because the item was already in the collection.

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
    ERR_CODE = "ADDING_DUPLICATE_ITEM_EXCEPTION"
    MSG = "Item is already in the stack."
    
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