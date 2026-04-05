# src/logic/token/database/kernel/operation/crud/pop/exception/empty.py

"""
Module: logic.token.database.kernel.operation.crud.pop.exception.empty
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_STACK_POP_FAILURE #======================#
    "TokenStackPopException",
]

from system import DeletionException

# ======================# TOKEN_STACK_POP_FAILURE #======================#
class TokenStackPopException(DeletionException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1
        -   Exception Messaging

    Responsibilities:
        1.  Indicate a TokenStackStack pop was unsuccessful.
        2.  Identify the TokenStackService method where the pop operation failed.
        
    Attributes:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]

    Provides:
    
    Super Class:
        DeletionOperation
    """
    OP = "Deletion"
    RSLT_TYPE = "DeletionResult"
    ERR_CODE = "TOKEN_STACK_POP_FAILURE"
    MSG = "TokenStackService pop failed."
    
    def __init__(
            self,
            op: Optional[str] = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[str] = None,
    ):
        """
        Args:
            op: Optional[str]
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            err_code: Optional[str]
            rslt_type: Optional[str]
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