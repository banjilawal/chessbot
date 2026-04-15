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
        rslt_type: Optional[resultCategory]
        
    Provides:

    Super Class:
        UpdateException
    """
    OP = "Insertion"
    RSLT_TYPE = "InsertionResult"
    ERR_CODE = "TOKEN_POSITION_PUSH_EXCEPTION"
    MSG = "TokenCoordPushProcess method failed."
    
    def __init__(
            self, = None,
            msg: Optional[str] = None,
            mthd: Optional[str] = None,
            title: Optional[str] = None,
            ex: Optional[Exception] = None,
            err_code: Optional[str] = None,
            rslt_type: Optional[resultCategory] = None,
    ):
        """
        Args:
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
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