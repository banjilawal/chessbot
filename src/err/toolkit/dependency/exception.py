# src/err/toolkit/EmptyDependencyList/exception.py

"""
Module: err.toolkit.EmptyDependencyList.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import ToolkitException

__all__ = [
    # ======================# TOOLKIT_OPERATION_LIST_EMPTY_ERROR #======================#
    "EmptyDependencyListException",
]

# ======================# TOOLKIT_OPERATION_LIST_EMPTY_ERROR #======================#
class EmptyDependencyListException(ToolkitException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a Toolkit's operation list is empty.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
            
    Provides:

    Super Class:
        ToolkitException
    """
    MSG = "Toolkit's operation list cannot be empty."
    ERR_CODE = "TOOLKIT_OPERATION_LIST_EMPTY_ERROR"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
    ):
        """
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
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
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )
