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
        rslt_type: Optional[resultCategory]

    Provides:
    
    Super Class:
        DeletionOperation
    """
    OP = "Deletion"
    RSLT_TYPE = "DeletionResult"
    ERR_CODE = "SQUARE_STACK_POP_FAILURE"
    MSG = "SquareStackService pop failed."
    
    def __init__(
            self, = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[resultCategory] = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            rslt_type: Optional[resultCategory]
        """
        op = op or self.OP
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        rslt_type = rslt_type or self.RSLT_TYPE
        
        super().__init__(
            ex=ex,
            op=op,
            msg=msg,
            mthd=mthd,
            err_code=err_code,
            rslt_type=rslt_type,
        )