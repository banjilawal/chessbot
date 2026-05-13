# src/logic/token/database/kernel/operation/crud/exception/push/validator.py

"""
Module: logic.token.database.kernel.OPERATION.CRUD.exception.push.work
Author: Banji Lawal
Created: 2026-02-22
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_STACK_PUSH_FAILURE #======================#
    "TokenStackPushException",
]

from system import InsertionException

# ======================# TOKEN_STACK_PUSH_FAILURE #======================#
class TokenStackPushException(InsertionException):
    """
    Role:
        - Error Variable Identifier
        - Exception Chain Layer 2
        - Exception Messaging

    Responsibilities:
        1.  Indicate that pushing a token to the stack failed because the stack was full.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        msg: Optional[str]
        ex: Optional[Exception]
        err_code: Optional[str]

    Provides:

    Super Class:
        TokenDebugException
    """
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that pushing a token on to the stack failed.
        2.  Identify the TokenStackService method where the failure occurred.
        

    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]
        

    Provides:

    Super Class:
        InsertionException
    """
    OP = "Insertion"
    MTHD_RSLT = "InsertionResult"
    ERR_CODE = "INSERTION_FAILURE"
    MSG = "Insertion method failed."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
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