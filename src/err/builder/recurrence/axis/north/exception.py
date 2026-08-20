# src/err/builder/recurrence/quadrant/north/exception.py

"""
Module: err.builder.recurrence.quadrant.north.exception
Author: Banji Lawal
Created: 2026-04-04
version: 0.0.2
"""

from __future__ import annotations
from typing import Any, Optional

from err import QuadrantRecurrenceBuilderException
from result import MethodResultType


__all__ = [
    # ======================# NORTH_QUADRANT_RECURRENCE_BUILDER_FAILURE #======================#
    "NorthQuadrantRecurrenceBuilderException",
]

# ======================# NORTH_QUADRANT_RECURRENCE_BUILDER_FAILURE #======================#
class NorthQuadrantRecurrenceBuilderException(QuadrantRecurrenceBuilderException):
    """
    Role:
        -   Error Tracing

    Responsibilities:
        1.  Indicating a NorthQuadrantRecurrenceBuilder failed.

    Attributes:
        msg: Optional[str]
        var: Optional[str]
        val: Optional[Any]
        ex: Optional[Exception]
        cls_name: Optional[str]
        cls_mthd: Optional[str]
        err_code: Optional[str]
        mthd_rslt_type: Optional[MethodResultType]
        
    Provides:

    Super Class:
        QuadrantRecurrenceBuilderException
    """
    MSG = "NorthQuadrantRecurrenceBuilder failure."
    ERR_CODE = "NORTH_QUADRANT_RECURRENCE_BUILDER_FAILURE"
    
    def __init__(
            self,
            msg: Optional[str] | None = None,
            var: Optional[str] | None = None,
            val: Optional[Any] | None = None,
            cls_mthd: Optional[str] | None = None,
            cls_name: Optional[str] | None = None,
            ex: Optional[Exception] | None = None,
            err_code: Optional[str] | None = None,
            mthd_rslt_type: Optional[MethodResultType] | None = None,
    ):
        """
        args:
            Msg: Optional[str]
            Var: Optional[str]
            val: Optional[any]
            ex: Optional[Exception]
            cls_name: Optional[Str]
            cls_mthd: Optional[str]
            err_code: Optional[str]
            mthd_rslt_type: Optional[MethodResultType]
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
           mthd_rslt_type=mthd_rslt_type,
        )