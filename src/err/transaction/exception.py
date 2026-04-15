# src/err/transaction/exception.py

"""
Module: err.transaction.exception
Author: Banji Lawal
Created: 2026-02-25
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# TRANSACTION_FAILURE #======================#
    "TransactionException",
]

from err import ChessException


# ======================# TRANSACTION_FAILURE #======================#
class TransactionException(ChessException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Identifies which WorkerClass method the error was caught.
        2.  Encapsulates the DebugException created after, a code block triggers a variable into its
            error state.

    Naming Convention:
        1.  Prefix is the Class schema with the Result schema.
        2.  The transaction schema should match the Result subclass.
        3.  Transaction outcome. This will always be Failed.
        4.  Suffix is Exception.
        5.  The Syntax is: [ClassName][ResultClassName]FailedException

    Error Code Convention::
        1.  All caps, snake case. Prefix is the class schema followed by the transaction schema.
        2.  The transaction schema should match the type of result.
        3.  Suffix is Exception.
        2.  The Syntax is: [Class]_[TRANSACTION]_FAILURE

    Default MSG Convention:
        1.  Sentence whose first word is the class schema followed by the transaction schema.
        2.  The sentence ends with failed.
        3.  The Syntax is: [Class] transaction failed.

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
        ChessException
    """
    MSG = "Transaction failed."
    ERR_CODE = "TRANSACTION_FAILURE"

    _op = Optional[str]
    _mthd_rslt = Optional[str]
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            cls_mthd: Optional[str] = None,
            cls_name: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            mthd_rslt: Optional[ResultCategory] = None,
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
            mthd_rslt: Optional[str
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
        self._mthd_rslt = mthd_rslt
    
    @property
    def mthd_rslt(self) -> Optional[str]:
        return self._mthd_rslt
    
    def __str__(self):
        return f"{super().__str__()},  mthd_rslt:{self._mthd_rslt}"


    

