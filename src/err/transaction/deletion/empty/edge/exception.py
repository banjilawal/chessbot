# src/err/transaction/deletion/edge/exception.py

"""
Module: err.transaction.deletion.edge.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import PoppingEmptyStackException


__all__ = [
    # ======================# POPPING_EMPTY_EDGE_STACK_ERROR #======================#
    "PoppingEmptyEdgeStackException",
]

# ======================# POPPING_EMPTY_EDGE_STACK_ERROR #======================#
class PoppingEmptyEdgeStackException(PoppingEmptyStackException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicates that popping An EdgeStack failed because it was empty.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[str

    Provides:
    
    Super Class:
        PoppingEmptyStackException
    """
    MSG = "Cannot pop an empty Edge stack."
    ERR_CODE = "POPPING_EMPTY_EDGE_STACK_ERROR"
    
    def .__init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
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
    

