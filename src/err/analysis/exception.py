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

from result.category import ResultCategory


# ======================# ANALYSIS_FAILURE #======================#
class AnalysisException(ChessException):
    """
    Role:
        -   Error Tracing

    Responsibilities
        1.  Indicate that an error prevented an analysis from completing its work.
        
    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[ResultCategory]
            
    Provides:

    Super Class:
        ChessException
    """
    MSG = "Analysis step failed."
    ERR_CODE = "ANALYSIS_FAILURE"
    RSLT_TYPE = "AnalysisResult"
    _rslt_type = Optional[ResultCategory]
    
    def __init__(
            self,
            msg: Optional[str] = None,
            var: Optional[str] = None,
            val: Optional[Any] = None,
            cls_mthd: Optional[str] = None,
            cls_name: Optional[str] = None,
            ex: Optional[Exception] = None,
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
        rslt_type = self.RSLT_TYPE
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
        self._rslt_type = rslt_type
    
    @property
    def rslt_type(self) -> Optional[str]:
        return self._rslt_type
    
    def __str__(self):
        return f"{super().__str__()},  rslt_type:{self._rslt_type}"