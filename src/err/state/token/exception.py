# src/err/state/token/exception.py

"""
Module: err.state.token.exception
Author: Banji Lawal
Created: 2026-04-07
version: 1.0.0
"""

from __future__ import annotations
from typing import Any, Optional

from err import StateException


__all__ = [
    # ======================# TOKEN_STATE_ERROR #======================#
    "TokenStateException",
]

# ======================# TOKEN_STATE_ERROR #======================#
class TokenStateException(StateException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate an operation failed because a Token was not in the correct state.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]
            
    Provides:

    Super Class:
        StateException
    """
    MSG = "Token is not in the correct state to execute the operation"
    ERR_CODE = "TOKEN_STATE_ERROR"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        Args:
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt_type = mthd_rslt_type or self.MTHD_RSLT
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
            mthd_rslt_type=mthd_rslt_type,
        )
