# src/err/pipeline/insertion/exception.py

"""
Module: err.pipeline.insertion.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import PipelineException

__all__ = [
    # ======================# INSERTION_PIPELINE_FAILURE #======================#
    "InsertionPipelineException",
]

# ======================# INSERTION_PIPELINE_FAILURE #======================#
class InsertionPipelineException(PipelineException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an error occurred in a InsertionPipeline.

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
        InsertionPipeline
    """
    OP = "Insertion"
    MSG = "Error in InsertionPipeline."
    ERR_CODE = "INSERTION_PIPELINE_FAILURE"
    MTHD_RSLT = "InsertionResult"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt: Optional[ResultCategory] | None = None,
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
            mthd_rslt: Optional[ResultCategory]
        """
        op = op or self.OP
        msg = msg or self.MSG
        mthd_rslt = self.MTHD_RSLT
        err_code = err_code or self.ERR_CODE
        super().__init__(
            op=op,
            ex=ex,
            msg=msg,
            var=var,
            val=val,
            err_code=err_code,
            cls_name=cls_name,
            cls_mthd=cls_mthd,
            mthd_rslt=mthd_rslt,
        )
