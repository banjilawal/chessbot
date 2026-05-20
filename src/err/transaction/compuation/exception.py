# src/err/transaction/computation/exception.py

"""
Module: err.transaction.computation.exception
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

from err import TransactionException

__all__ = [
    # ======================# COMPUTATION_FAILURE #======================#
    "ComputationTransactionException",
]

# ======================# COMPUTATION_FAILURE #======================#
class ComputationTransactionException(TransactionException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        Indicates that an error prevented a computation from completing.

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
    OP = "Computation"
    MSG = "Computation aborted."
    ERR_CODE = "COMPUTATION_FAILURE"
    MTHD_RSLT = "ComputationResult"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
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
            mthd_rslt_type: Optional[str
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt_type = mthd_rslt_type or self.MTHD_RSLT
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
            mthd_rslt_type=mthd_rslt_type,
        )


    

