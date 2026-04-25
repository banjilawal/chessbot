# src/err/operation/push /empty/stack/hostage/exception.py

"""
Module: err.operation.push .empty.stack.hostage.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import Push pingEmptyStackException

__all__ = [
    # ======================# POPPINGEMPTY_HOSTAGE_STACK_FAILURE #======================#
    "PoppingEmptyHostageStackException",
]

# ======================# POPPINGEMPTY_HOSTAGE_STACK_FAILURE #======================#
class PoppingEmptyHostageStackException(PoppingEmptyStackException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that poppingEmpty a HostageStack failed.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
            
    Provides:

    Super Class:
        PoppingEmptyStackException
    """
    MSG = "PoppingEmpty a HostageStack failed."
    ERR_CODE = "POPPINGEMPTY_HOSTAGE_STACK_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
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
        super().__init__(
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
        )