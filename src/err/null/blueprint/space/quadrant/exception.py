# src/err/null/blueprint/space/quadrant/exception.py

"""
Module: err.null.blueprint.space.Quadrant is null.exception
Author: Banji Lawal
Created: 2026-04-04
version: 1.0.1
"""

from __future__ import annotations
from typing import Any, Optional

from err import SpaceblueprintNullException
from result import MethodResultType


__all__ = [
    # ======================# QUADRANT_SPACE_blueprint_NULL_ERROR #======================#
    "QuadrantblueprintNullException",
]
# ======================# QUADRANT_SPACE_blueprint_NULL_ERROR #======================#
class QuadrantblueprintNullException(SpaceblueprintNullException):
    """
    Role:
        -   Failure Tracing

    Responsibilities:
        1.  Indicate that a required QuadrantSpace.

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
        SpaceblueprintNullException
    """
    MSG = "QuadrantSpaceblueprint cannot be null."
    ERR_CODE = "QUADRANT_SPACE_blueprint_NULL_ERROR"
    
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