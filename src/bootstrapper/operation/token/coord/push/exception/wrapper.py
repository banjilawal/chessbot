# src/logic/token/service/operation/promotion/exception/validator.py

"""
Module: logic.token.service.operation.promotion.exception.work
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_POSITION_PUSH_EXCEPTION #======================#
    "TokenPushCoordException",
]

from system import InsertionException, UpdateException

# ======================# TOKEN_POSITION_PUSH_EXCEPTION #======================#
class TokenPushCoordException(InsertionException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that the TokenPushCoord exception was aborted.
        2.  Identify the method where the error occurred.
        
    Attributes:
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]
        
    Provides:

    Super Class:
        UpdateException
    """
    OP = "Insertion"
    MTHD_RSLT = "InsertionResult"
    ERR_CODE = "TOKEN_POSITION_PUSH_EXCEPTION"
    MSG = "TokenCoordPushProcess method failed."
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_Ttype: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
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