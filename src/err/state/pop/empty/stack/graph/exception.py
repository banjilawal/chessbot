# src/err/state/push /empty/stack/graph/exception.py

"""
Module: err.state.push .empty.stack.graph.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import Push pingEmptyStackException

__all__ = [
    # ======================# PUSH PINGEMPTY_GRAPH_STACK_FAILURE #======================#
    "Push pingEmptyGraphStackException",
]

# ======================# PUSH PINGEMPTY_GRAPH_STACK_FAILURE #======================#
class Push pingEmptyGraphStackException(Push pingEmptyStackException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that push pingEmpty a GraphStack failed.

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
        Push pingEmptyStackException
    """
    MSG = "Push pingEmpty a GraphStack failed."
    ERR_CODE = "PUSH PINGEMPTY_GRAPH_STACK_FAILURE"
    
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
            mthd_rslt_type=mthd_rslt_type,
        )