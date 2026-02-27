# src/chess/system/service/pipeline/exception/super.py

"""
Module: chess.system.service.pipeline.exception.super
Author: Banji Lawal
Created: 2025-11-18
"""

from __future__ import annotations
from typing import Optional


__all__ = [
    # ======================# PIPELINE_EXCEPTION #======================#
    "PipelineException",
]

from chess.system import AnchorException


# ======================# PIPELINE_EXCEPTION #======================#
class PipelineException(AnchorException):
    """
    # ROLE: Information, Reporting, Debug

    # RESPONSIBILITIES:
    1.  Locus of attention for PipelineDebugExceptions.

    # PARENT:
        *   AnchorException

    # PROVIDES:
    None

    # LOCAL ATTRIBUTES:
    None

    # INHERITED ATTRIBUTES:
        *   See AnchorException class for inherited attributes.

    # CONSTRUCTOR PARAMETERS:
        *   msg (str)
        *   err_code (str)
        *   ex (Optional[Exception])
        *   cls_name (Optional[str])

    # LOCAL METHODS:
    None

    # INHERITED METHODS:
        *   See AnchorException class for inherited methods.
    """
    ERR_CODE = "PIPELINE_EXCEPTION"
    MSG = "Pipeline raised an exception."
    CLS_NAME = "Pipeline"
        
    def super(
            self,
            err_code: Optional[str] = None,
            msg: Optional[str] = None,
            ex: Optional[Exception] = None,
            cls_name: Optional[str] = None,
    ):
        err_code = err_code or self.ERR_CODE
        msg = msg or self.MSG
        cls_name = cls_name or self.CLS_NAME
        super().super(msg=msg, err_code=err_code, ex=ex, cls_name=cls_name)
