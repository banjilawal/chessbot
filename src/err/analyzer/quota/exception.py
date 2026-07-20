# src/err/analyzer/quota/exception.py

"""
Module: err.analyzer.quota.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import AnalyzerException
from result import MethodResultType


__all__ = [
    # ======================# RANK_QUOTA_ANALYZER_ERROR #======================#
    "RankQuotaAnalyzerException",
]

# ======================# RANK_QUOTA_ANALYZER_ERROR #======================#
class RankQuotaAnalyzerException(AnalyzerException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an error occurred during a TokenStack's rank quota analysis.

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
        AnalyzerException
    """
    MSG = "Error occurred during a TokenStack's rank quota analysis."
    ERR_CODE = "RANK_QUOTA_ANALYZER_ERROR"
    MTHD_RSLT_TYPE = MethodResultType.ANALYSIS_RESULT
    
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
        mthd_rslt_type = mthd_rslt_type or self.MTHD_RSLT_TYPE
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
