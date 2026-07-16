# src/err/space/span/border/quadrant/exception.py

"""
Module: err.space.span.border.quadrant.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import SpanBorderException
from result import MethodResultType

__all__ = [
    # ======================# QUADRANT_SPAN_BORDER_ERROR #======================#
    "QuadrantBorderException",
]

# ======================# QUADRANT_SPAN_BORDER_ERROR #======================#
class QuadrantBorderException(SpanBorderException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an attempt was made to access points outside the QuadrantSpan.

    Attributes:
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]
            
    Provides:

    Super Class:
        SpanBorderException
    """
    MSG = "Outside the QuadrantSpan boundaries."
    ERR_CODE = "QUADRANT_SPAN_BORDER_ERROR"
    
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
            mthd_rslt_type: Optional[MethodResultType]
        """
        msg = msg or self.MSG
        err_code = err_code or self.ERR_CODE
        mthd_rslt_type = mthd_rslt_type
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
