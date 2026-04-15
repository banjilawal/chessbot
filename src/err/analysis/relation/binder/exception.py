# src/err/analysis/relation/binder/exception.py

"""
Module: err.analysis.relation.binder.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional


__all__ = [
    # ======================# BOARD_BINDER_RELATION_ANALYSIS_FAILURE #======================#
    "BoardBinderAnalysisException",
]

from err.analysis.relation import RelationException


# ======================# BOARD_BINDER_RELATION_ANALYSIS_FAILURE #======================#
class BoardBinderAnalysisException(RelationException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an error prevented a BoardBinderRelations analysis from completing.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt: Optional[ResultCategory]
            
    Provides:

    Super Class:
        IdRelationException
    """
    MSG = "A BoardBinderRelations analysis step failed."
    ERR_CODE = "BOARD_BINDER_RELATION_ANALYSIS_FAILURE"
    
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
