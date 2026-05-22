# src/err/transaction/insertion/exception.py

"""
Module: err.transaction.insertion.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import TransactionException

__all__ = [
    # ======================# INSERTION_FAILURE #======================#
    "InsertionException",
]

# ======================# INSERTION_FAILURE #======================#
class InsertionException(TransactionException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        Indicates that an error prevented a insertion from completing.

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
        TransactionException
    """
    OP = "Insertion"
    MSG = "Insertion aborted."
    ERR_CODE = "INSERTION_FAILURE"
    MTHD_RSLT_TYPE = "InsertionResult"
    
    def __init__(
            self,
            # op: Optional[str] = None,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            # mthd_rslt_type: Optional[MethodResultType] | None = None,
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
        mthd_rslt_type = self.MTHD_RSLT_TYPE
        err_code = err_code or self.ERR_CODE
        mthd_rslt_type = mthd_rslt or self.MTHD_RSLT_TYPE
        super().__init__(
            op=op,
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
            mthd_rslt_type=mthd_rslt,
        )
    

