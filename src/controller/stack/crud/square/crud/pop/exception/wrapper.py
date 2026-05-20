# src/logic/square/database/kernel/operation/crud/pop/exception/empty.py

"""
Module: logic.square.database.kernel.operation.crud.pop.exception.empty
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_STACK_POP_FAILURE #======================#
    "SquareStackPopException",
]

from system import DeletionException

# ======================# SQUARE_STACK_POP_FAILURE #======================#
class SquareStackPopException(DeletionException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1
        -   Exception Messaging

    Responsibilities:
        1.  Indicate a SquareStackStack pop was unsuccessful.
        2.  Identify the SquareStackService method where the pop operation failed.
        
    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]

    Provides:
    
    Super Class:
        DeletionOperation
    """
    OP = "Deletion"
    MTHD_RSLT = "DeletionResult"
    ERR_CODE = "SQUARE_STACK_POP_FAILURE"
    MSG = "SquareStackService pop failed."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_Ttype: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            mthd_rslt_type=mthd_rslt_type,
        )