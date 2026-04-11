# src/err/pipeline/deletion/exception.py

"""
Module: err.pipeline.deletion.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import PipelineException

__all__ = [
    # ======================# DELETION_PIPELINE_FAILURE #======================#
    "DeletionPipelineException",
]

# ======================# DELETION_PIPELINE_FAILURE #======================#
class DeletionPipelineException(PipelineException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an error occurred in a DeletionPipeline.

    Attributes:
        op: Optional[str]
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        rslt_type: Optional[str]
            
    Provides:

    Super Class:
        DeletionPipeline
    """
    OP = "Deletion"
    MSG = "Error in DeletionPipeline."
    ERR_CODE = "DELETION_PIPELINE_FAILURE"
    RSLT_TYPE = "DeletionResult"
    
    def __init__(
            self,
            op: Optional[str] | None = None,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
            rslt_type: Optional[str] | None = None,
    ):
        """
        Args:
            op: Optional[str]
            msg: Optional[str]
            var: Optional[str]
            val: Optional[Any]
            ex: Optional[Exception]
            cls_name: Optional[str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            rslt_type: Optional[str]
        """
        op = op or self.OP
        msg = msg or self.MSG
        rslt_type = self.RSLT_TYPE
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
            rslt_type=rslt_type,
        )
