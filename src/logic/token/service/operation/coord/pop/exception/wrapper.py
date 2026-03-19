# src/logic/token/service/operation/promotion/exception/wrapper.py

"""
Module: logic.token.service.operation.promotion.exception.wrapper
Author: Banji Lawal
Created: 2026-02-08
version: 1.0.0
"""

from __future__ import annotations
from typing import Optional

__all__ = [
    # ======================# TOKEN_COORD_POP_EXCEPTION #======================#
    "TokenPopCoordException",
]

from logic.system import DeletionException

# ======================# TOKEN_COORD_POP_EXCEPTION #======================#
class TokenPopCoordException(DeletionException):
    """
    Role:
        -   Worker Method Identification
        -   Exception Chain Layer 1
        -   Exception Messaging

    Responsibilities:
        1.  Indicate that the TokenPopCoord process was aborted.
        2.  Identify the method where the error occurred.
        
    Attributes:
        op: Optional[str]
        ex: Optional[str]
        msg: Optional[str]
        mthd: Optional[str]
        title: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]
        
    Provides:

    Super Class:
        UpdateException
    """
    OP = "Deletion"
    RSLT_TYPE = "DeletionResult"
    ERR_CODE = "TOKEN_COORD_POP_EXCEPTION"
    MSG = "TokenCoordPopProcess method failed."
    
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
            ex: Optional[str]
            msg: Optional[str]
            mthd: Optional[str]
            title: Optional[str]
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