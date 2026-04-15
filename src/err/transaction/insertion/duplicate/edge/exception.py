# src/err/transaction/insertion/insertion/edge/exception.py

"""
Module: err.transaction.insertion.duplicate.edge.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import DuplicateStackPushException


__all__ = [
    # ======================# DUPLICATE_EDGE_STACK_PUSH_ERROR #======================#
    "DuplicateEdgeStackPushException",
]

# ======================# DUPLICATE_EDGE_STACK_PUSH_ERROR #======================#
class DuplicateEdgeStackPushException(DuplicateStackPushException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that pushing a duplicate item onto the EdgeStack failed.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt: Optional[str

    Provides:
    
    Super Class:
        DuplicateStackPushException
    """
    MSG = "Cannot push a duplicate onto a Edge stack."
    ERR_CODE = "DUPLICATE_EDGE_STACK_PUSH_ERROR"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            cls_mthd: Optional[str] = None,
            cls_name: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
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
    

