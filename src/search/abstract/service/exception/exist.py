# src/logic/system/search/service/exception/exist.py

"""
Module: logic.system.search.service.exception.exist
Author: Banji Lawal
Created: 2026-03-31
Version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

__all__ = [
    # ======================# ITEM_NOT_FOUND_EXCEPTION #======================#
    "ItemNotFoundException",
]

from system import SearchServiceDebugException


# ======================# ITEM_NOT_FOUND_EXCEPTION #======================#
class ItemNotFoundException(SearchServiceDebugException):
    """
    Role:
        -   Exception Chain Layer 0
        -   Exception coverage target
    
    Responsibilities:
        1.  Indicate that no item matching the search criteria was found.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
    
    Provides
    
    Super Class:
        SearchServiceDebugException
    """
    ERR_CODE = "ITEM_NOT_FOUND_EXCEPTION"
    MSG = "No item matching the search criteria was found."
    
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