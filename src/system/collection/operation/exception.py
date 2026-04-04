# src/logic/system/collection/operation/exception.py

"""
Module: logic.system.operation.exception
Author: Banji Lawal
Created: 2025-11-18
Version: 1.0.0
"""

from typing import Optional


__all__ = [
    # ======================# COLLECTION_OPERATION_FAILURE #======================#
    "CollectionOperationException",
]

from system import OperationException


# ======================# COLLECTION_OPERATION_FAILURE #======================#
class CollectionOperationException(OperationException):
    """
    Role:
        -   Process Identifier
        -   Exception Chain Layer 1
        -   Exception Messaging

    Responsibilities:
        1.  Indicate what Collection Operation failed.
        2.  Encapsulate the DebugException which describes the failure condition.

    Attributes:
        op: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]
        rslt_type: Optional[str]

    Provides:

    Super Class:
        TransactionException
    """
    MSG = "Collection operation failed."
    ERR_CODE = "COLLECT_OPERATION_FAILURE"
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
            ex: Optional[Exception]
            err_code: Optional[str]
            rslt_type: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            title=title,
            err_code=err_code,
            rslt_type=rslt_type,
        )



