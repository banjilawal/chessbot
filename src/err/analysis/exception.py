# src/err/analysis/exception.py

"""
Module: err.analysis.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import ChessException

__all__ = [
    # ======================# ANALYSIS_FAILURE #======================#
    "AnalysisException",
]

from result import MethodResultType


# ======================# ANALYSIS_FAILURE #======================#
class AnalysisException(ChessException):
    """
    Role:
        -   Failure Tracing

    Responsibilities:
        1.  Indicate that an error prevented the analysis from completing the task.

    Attributes:
        msg: str
        err_code: str
        var: Optional[str]
        val: Optional[Any]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        ex: Optional[Exception]
        mthd_rslt: Optional[ResultCategory]
            
    Provides:

    Super Class:
        ChessException
    """
    MSG = "Analysis failed"
    ERR_CODE = "ANALYSIS_FAILURE"
    MTHD_RSLT = MethodResultType.ANALYSIS_RESULT
    
    def __init__(
            self,
            msg: str = MSG,
            err_code: str = ERR_CODE,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            mthd_rslt: Optional[MethodResultType] | None = None,
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
            mthd_rslt: Optional[ResultCategory]
        """
        msg = msg or self.MSG
        mthd_rslt = mthd_rslt or self.MTHD_RSLT
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