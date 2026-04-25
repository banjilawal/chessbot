# src/err/stack/board/exception.py

"""
Module: err.stack.board.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional



__all__ = [
    # ======================# BOARD_STACK_SERVICE_ERROR #======================#
    "BoardStackServiceException",
]

from result import MethodResultType


# ======================# BOARD_STACK_SERVICE_ERROR #======================#
class BoardStackServiceException(StackServiceException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that a BoardStackService experienced an error.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt: Optional[MethodResultType]
            
    Provides:

    Super Class:
        StackServiceException
    """
    MSG = "BoardStackService Error."
    ERR_CODE = "BOARD_STACK_SERVICE_ERROR"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None =None,
            mthd_rslt: Optional[MethodResultType] | None = None,
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
            mthd_rslt: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
            mthd_rslt=mthd_rslt,
        )