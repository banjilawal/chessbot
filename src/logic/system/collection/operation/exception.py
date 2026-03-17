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

from logic.system import OperationException


# ======================# COLLECTION_OPERATION_FAILURE #======================#
class CollectionOperationException(OperationException):
    """
    Role:Debug Wrapper, Exception Chain Layer 2, Exception Messaging

    Responsibilities:
    1.  Indicate what Collection Operation failed.
    2.  Encapsulate the DebugException which describes the failure condition.

    Super Class:
        *   OperationException

    Provides:


    # INHERITED ATTRIBUTES:
        *   See OperationException class for inherited attributes.

    Attributes:
        *   err_code (str)
        *   msg (str)
        *   ex (Optional[Exception])
        *   mthd (Optional[str])
        *   op (Optional[str])
        *   rslt_type (Optional[str])

    # LOCAL METHODS:
   None

    # INHERITED METHODS:
        *   See OperationException class for inherited methods.
    """
    ERR_CODE = "COLLECT_OPERATION_FAILURE"
    MSG = "Collection operation failed."
    MTHD = Optional[str]
    OP = None
    RSLT_TYPE = None
    
    def __init__(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            mthd: Optional[str] = None,
            op: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        mthd = mthd or self.MTHD
        op = op or self.OP
        rslt_type = rslt_type or self.RSLT_TYPE
        
        super().__init__(err_code=err_code, msg=msg, ex=ex, mthd=mthd, op=op, rslt_type=rslt_type)