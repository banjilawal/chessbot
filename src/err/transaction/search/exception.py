# src/err/transaction/search/exception.py

"""
Module: err.transaction.search.exception
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

from err import TransactionException

__all__ = [
    # ======================# SEARCH_FAILURE #======================#
    "SearchTransactionException",
]

# ======================# SEARCH_FAILURE #======================#
class SearchTransactionException(TransactionException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        Indicates that an error prevented a search from completing.

    Attributes:
        op: Optional[str]
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str

    Provides:
    
    Super Class:
        TransactionException
    """
    OP = "Search"
    MSG = "Search aborted."
    ERR_CODE = "SEARCH_FAILURE"
    RSLT_TYPE = "SearchResult"
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            cls_mthd: Optional[str] = None,
            cls_name: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            rslt_type: Optional[str
        """
        op = op or self.OP
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )


    

