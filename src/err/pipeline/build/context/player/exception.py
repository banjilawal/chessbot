# src/err/pipeline/build/context/player/exception.py

"""
Module: err.pipeline.build.context.player.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import ContextBuildPipelineException

__all__ = [
    # ======================# PLAYER_CONTEXT_BUILD_PIPELINE_FAILURE #======================#
    "PlayerContextBuildPipelineException",
]

# ======================# PLAYER_CONTEXT_BUILD_PIPELINE_FAILURE #======================#
class PlayerContextBuildPipelineException(ContextBuildPipelineException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicate that an error occurred in an PlayerContextBuildPipeline.

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
        ContextBuildPipeline
    """
    MSG = "Error in PlayerContextBuildPipeline."
    ERR_CODE = "PLAYER_CONTEXT_BUILD_PIPELINE_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            ex: Optional[Exception] | None = None,
            cls_name: Optional[str] | None = None,
            cls_mthd: Optional[str] | None = None,
            err_code: Optional[str] | None = None,
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
