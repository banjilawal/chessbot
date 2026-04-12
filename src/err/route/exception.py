# src/err/route/exception.py

"""
Module: err.route.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# EXECUTION_ROUTE_EXCEPTION #======================#
    "ExecutionRouteException",
]

from err import ChessException


# ======================# EXECUTION_ROUTE_EXCEPTION #======================#
class ExecutionRouteException(ChessException):
    """
    Role:
        -   Error Tracing
    
    Responsibilities:
        1.  Indicate that an execution route was missing from the logic.
   
    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]

    Provides

    Provides:
    
    Super Class:
        ChessException
    """
    MSG = "Missing execution route."
    ERR_CODE = "EXECUTION_ROUTE_EXCEPTION"
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
            cls_mthd: Optional[str] = None,
            err_code: Optional[str] = None,
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
