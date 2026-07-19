# src/err/builder/space/linear/exception.py

"""
Module: err.builder.space.linear.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import SpaceBuilderException
from result import MethodResultType

__all__ = [
    # ======================# LINEAR_SPACE_BUILDER_FAILURE #======================#
    "LinearSpaceBuilderException",
]
# ======================# LINEAR_SPACE_BUILDER_FAILURE #======================#
class LinearSpaceBuilderException(SpaceBuilderException):
    """
    Role:
        -   Failure Tracing

    Responsibilities:
        1.  Indicate that a LinearSpace instance encountered an error.

    Attributes:
        msg: str
        err_code: str
        var: Optional[str]
        val: Optional[Any]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        ex: Optional[Exception]
        mthd_rslt_type: Optional[MethodResultType]
            
    Provides:

    Super Class:
        SpaceBuilderException
    """
    MSG = "An error occurred in a LinearSpace."
    ERR_CODE = "LINEAR_SPACE_BUILDER_FAILURE"
    
    def __init__(
            self,
            msg: str = MSG,
            err_code: str = ERR_CODE,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
            Args:
            msg: str
            err_code: str
            var: Optional[str]
            val: Optional[Any]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            ex: Optional[Exception]
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