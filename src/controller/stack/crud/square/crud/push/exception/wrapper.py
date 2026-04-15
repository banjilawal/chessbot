# src/logic/square/database/kernel/operation/crud/exception/push/validator.py

"""
Module: logic.square.database.kernel.OPERATION.CRUD.exception.push.work
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# SQUARE_STACK_PUSH_FAILURE #======================#
    "SquareStackPushException",
]

from system import InsertionException

# ======================# SQUARE_STACK_PUSH_FAILURE #======================#
class SquareStackPushException(InsertionException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate that pushing a square to the schema failed because the schema was full.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        SquareDebugException
    """
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that pushing a square on to the schema failed.
        2.  Identify the SquareStackService method where the failure occurred.
        

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[resultCategory]
        

    Provides:

    Super Class:
        InsertionException
    """
    OP = "Insertion"
    RSLT_TYPE = "InsertionResult"
    ERR_CODE = "INSERTION_FAILURE"
    MSG = "Insertion method failed."
    
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