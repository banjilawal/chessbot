# src/logic/system/collection/operation/insertion/exception/validator.py

"""
Module: logic.system.collection.operation.insertion.exception.work
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# INSERTION_FAILURE #======================#
    "InsertionException",
]

from system import CollectionOperationException

# ======================# INSERTION_FAILURE #======================#
class InsertionException(CollectionOperationException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate an insertion was unsuccessful.
        2.  Trace the method calls.

    Attributes:
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        mthd_rslt: Optional[ResultCategory]

    Provides:

    Super Class:
        CollectionOperationException
    """
    OP = "Insertion"
    MTHD_RSLT = "InsertionResult"
    ERR_CODE = "INSERTION_FAILURE"
    MSG = "Insertion method failed."
    
    def __init__(
            self,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            mthd_rslt: Optional[ResultCategory] = None,
    ):
        """
        Args:
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            mthd_rslt: Optional[ResultCategory]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            title=title,
            err_code=err_code,
            mthd_rslt=mthd_rslt,
        )