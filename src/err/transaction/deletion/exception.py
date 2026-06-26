# src/err/transaction/deletion/exception.py

"""
Module: err.transaction.deletion.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import TransactionException

__all__ = [
    # ======================# DELETION_FAILURE #======================#
    "DeletionException",
]

# ======================# DELETION_FAILURE #======================#
class DeletionException(TransactionException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        Indicates that an error prevented a deletion from completing.

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
    OP = "Deletion"
    MSG = "Deletion aborted."
    ERR_CODE = "DELETION_FAILURE"
    MTHD_RSLT_TYPE = "DeletionResult"
    
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
        mthd_rslt_type = mthd_rslt_type or self.MTHD_RSLT_TYPE
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
    

