# src/logic/system/collection/operation/deletion/exception/validator.py

"""
Module: logic.system.collection.operation.deletion.exception.work
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# DELETION_FAILURE #======================#
    "DeletionException",
]

from system import CollectionOperationException


# ======================# DELETION_FAILURE #======================#
class DeletionException(CollectionOperationException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1,
        -   Exception Messaging

    Responsibilities:
        1.  Indicate a deletion was unsuccessful.
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
        CollectionOperation
    """
    OP = "Deletion"
    MTHD_RSLT = "DeletionResult"
    ERR_CODE = "DELETION_FAILURE"
    MSG = "Deletion method failed."
    
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



